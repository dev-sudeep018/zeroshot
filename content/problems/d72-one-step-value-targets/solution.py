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

def td_value_targets(rewards, current_values, next_values, terminated, discount):
    r,v,n = [_vector(x) for x in (rewards,current_values,next_values)]
    done = _flags(terminated,len(r)); g = _unit(discount)
    if v.shape != r.shape or n.shape != r.shape: raise ValueError("Vector shapes differ")
    target = r+g*(1-done)*n
    return dict(targets=target, errors=target-v)
