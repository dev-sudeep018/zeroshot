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

def generalized_advantages(rewards, values, terminated, discount, trace_decay):
    r = _vector(rewards); v = _vector(values); done = _flags(terminated,len(r))
    g = _unit(discount); lam = _unit(trace_decay)
    if len(v) != len(r)+1: raise ValueError("Supply T+1 values")
    delta = r + (g*(1-done)*v[1:] - v[:-1])
    a = np.empty_like(r); targets = np.empty_like(r)
    running = 0.0; target = v[-1]
    for t in range(len(r)-1,-1,-1):
        running = delta[t] + g*lam*(1-done[t])*running
        a[t] = running
        # Equivalent lambda-return recurrence avoids subtracting and then
        # adding a huge current value to recover a small terminal reward.
        target = r[t] + g*(1-done[t])*((1-lam)*v[t+1]+lam*target)
        targets[t] = target
    return dict(advantages=a, targets=targets)
