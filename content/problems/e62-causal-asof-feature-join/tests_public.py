def run_tests(namespace, mode="all"):
    cases = [
        ('Never read a future event', lambda f: assert_close(f([1,3], [[10],[30]], [0,2,3]), dict(indices=np.array([-1,0,1]),matched=np.array([False,True,True]),values=np.array([[0.],[10.],[30.]])))),
        ('Unsorted event rows', lambda f: assert_close(f([3,1], [[30],[10]], [2,4]), dict(indices=np.array([1,0]),matched=np.array([True,True]),values=np.array([[10.],[30.]])))),
        ('Last row wins timestamp tie', lambda f: assert_close(f([1,1], [[10],[20]], [1]), dict(indices=np.array([1]),matched=np.array([True]),values=np.array([[20.]])))),
        ('No events available', lambda f: assert_close(f([], np.empty((0,2)), [1]), dict(indices=np.array([-1]),matched=np.array([False]),values=np.zeros((1,2))))),
        ('No queries', lambda f: assert_close(f([1], [[2]], []), dict(indices=np.array([],dtype=int),matched=np.array([],dtype=bool),values=np.empty((0,1))))),
        ('Zero feature is still matched', lambda f: assert_close(f([1], [[0]], [1]), dict(indices=np.array([0]),matched=np.array([True]),values=np.array([[0.]])))),
        ('Reject mismatched rows', lambda f: rejects(f, [1,2], [[3]], [1])),
        ('Reject no feature columns', lambda f: rejects(f, [1], np.empty((1,0)), [1])),
        ('Reject nonfinite query time', lambda f: rejects(f, [1], [[2]], [np.inf])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1,3], [[10],[30]], [0,2,3]), dict(indices=np.array([-1,0,1]),matched=np.array([False,True,True]),values=np.array([[0.],[10.],[30.]]))))
    ]
    return run_cases(namespace, 'asof_features', cases, mode)
