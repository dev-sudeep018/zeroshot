# Original ZeroShot implementation, Apache-2.0.
import numpy as np
import math


def _a(value):
    try:
        raw = np.asarray(value)
        if raw.dtype.kind not in 'iuf':
            raise ValueError('Use real numeric values, excluding booleans')
        out = raw.astype(float)
    except (TypeError, OverflowError) as exc:
        raise ValueError('Use real numeric values') from exc
    if not np.all(np.isfinite(out)) or np.any(np.abs(out) > 1e6):
        raise ValueError('Values must be finite with magnitude at most 1e6')
    return out


def _v(value):
    out = _a(value)
    if out.ndim != 1 or not 1 <= out.size <= 128:
        raise ValueError('Use a vector of length 1..128')
    return out


def _m(value):
    out = _a(value)
    if out.ndim != 2 or not all(1 <= n <= 128 for n in out.shape):
        raise ValueError('Use a matrix with dimensions 1..128')
    return out


def _s(value):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, float, np.integer, np.floating)):
        raise ValueError('Use a real scalar')
    return float(_a(value))


def _i(value, low, high):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)) or not low <= value <= high:
        raise ValueError('Integer outside documented range')
    return int(value)


def _p(value):
    out = _v(value)
    if np.any(out < 0) or not np.isclose(out.sum(), 1, rtol=0, atol=1e-8):
        raise ValueError('Probabilities must be nonnegative and sum to one')
    return out


def _same(x, y):
    if x.shape != y.shape:
        raise ValueError('Shapes must match exactly')


def _ids(value, n, k):
    out = _v(value)
    if out.size != n or np.any(out != np.floor(out)) or np.any((out < 0) | (out >= k)):
        raise ValueError('Invalid category labels')
    return out.astype(int)


def gaussian_em_step(values, weights, means, variances, variance_floor=1e-6):
    x=_v(values); w=_p(weights); mu=_v(means); var=_v(variances); floor=_s(variance_floor); _same(w,mu); _same(w,var)
    if np.any(w<=0) or np.any(var<1e-8) or not 1e-8<=floor<=1e6: raise ValueError('Invalid component variance or weight')
    logp=np.log(w)[None,:]-.5*(np.log(2*np.pi*var)[None,:]+(x[:,None]-mu[None,:])**2/var[None,:])
    maximum=logp.max(axis=1); scaled=np.exp(logp-maximum[:,None]); normalizer=scaled.sum(axis=1); responsibilities=scaled/normalizer[:,None]
    count=responsibilities.sum(axis=0)
    if np.any(count<=1e-12): raise ValueError('Numerically empty component')
    new_mu=responsibilities.T@x/count
    new_var=np.sum(responsibilities*(x[:,None]-new_mu[None,:])**2,axis=0)/count
    return {'weights':count/len(x),'means':new_mu,'variances':np.maximum(new_var,floor),'log_likelihood':float(np.sum(maximum+np.log(normalizer)))}
