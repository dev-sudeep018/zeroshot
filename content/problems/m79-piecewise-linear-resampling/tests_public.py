def run_tests(namespace, mode="all"):
    cases = [
        ('Interior interpolation', lambda f: assert_close(f([0,2,5],[0,4,1],[1,3,5]), np.array([2.0, 3.0, 1.0], dtype=float).reshape((3,)))),
        ('Endpoint extension', lambda f: assert_close(f([1,3],[2,6],[-1,1,4]), np.array([2.0, 2.0, 6.0], dtype=float).reshape((3,)))),
        ('Unsorted queries', lambda f: assert_close(f([0,1,2],[0,3,0],[1.5,.5,1]), np.array([1.5, 1.5, 3.0], dtype=float).reshape((3,)))),
        ('Constant values', lambda f: assert_close(f([0,4],[7,7],[0,2,8]), np.array([7.0, 7.0, 7.0], dtype=float).reshape((3,)))),
        ('Negative coordinates', lambda f: assert_close(f([-3,-1,2],[0,4,1],[-2,0]), np.array([2.0, 3.0], dtype=float).reshape((2,)))),
        ('Repeated queries', lambda f: assert_close(f([0,2],[1,5],[1,1,0]), np.array([3.0, 3.0, 1.0], dtype=float).reshape((3,)))),
        ('Reject duplicate samples', lambda f: rejects(f,[0,0],[1,2],[0])),
        ('Reject length mismatch', lambda f: rejects(f,[0,1],[2],[.5])),
        ('Reject empty queries', lambda f: rejects(f,[0,1],[1,2],[])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,2,5],[0,4,1],[1,3,5]), np.array([2.0, 3.0, 1.0], dtype=float).reshape((3,)))),
    ]
    return run_cases(namespace, 'linear_resample', cases, mode)
