def run_tests(namespace, mode="all"):
    cases = [
        ('Missing observations', lambda f: assert_close(f([[2,99],[4,8]],[[True,False],[True,True]],-1), {'count':np.array([2, 1], dtype=float).reshape((2,)),'mean':np.array([3.0, 8.0], dtype=float).reshape((2,))})),
        ('Empty column', lambda f: assert_close(f([[1,2],[3,4]],[[False,True],[False,True]],7), {'count':np.array([0, 2], dtype=float).reshape((2,)),'mean':np.array([7.0, 3.0], dtype=float).reshape((2,))})),
        ('All observed', lambda f: assert_close(f([[1,3],[5,7]],[[True,True],[True,True]],0), {'count':np.array([2, 2], dtype=float).reshape((2,)),'mean':np.array([3.0, 5.0], dtype=float).reshape((2,))})),
        ('No observations', lambda f: assert_close(f([[4]],[[False]],-3), {'count':np.array([0], dtype=float).reshape((1,)),'mean':np.array([-3.0], dtype=float).reshape((1,))})),
        ('Observed zero', lambda f: assert_close(f([[0]],[[True]],9), {'count':np.array([1], dtype=float).reshape((1,)),'mean':np.array([0.0], dtype=float).reshape((1,))})),
        ('Unequal counts', lambda f: assert_close(f([[1,2,3],[4,5,6]],[[True,False,True],[False,True,True]],0), {'count':np.array([1, 1, 2], dtype=float).reshape((3,)),'mean':np.array([1.0, 5.0, 4.5], dtype=float).reshape((3,))})),
        ('Reject numeric mask', lambda f: rejects(f,[[1]],[[1]],0)),
        ('Reject mask shape', lambda f: rejects(f,[[1,2]],[[True]],0)),
        ('Reject nonfinite cell', lambda f: rejects(f,[[np.nan]],[[False]],0)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[2,99],[4,8]],[[True,False],[True,True]],-1), {'count':np.array([2, 1], dtype=float).reshape((2,)),'mean':np.array([3.0, 8.0], dtype=float).reshape((2,))})),
    ]
    return run_cases(namespace, 'observed_column_summary', cases, mode)
