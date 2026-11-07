def run_tests(namespace, mode="all"):
    cases = [
        ('Square root two', lambda f: assert_close(f([1,0,-2],1,2,5), np.array([1.0, 2.0, 1.3333333333333335, 1.4000000000000001, 1.4146341463414633, 1.41421143847487, 1.4142135620573204], dtype=float).reshape((7,)))),
        ('Linear root', lambda f: assert_close(f([2,-4],0,3,4), np.array([0.0, 3.0, 2.0, 2.0, 2.0, 2.0], dtype=float).reshape((6,)))),
        ('Latest estimate root', lambda f: assert_close(f([1,-2],0,2,3), np.array([0.0, 2.0, 2.0, 2.0, 2.0], dtype=float).reshape((5,)))),
        ('No iterations', lambda f: assert_close(f([1,0,-2],1,2,0), np.array([1.0, 2.0], dtype=float).reshape((2,)))),
        ('Negative root', lambda f: assert_close(f([1,0,-2],-2,-1,4), np.array([-2.0, -1.0, -1.3333333333333333, -1.4285714285714286, -1.4137931034482758, -1.41421143847487], dtype=float).reshape((6,)))),
        ('Cubic root', lambda f: assert_close(f([1,0,0,-2],1,2,4), np.array([1.0, 2.0, 1.1428571428571428, 1.2096774193548387, 1.265038533785313, 1.25971202333506], dtype=float).reshape((6,)))),
        ('Reject flat secant', lambda f: rejects(f,[1,0,1],-1,1,1)),
        ('Reject equal starting points', lambda f: rejects(f,[1,-2],1,1,2)),
        ('Reject escaping estimate', lambda f: rejects(f,[.001,-1],0,1,1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,0,-2],1,2,5), np.array([1.0, 2.0, 1.3333333333333335, 1.4000000000000001, 1.4146341463414633, 1.41421143847487, 1.4142135620573204], dtype=float).reshape((7,)))),
    ]
    return run_cases(namespace, 'secant_polynomial', cases, mode)
