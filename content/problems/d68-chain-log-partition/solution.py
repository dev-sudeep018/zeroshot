# Original ZeroShot reference implementation; Apache-2.0.

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


def _shape(a, ndim):
    if a.ndim != ndim or any(n == 0 for n in a.shape):
        raise ValueError("Use the documented nonempty shape")
    return a


def _sigmoid(x):
    return np.exp(-np.logaddexp(0, -x))


def _softmax(x):
    z = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return z / z.sum(axis=-1, keepdims=True)


def _indices(x, size):
    raw = np.asarray(x)
    if raw.dtype.kind not in "iu" or raw.ndim != 1 or np.any(raw < 0) or np.any(raw >= size):
        raise ValueError("Use an integer index vector in range")
    return raw.astype(np.int64)


def _binary(x):
    x = _array(x)
    if np.any((x != 0) & (x != 1)):
        raise ValueError("Use numeric zero or one flags")
    return x


def chain_log_partition(emissions, transitions, start, end):
    e=_shape(_array(emissions),2); a,s,z=[_array(x) for x in (transitions,start,end)]; k=e.shape[1]
    if a.shape!=(k,k) or s.shape!=(k,) or z.shape!=(k,): raise ValueError("Invalid chain shapes")
    alpha=s+e[0]
    for row in e[1:]: alpha=np.logaddexp.reduce(alpha[:,None]+a,axis=0)+row
    return float(np.logaddexp.reduce(alpha+z))
