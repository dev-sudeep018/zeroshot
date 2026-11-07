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

def verify_draft(draft_probs,target_probs,tokens,uniforms):
    q=_array(draft_probs); p=_array(target_probs)
    if q.ndim!=2 or min(q.shape)==0 or p.shape!=q.shape or np.any(q<0) or np.any(p<0) or np.any(np.abs(q.sum(1)-1)>1e-8) or np.any(np.abs(p.sum(1)-1)>1e-8): raise ValueError("Invalid probability matrices")
    q=q/q.sum(1,keepdims=True); p=p/p.sum(1,keepdims=True)
    ids=_ints(tokens,0,q.shape[1]-1); u=_vector(uniforms)
    if ids.size!=q.shape[0] or u.shape!=ids.shape or np.any((u<0)|(u>=1)) or np.any(q[np.arange(len(ids)),ids]<=0): raise ValueError("Invalid draft sequence")
    accepted=[]
    for i,t in enumerate(ids):
        if u[i]<min(1.,p[i,t]/q[i,t]): accepted.append(int(t))
        else:
            correction=np.maximum(p[i]-q[i],0); total=correction.sum()
            if total<=0: raise ValueError("Rejection has no correction mass")
            return dict(accepted=accepted,rejected_at=i,correction=correction/total)
    return dict(accepted=accepted,rejected_at=-1,correction=np.zeros(q.shape[1]))
