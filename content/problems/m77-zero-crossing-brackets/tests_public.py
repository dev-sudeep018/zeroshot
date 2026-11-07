def run_tests(namespace, mode="all"):
    cases = [
        ('Direct crossing', lambda f: assert_close(f([-2,3]), np.array([[0, 1]], dtype=float).reshape((1, 2)))),
        ('Zero run bridge', lambda f: assert_close(f([-2,0,0,3]), np.array([[0, 3]], dtype=float).reshape((1, 2)))),
        ('Several crossings', lambda f: assert_close(f([1,-1,0,2,-3]), np.array([[0, 1], [1, 3], [3, 4]], dtype=float).reshape((3, 2)))),
        ('Touch without crossing', lambda f: assert_close(f([1,0,1]), np.array([], dtype=float).reshape((0, 2)))),
        ('All zeros', lambda f: assert_close(f([0,0,0]), np.array([], dtype=float).reshape((0, 2)))),
        ('Endpoint zeros', lambda f: assert_close(f([0,-2,0]), np.array([], dtype=float).reshape((0, 2)))),
        ('Reject empty', lambda f: rejects(f,[])),
        ('Reject matrix', lambda f: rejects(f,[[1,-1]])),
        ('Reject boolean', lambda f: rejects(f,[True,False])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[-2,3]), np.array([[0, 1]], dtype=float).reshape((1, 2)))),
    ]
    return run_cases(namespace, 'zero_crossing_brackets', cases, mode)
