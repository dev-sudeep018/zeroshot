def run_tests(namespace, mode="all"):
    cases = [
        ('Row swap required', lambda f: assert_close(f([[0,2],[3,4]],[4,11]), np.array([1.0, 2.0], dtype=float).reshape((2,)))),
        ('Three equations', lambda f: assert_close(f([[2,1,-1],[-3,-1,2],[-2,1,2]],[8,-11,-3]), np.array([2.0, 3.0000000000000004, -0.9999999999999999], dtype=float).reshape((3,)))),
        ('Single equation', lambda f: assert_close(f([[4]],[10]), np.array([2.5], dtype=float).reshape((1,)))),
        ('Identity matrix', lambda f: assert_close(f([[1,0],[0,1]],[3,-2]), np.array([3.0, -2.0], dtype=float).reshape((2,)))),
        ('Negative pivots', lambda f: assert_close(f([[-2,1],[1,-3]],[1,4]), np.array([-1.4, -1.8], dtype=float).reshape((2,)))),
        ('Triangular matrix', lambda f: assert_close(f([[2,1,3],[0,4,2],[0,0,5]],[13,14,15]), np.array([1.0, 2.0, 3.0], dtype=float).reshape((3,)))),
        ('Reject singular system', lambda f: rejects(f,[[1,2],[2,4]],[3,6])),
        ('Reject rectangular matrix', lambda f: rejects(f,[[1,2]],[1])),
        ('Reject tiny pivot', lambda f: rejects(f,[[1e-12]],[1])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[0,2],[3,4]],[4,11]), np.array([1.0, 2.0], dtype=float).reshape((2,)))),
    ]
    return run_cases(namespace, 'pivoted_linear_solve', cases, mode)
