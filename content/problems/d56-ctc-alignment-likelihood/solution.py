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


def ctc_probability(probabilities, labels, blank=0):
    p=_shape(_array(probabilities),2); t,c=p.shape
    blank=_integer(blank,0,c-1)
    raw=np.asarray(labels)
    lab=np.empty(0,dtype=np.int64) if raw.shape==(0,) else _indices(labels,c)
    if t>64 or not 2<=c<=32 or np.any(p<0) or np.any(p>1) or not np.allclose(p.sum(1),1,atol=1e-8,rtol=0) or np.any(lab==blank):
        raise ValueError("Invalid probabilities or target labels")
    if len(lab)>t: return 0.0
    ext=np.full(2*len(lab)+1,blank,dtype=int); ext[1::2]=lab
    a=np.zeros(len(ext)); a[0]=p[0,blank]
    if len(ext)>1: a[1]=p[0,ext[1]]
    for row in p[1:]:
        b=np.zeros_like(a)
        for s in range(len(ext)):
            total=a[s]
            if s>0: total+=a[s-1]
            if s>1 and ext[s]!=blank and ext[s]!=ext[s-2]: total+=a[s-2]
            b[s]=total*row[ext[s]]
        a=b
    return float(a[-1]+(a[-2] if len(a)>1 else 0))
