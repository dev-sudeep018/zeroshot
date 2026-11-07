def run_tests(namespace, mode="all"):
    cases = [
        ('Repeated location', lambda f: assert_close(f(2,2,[[0,1],[0,1],[1,0]],[2,3,7]), {'sum':np.array([[0.0, 5.0], [7.0, 0.0]], dtype=float).reshape((2, 2)),'count':np.array([[0, 2], [1, 0]], dtype=float).reshape((2, 2))})),
        ('Negative measurements', lambda f: assert_close(f(1,2,[[0,0],[0,0],[0,1]],[3,-3,-2]), {'sum':np.array([[0.0, -2.0]], dtype=float).reshape((1, 2)),'count':np.array([[2, 1]], dtype=float).reshape((1, 2))})),
        ('Single cell', lambda f: assert_close(f(1,1,[[0,0]],[4]), {'sum':np.array([[4.0]], dtype=float).reshape((1, 1)),'count':np.array([[1]], dtype=float).reshape((1, 1))})),
        ('Sparse grid', lambda f: assert_close(f(3,3,[[2,2]],[0]), {'sum':np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=float).reshape((3, 3)),'count':np.array([[0, 0, 0], [0, 0, 0], [0, 0, 1]], dtype=float).reshape((3, 3))})),
        ('Row boundaries', lambda f: assert_close(f(2,1,[[1,0],[0,0]],[5,2]), {'sum':np.array([[2.0], [5.0]], dtype=float).reshape((2, 1)),'count':np.array([[1], [1]], dtype=float).reshape((2, 1))})),
        ('Repeated zero', lambda f: assert_close(f(1,1,[[0,0],[0,0]],[0,0]), {'sum':np.array([[0.0]], dtype=float).reshape((1, 1)),'count':np.array([[2]], dtype=float).reshape((1, 1))})),
        ('Reject coordinate outside grid', lambda f: rejects(f,2,2,[[2,0]],[1])),
        ('Reject fractional coordinate', lambda f: rejects(f,2,2,[[.5,0]],[1])),
        ('Reject length mismatch', lambda f: rejects(f,2,2,[[0,0]],[1,2])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,2,2,[[0,1],[0,1],[1,0]],[2,3,7]), {'sum':np.array([[0.0, 5.0], [7.0, 0.0]], dtype=float).reshape((2, 2)),'count':np.array([[0, 2], [1, 0]], dtype=float).reshape((2, 2))})),
    ]
    return run_cases(namespace, 'accumulate_grid', cases, mode)
