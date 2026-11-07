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

def beam_search(log_probs,start,eos,width,max_steps):
    a=_array(log_probs)
    if a.ndim!=2 or a.shape[0]!=a.shape[1] or not 1<=a.shape[0]<=50 or np.any(a>0): raise ValueError("Invalid transition table")
    start=_integer(start,0,a.shape[0]-1); eos=_integer(eos,0,a.shape[0]-1); width=_integer(width,1,100); steps=_integer(max_steps,0,20)
    beams=[([start],0.)]
    for _ in range(steps):
        expanded=[]
        for seq,score in beams:
            if seq[-1]==eos: expanded.append((seq,score))
            else: expanded.extend((seq+[j],score+float(a[seq[-1],j])) for j in range(a.shape[0]))
        beams=sorted(expanded,key=lambda item:(-item[1],item[0]))[:width]
        if all(seq[-1]==eos for seq,_ in beams): break
    seq,score=beams[0]; return dict(tokens=seq,score=score)
