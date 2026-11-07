# Original ZeroShot validation helpers, Apache-2.0.
import numpy as np


def _reject_booleans(value):
    if isinstance(value,(bool,np.bool_)):
        raise ValueError("Boolean values are not numeric inputs")
    if isinstance(value,(list,tuple)):
        for item in value: _reject_booleans(item)


def _array(value):
    _reject_booleans(value)
    try:
        raw = np.asarray(value)
        if raw.dtype.kind not in 'iuf':
            raise ValueError('Use real numeric arrays')
        result = raw.astype(np.float64)
    except (TypeError, OverflowError) as exc:
        raise ValueError('Use real numeric arrays') from exc
    if not np.all(np.isfinite(result)) or np.any(np.abs(result)>1e30):
        raise ValueError('Values must be finite with magnitude at most 1e30')
    return result


def _scalar(value):
    if isinstance(value,(bool,np.bool_)) or not isinstance(value,(int,float,np.integer,np.floating)):
        raise ValueError('Use a real scalar')
    try:
        result=float(value)
    except OverflowError as exc:
        raise ValueError('Scalar must be finite with magnitude at most 1e30') from exc
    if not np.isfinite(result) or abs(result)>1e30:
        raise ValueError('Scalar must be finite with magnitude at most 1e30')
    return result


def _integer(value,low,high):
    if isinstance(value,(bool,np.bool_)) or not isinstance(value,(int,np.integer)) or not low<=value<=high:
        raise ValueError('Integer parameter outside the documented bounds')
    return int(value)


def _tokens(value):
    if not isinstance(value,(list,tuple)) or len(value)>10000 or any(not isinstance(x,str) or not x for x in value):
        raise ValueError("Use a sequence of at most 10000 nonempty strings")
    return list(value)

def _vector(value, nonempty=True):
    a=_array(value)
    if a.ndim!=1 or (nonempty and a.size==0):
        raise ValueError("Use a vector with the documented length")
    return a

def _ints(value, low=0, high=1000000, nonempty=True):
    a=_vector(value,nonempty)
    if np.any(a!=np.floor(a)) or np.any(a<low) or np.any(a>high):
        raise ValueError("Integer-valued entries outside the documented bounds")
    return a.astype(np.int64)

def unscale_gradients(scaled_gradients,scale):
    _reject_booleans(scaled_gradients)
    try:
        raw=np.asarray(scaled_gradients)
        if raw.dtype.kind not in 'iuf': raise ValueError("Use real numeric gradients")
        g=raw.astype(np.float64)
    except (TypeError,OverflowError) as exc: raise ValueError("Invalid gradients") from exc
    s=_scalar(scale)
    if s<=0 or np.any(np.abs(g[np.isfinite(g)])>1e30): raise ValueError("Invalid scale or finite magnitude")
    with np.errstate(over='ignore',invalid='ignore',divide='ignore'): out=g/s
    skip=bool(np.any(~np.isfinite(g)) or np.any(~np.isfinite(out)))
    return dict(gradients=np.zeros_like(g) if skip else out,skip_step=skip)
