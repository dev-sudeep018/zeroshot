def run_tests(namespace, mode="all"):
    cases = [
        ('Single peak', lambda f: assert_close(f([0,3,0]), np.array([1], dtype=float).reshape((1,)))),
        ('Even plateau', lambda f: assert_close(f([0,2,2,0]), np.array([1], dtype=float).reshape((1,)))),
        ('Several peaks', lambda f: assert_close(f([0,2,0,3,3,3,1]), np.array([1, 4], dtype=float).reshape((2,)))),
        ('Endpoint excluded', lambda f: assert_close(f([3,3,1,0]), np.array([], dtype=float).reshape((0,)))),
        ('Constant signal', lambda f: assert_close(f([2,2,2]), np.array([], dtype=float).reshape((0,)))),
        ('Singleton', lambda f: assert_close(f([5]), np.array([], dtype=float).reshape((0,)))),
        ('Reject empty signal', lambda f: rejects(f,[])),
        ('Reject matrix', lambda f: rejects(f,[[1,2]])),
        ('Reject nonfinite', lambda f: rejects(f,[0,np.nan,0])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,3,0]), np.array([1], dtype=float).reshape((1,)))),
    ]
    return run_cases(namespace, 'plateau_peaks', cases, mode)
