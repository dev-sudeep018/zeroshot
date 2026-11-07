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


def permutation_mean_test(values, group_size, permutations):
    x=_v(values); n=len(x); k=_i(group_size,1,n-1); ids=_m(permutations)
    if ids.shape[1]!=n or np.any(ids!=np.floor(ids)) or not np.all(np.sort(ids,axis=1)==np.arange(n)): raise ValueError('Every row must be a permutation')
    observed=float(x[:k].mean()-x[k:].mean()); reordered=x[ids.astype(int)]; null=reordered[:,:k].mean(axis=1)-reordered[:,k:].mean(axis=1)
    return {'observed':observed,'null':null,'p_value':float((1+np.sum(np.abs(null)>=abs(observed)))/(1+len(null)))}
