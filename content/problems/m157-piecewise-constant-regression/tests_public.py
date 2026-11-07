def run_tests(namespace, mode="all"):
    cases = [
        ('Boundary decisions', lambda f: assert_close(f([0,2],[10,20,30],[-1,0,1,2,3]), {'indices':np.array([0, 1, 1, 2, 2], dtype=float).reshape((5,)),'predictions':np.array([10.0, 20.0, 20.0, 30.0, 30.0], dtype=float).reshape((5,))})),
        ('Single split', lambda f: assert_close(f([5],[-1,1],[4,5,6]), {'indices':np.array([0, 1, 1], dtype=float).reshape((3,)),'predictions':np.array([-1.0, 1.0, 1.0], dtype=float).reshape((3,))})),
        ('Unsorted queries', lambda f: assert_close(f([-2,0,3],[1,2,3,4],[4,-3,0]), {'indices':np.array([3, 0, 2], dtype=float).reshape((3,)),'predictions':np.array([4.0, 1.0, 3.0], dtype=float).reshape((3,))})),
        ('Repeated values', lambda f: assert_close(f([0,1],[7,7,7],[-1,.5,2]), {'indices':np.array([0, 1, 2], dtype=float).reshape((3,)),'predictions':np.array([7.0, 7.0, 7.0], dtype=float).reshape((3,))})),
        ('Extreme queries', lambda f: assert_close(f([-1,1],[2,4,8],[-100,100]), {'indices':np.array([0, 2], dtype=float).reshape((2,)),'predictions':np.array([2.0, 8.0], dtype=float).reshape((2,))})),
        ('Repeated query', lambda f: assert_close(f([0],[1,2],[0,0]), {'indices':np.array([1, 1], dtype=float).reshape((2,)),'predictions':np.array([2.0, 2.0], dtype=float).reshape((2,))})),
        ('Reject duplicate splits', lambda f: rejects(f,[0,0],[1,2,3],[1])),
        ('Reject unsorted splits', lambda f: rejects(f,[2,1],[1,2,3],[0])),
        ('Reject value count mismatch', lambda f: rejects(f,[0,1],[1,2],[0])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,2],[10,20,30],[-1,0,1,2,3]), {'indices':np.array([0, 1, 1, 2, 2], dtype=float).reshape((5,)),'predictions':np.array([10.0, 20.0, 20.0, 30.0, 30.0], dtype=float).reshape((5,))})),
    ]
    return run_cases(namespace, 'regression_bins', cases, mode)
