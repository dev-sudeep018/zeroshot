def run_tests(namespace, mode="all"):
    cases = [
        ('Unequal row totals', lambda f: assert_close(f([[1,3],[2,0]]), {'conditional':np.array([[0.25, 0.75], [1.0, 0.0]], dtype=float).reshape((2, 2)),'row_mass':np.array([0.6666666666666666, 0.3333333333333333], dtype=float).reshape((2,))})),
        ('Empty row', lambda f: assert_close(f([[0,0],[2,2]]), {'conditional':np.array([[0.0, 0.0], [0.5, 0.5]], dtype=float).reshape((2, 2)),'row_mass':np.array([0.0, 1.0], dtype=float).reshape((2,))})),
        ('One column', lambda f: assert_close(f([[1],[3]]), {'conditional':np.array([[1.0], [1.0]], dtype=float).reshape((2, 1)),'row_mass':np.array([0.25, 0.75], dtype=float).reshape((2,))})),
        ('One row', lambda f: assert_close(f([[1,2,1]]), {'conditional':np.array([[0.25, 0.5, 0.25]], dtype=float).reshape((1, 3)),'row_mass':np.array([1.0], dtype=float).reshape((1,))})),
        ('Fractional counts', lambda f: assert_close(f([[.5,.5],[0,1]]), {'conditional':np.array([[0.5, 0.5], [0.0, 1.0]], dtype=float).reshape((2, 2)),'row_mass':np.array([0.5, 0.5], dtype=float).reshape((2,))})),
        ('Sparse rows', lambda f: assert_close(f([[0,2,0],[0,0,0],[3,0,0]]), {'conditional':np.array([[0.0, 1.0, 0.0], [0.0, 0.0, 0.0], [1.0, 0.0, 0.0]], dtype=float).reshape((3, 3)),'row_mass':np.array([0.4, 0.0, 0.6], dtype=float).reshape((3,))})),
        ('Reject all zero', lambda f: rejects(f,[[0,0]])),
        ('Reject negative count', lambda f: rejects(f,[[-1,2]])),
        ('Reject empty input', lambda f: rejects(f,[])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[1,3],[2,0]]), {'conditional':np.array([[0.25, 0.75], [1.0, 0.0]], dtype=float).reshape((2, 2)),'row_mass':np.array([0.6666666666666666, 0.3333333333333333], dtype=float).reshape((2,))})),
    ]
    return run_cases(namespace, 'conditional_rows', cases, mode)
