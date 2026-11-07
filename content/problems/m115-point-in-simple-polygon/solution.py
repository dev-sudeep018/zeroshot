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


def points_in_polygon(points, vertices):
    p=_m(points); v=_m(vertices)
    if p.shape[1]!=2 or v.shape[1]!=2 or len(v)<3 or np.any(v!=np.floor(v)) or np.any(np.abs(v)>100) or len(np.unique(v,axis=0))!=len(v): raise ValueError('Invalid polygon vertices')
    def cross(a,b,c):
        u=b-a; w=c-a; return float(u[0]*w[1]-u[1]*w[0])
    def on(a,b,q): return abs(cross(a,b,q))<=1e-9 and np.all(q>=np.minimum(a,b)-1e-9) and np.all(q<=np.maximum(a,b)+1e-9)
    n=len(v)
    if abs(sum(v[i,0]*v[(i+1)%n,1]-v[i,1]*v[(i+1)%n,0] for i in range(n)))<1e-9: raise ValueError('Zero polygon area')
    for i in range(n):
        a=v[i]; b=v[(i+1)%n]
        for j in range(i+1,n):
            if j==i+1 or (i==0 and j==n-1): continue
            c=v[j]; d=v[(j+1)%n]; s1=cross(a,b,c); s2=cross(a,b,d); s3=cross(c,d,a); s4=cross(c,d,b)
            if (s1*s2<0 and s3*s4<0) or on(a,b,c) or on(a,b,d) or on(c,d,a) or on(c,d,b): raise ValueError('Polygon is not simple')
    out=[]
    for q in p:
        inside=False; boundary=False
        for i in range(n):
            a=v[i]; b=v[(i+1)%n]
            if on(a,b,q): boundary=True; break
            if (a[1]>q[1])!=(b[1]>q[1]):
                hit=a[0]+(q[1]-a[1])*(b[0]-a[0])/(b[1]-a[1])
                if q[0]<hit: inside=not inside
        out.append(boundary or inside)
    return np.array(out,dtype=bool)
