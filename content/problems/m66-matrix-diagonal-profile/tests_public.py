def run_tests(namespace, mode="all"):
    cases = [
        ('Square grid', lambda f: assert_close(f([[1,2],[3,4]]), {'offsets':np.array([-1, 0, 1], dtype=float).reshape((3,)),'count':np.array([1, 2, 1], dtype=float).reshape((3,)),'mean':np.array([3.0, 2.5, 2.0], dtype=float).reshape((3,))})),
        ('Wide grid', lambda f: assert_close(f([[1,2,3],[4,5,6]]), {'offsets':np.array([-1, 0, 1, 2], dtype=float).reshape((4,)),'count':np.array([1, 2, 2, 1], dtype=float).reshape((4,)),'mean':np.array([4.0, 3.0, 4.0, 3.0], dtype=float).reshape((4,))})),
        ('Tall grid', lambda f: assert_close(f([[1,2],[3,4],[5,6]]), {'offsets':np.array([-2, -1, 0, 1], dtype=float).reshape((4,)),'count':np.array([1, 2, 2, 1], dtype=float).reshape((4,)),'mean':np.array([5.0, 4.5, 2.5, 2.0], dtype=float).reshape((4,))})),
        ('Single value', lambda f: assert_close(f([[9]]), {'offsets':np.array([0], dtype=float).reshape((1,)),'count':np.array([1], dtype=float).reshape((1,)),'mean':np.array([9.0], dtype=float).reshape((1,))})),
        ('Single row', lambda f: assert_close(f([[1,-2,4]]), {'offsets':np.array([0, 1, 2], dtype=float).reshape((3,)),'count':np.array([1, 1, 1], dtype=float).reshape((3,)),'mean':np.array([1.0, -2.0, 4.0], dtype=float).reshape((3,))})),
        ('Single column', lambda f: assert_close(f([[1],[-2],[4]]), {'offsets':np.array([-2, -1, 0], dtype=float).reshape((3,)),'count':np.array([1, 1, 1], dtype=float).reshape((3,)),'mean':np.array([4.0, -2.0, 1.0], dtype=float).reshape((3,))})),
        ('Reject vector', lambda f: rejects(f,[1,2])),
        ('Reject nonfinite', lambda f: rejects(f,[[np.inf]])),
        ('Reject empty row', lambda f: rejects(f,[[]])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[1,2],[3,4]]), {'offsets':np.array([-1, 0, 1], dtype=float).reshape((3,)),'count':np.array([1, 2, 1], dtype=float).reshape((3,)),'mean':np.array([3.0, 2.5, 2.0], dtype=float).reshape((3,))})),
    ]
    return run_cases(namespace, 'diagonal_profile', cases, mode)
