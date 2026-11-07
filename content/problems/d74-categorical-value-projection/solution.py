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

def project_value_distribution(probabilities, atoms, reward, discount, terminal):
    p = _vector(probabilities); z = _vector(atoms); r = _scalar(reward); g = _unit(discount); done = _integer(terminal,0,1)
    if len(p)!=len(z) or len(z)<2 or np.any(p<0) or not np.isclose(p.sum(),1,rtol=0,atol=1e-8): raise ValueError("Invalid distribution")
    step = z[1]-z[0]
    if step < 1e-8 or not np.allclose(np.diff(z),step,rtol=1e-10,atol=1e-10): raise ValueError("Use an equally spaced increasing support")
    moved = np.clip(r+g*(1-done)*z,z[0],z[-1])
    out = np.zeros_like(p)
    for mass,value in zip(p,moved):
        # Interpolate between the actual supplied atoms, including supports
        # that are equally spaced only to the documented numeric tolerance.
        hi = int(np.searchsorted(z,value,side='left'))
        if z[hi] == value: out[hi] += mass
        else:
            lo = hi-1
            fraction = (value-z[lo])/(z[hi]-z[lo])
            out[lo] += mass*(1-fraction)
            out[hi] += mass*fraction
    return out
