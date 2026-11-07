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


def _a(x, ndim):
    def no_bool(v):
        if isinstance(v,(bool,np.bool_)): raise ValueError("Boolean inputs are not numeric data")
        if isinstance(v,(list,tuple)):
            for z in v: no_bool(z)
    no_bool(x)
    a=_array(x)
    if a.ndim!=ndim or any(n<1 or n>64 for n in a.shape) or a.size>65536:
        raise ValueError("Documented rank; axes 1..64, at most 65536 elements")
    if np.any(np.abs(a)>1e6): raise ValueError("Magnitude exceeds 1e6")
    return a
def _v(x): return _a(x,1)
def _m(x): return _a(x,2)
def _s(x):
    v=_scalar(x)
    if abs(v)>1e6: raise ValueError("Magnitude exceeds 1e6")
    return v
def _unit(x):
    v=_s(x)
    if not 0<=v<=1: raise ValueError("Use [0,1]")
    return v
def _ints(x,low=0,high=64):
    a=_v(x)
    if np.any(a!=np.floor(a)) or np.any(a<low) or np.any(a>high): raise ValueError("Invalid integer vector")
    return a.astype(np.int64)
def _same(*a):
    if any(x.shape!=a[0].shape for x in a[1:]): raise ValueError("Shapes must match")
def _prob(x,ndim=2):
    a=_a(x,ndim)
    if np.any(a<0) or not np.allclose(a.sum(axis=-1),1,atol=1e-8,rtol=0): raise ValueError("Probability rows must sum to one")
    return a/a.sum(axis=-1,keepdims=True)


def teacher_forcing_inputs(targets,predictions,draws,teacher_probability,start_id):
    y=_m(targets); p=_m(predictions); u=_m(draws); _same(y,p,u); q=_unit(teacher_probability); start=_integer(start_id,0,1000000)
    if y.shape[1]<2 or np.any(y!=np.floor(y)) or np.any(p!=np.floor(p)) or np.any(y<0) or np.any(p<0) or np.any((u<0)|(u>=1)): raise ValueError("Invalid tokens or draws")
    result=np.empty(y.shape,dtype=int); result[:,0]=start; result[:,1:]=np.where(u[:,:-1]<q,y[:,:-1],p[:,:-1])
    return result
