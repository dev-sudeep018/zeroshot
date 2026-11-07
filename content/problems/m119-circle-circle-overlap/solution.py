# Original ZeroShot implementation. Apache-2.0.
import math
import numpy as np


def _no_bool(value):
    if isinstance(value, (bool, np.bool_)):
        raise ValueError('Boolean values are not real-number inputs')
    if isinstance(value, (list, tuple)):
        for item in value:
            _no_bool(item)


def _a(value):
    _no_bool(value)
    try:
        raw = np.asarray(value)
        if raw.dtype.kind not in 'iuf':
            raise ValueError('Use real numeric inputs')
        out = raw.astype(float)
    except (TypeError, OverflowError) as exc:
        raise ValueError('Use real numeric inputs') from exc
    if not np.all(np.isfinite(out)) or np.any(np.abs(out) > 10000):
        raise ValueError('Use finite values with magnitude at most 10000')
    return out


def _v(value, low=1, high=64):
    a = _a(value)
    if a.ndim != 1 or not low <= len(a) <= high:
        raise ValueError('Invalid vector length or rank')
    return a


def _m(value):
    a = _a(value)
    if a.ndim != 2 or not all(1 <= n <= 64 for n in a.shape):
        raise ValueError('Use a nonempty matrix with axes at most 64')
    return a


def _s(value):
    if not isinstance(value, (int, float, np.integer, np.floating)):
        raise ValueError('Use a real scalar')
    return float(_a(value))


def _i(value, low, high):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)) or not low <= value <= high:
        raise ValueError('Integer outside the documented range')
    return int(value)


def _same(a, b):
    if a.shape != b.shape:
        raise ValueError('Shapes must match exactly')


def _b(value, shape):
    a = np.asarray(value)
    if a.dtype.kind != 'b' or a.shape != shape:
        raise ValueError('Use a boolean mask of the documented shape')
    return a.copy()


def _p(value):
    p = _v(value)
    if np.any(p < 0) or not np.isclose(p.sum(), 1, rtol=0, atol=1e-10):
        raise ValueError('Probabilities must be nonnegative and sum to one')
    return p / p.sum()


def _inc(value):
    a = _v(value, 2)
    if np.any(np.diff(a) <= 0):
        raise ValueError('Coordinates must be strictly increasing')
    return a


def _point(value, dim=2):
    a = _v(value)
    if len(a) != dim:
        raise ValueError('Wrong point dimension')
    return a


def _positive(a):
    if np.any(a < 1e-6):
        raise ValueError('Positive quantities must be at least 1e-6')


def _labels(value, n, k):
    a = _v(value)
    if len(a) != n or np.any(a != np.floor(a)) or np.any((a < 0) | (a >= k)):
        raise ValueError('Invalid integer-valued labels')
    return a.astype(int)


def disk_overlap(radius_a, radius_b, distance):
    r=_s(radius_a); s=_s(radius_b); d=_s(distance); _positive(r); _positive(s)
    if d<0: raise ValueError('Negative center distance')
    if d>=r+s: return 0.0
    if d<=abs(r-s): return math.pi*min(r,s)**2
    alpha=math.acos(float(np.clip((d*d+r*r-s*s)/(2*d*r),-1,1))); beta=math.acos(float(np.clip((d*d+s*s-r*r)/(2*d*s),-1,1)))
    rad=max(0,(-d+r+s)*(d+r-s)*(d-r+s)*(d+r+s)); area=r*r*alpha+s*s*beta-.5*math.sqrt(rad)
    return float(np.clip(area,0,math.pi*min(r,s)**2))
