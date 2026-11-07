def run_tests(namespace, mode="all"):
    cases = [
        ('Recover square', lambda f: assert_close(f([0,1,2],[0,1,4],[.5,1.5,3]), np.array([0.25, 2.25, 9.0], dtype=float).reshape((3,)))),
        ('Unsorted nodes', lambda f: assert_close(f([2,0,1],[4,0,1],[0,1,2]), np.array([0.0, 1.0, 4.0], dtype=float).reshape((3,)))),
        ('Constant data', lambda f: assert_close(f([-1,0,2],[3,3,3],[-2,1]), np.array([3.0, 3.0], dtype=float).reshape((2,)))),
        ('Linear data', lambda f: assert_close(f([-1,0,1],[-1,1,3],[.5,2]), np.array([2.0, 5.0], dtype=float).reshape((2,)))),
        ('Asymmetric quadratic', lambda f: assert_close(f([-2,1,3],[9,0,4],[-1,0,2]), np.array([4.000000000000001, 0.9999999999999998, 1.0], dtype=float).reshape((3,)))),
        ('Repeated query', lambda f: assert_close(f([0,1,2],[1,0,1],[.25,.25]), np.array([0.5625, 0.5625], dtype=float).reshape((2,)))),
        ('Reject duplicate nodes', lambda f: rejects(f,[0,0,1],[1,2,3],[0])),
        ('Reject wrong values length', lambda f: rejects(f,[0,1,2],[1,2],[0])),
        ('Reject distant query', lambda f: rejects(f,[0,1,2],[1,2,3],[11])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,1,2],[0,1,4],[.5,1.5,3]), np.array([0.25, 2.25, 9.0], dtype=float).reshape((3,)))),
    ]
    return run_cases(namespace, 'quadratic_interpolate', cases, mode)
