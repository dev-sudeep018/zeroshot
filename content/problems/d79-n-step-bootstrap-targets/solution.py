# Original ZeroShot implementation, Apache-2.0.
# Original ZeroShot validation helpers, Apache-2.0.
import numpy as np


def _array(value):
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


def _vector(value):
    a = _array(value)
    if a.ndim != 1 or not 1 <= a.size <= 256:
        raise ValueError("Use a vector with 1..256 entries")
    return a

def _matrix(value):
    a = _array(value)
    if a.ndim != 2 or any(n < 1 or n > 256 for n in a.shape):
        raise ValueError("Use a matrix with each dimension in 1..256")
    return a

def _unit(value):
    x = _scalar(value)
    if not 0 <= x <= 1:
        raise ValueError("Use a scalar between zero and one")
    return x

def _flags(value, size):
    a = _vector(value)
    if a.size != size or np.any((a != 0) & (a != 1)):
        raise ValueError("Use a matching vector of numeric zero or one flags")
    return a

def n_step_targets(rewards, values, terminated, discount, steps):
    r = _vector(rewards); v = _vector(values); done = _flags(terminated,len(r)); g = _unit(discount); n = _integer(steps,1,256)
    if len(v)!=len(r)+1: raise ValueError("Supply T+1 values")
    out = np.empty_like(r)
    for t in range(len(r)):
        total = 0.0; factor = 1.0; end = t; terminal = False
        for j in range(t,min(t+n,len(r))):
            total += factor*r[j]; factor *= g; end = j+1
            if done[j]: terminal = True; break
        if not terminal: total += factor*v[end]
        out[t] = total
    return out
