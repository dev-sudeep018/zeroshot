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

def welford_update(count,mean,m2,values):
    n=_integer(count,0,1000000); mu=_scalar(mean); total=_scalar(m2); x=_vector(values,False)
    if n+x.size>1000000 or total<0 or (n==0 and (mu!=0 or total!=0)): raise ValueError("Invalid moment state")
    for value in x:
        n+=1; delta=float(value)-mu; mu+=delta/n; total+=delta*(float(value)-mu)
    return dict(count=n,mean=mu,m2=total)
