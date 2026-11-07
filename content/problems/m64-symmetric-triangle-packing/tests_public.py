def run_tests(namespace, mode="all"):
    cases = [
        ('Three by three', lambda f: assert_close(f([[1,2,3],[2,4,5],[3,5,6]]), {'packed':np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float).reshape((6,)),'reconstructed':np.array([[1.0, 2.0, 3.0], [2.0, 4.0, 5.0], [3.0, 5.0, 6.0]], dtype=float).reshape((3, 3))})),
        ('Single entry', lambda f: assert_close(f([[7]]), {'packed':np.array([7.0], dtype=float).reshape((1,)),'reconstructed':np.array([[7.0]], dtype=float).reshape((1, 1))})),
        ('Diagonal matrix', lambda f: assert_close(f([[2,0],[0,3]]), {'packed':np.array([2.0, 0.0, 3.0], dtype=float).reshape((3,)),'reconstructed':np.array([[2.0, 0.0], [0.0, 3.0]], dtype=float).reshape((2, 2))})),
        ('Negative off-diagonal', lambda f: assert_close(f([[0,-2],[-2,0]]), {'packed':np.array([0.0, -2.0, 0.0], dtype=float).reshape((3,)),'reconstructed':np.array([[0.0, -2.0], [-2.0, 0.0]], dtype=float).reshape((2, 2))})),
        ('Zero matrix', lambda f: assert_close(f([[0,0],[0,0]]), {'packed':np.array([0.0, 0.0, 0.0], dtype=float).reshape((3,)),'reconstructed':np.array([[0.0, 0.0], [0.0, 0.0]], dtype=float).reshape((2, 2))})),
        ('Fractional values', lambda f: assert_close(f([[.5,.25],[.25,.75]]), {'packed':np.array([0.5, 0.25, 0.75], dtype=float).reshape((3,)),'reconstructed':np.array([[0.5, 0.25], [0.25, 0.75]], dtype=float).reshape((2, 2))})),
        ('Reject asymmetric', lambda f: rejects(f,[[1,2],[3,4]])),
        ('Reject rectangle', lambda f: rejects(f,[[1,2,3],[2,3,4]])),
        ('Reject complex', lambda f: rejects(f,[[1j]])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[1,2,3],[2,4,5],[3,5,6]]), {'packed':np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float).reshape((6,)),'reconstructed':np.array([[1.0, 2.0, 3.0], [2.0, 4.0, 5.0], [3.0, 5.0, 6.0]], dtype=float).reshape((3, 3))})),
    ]
    return run_cases(namespace, 'pack_symmetric', cases, mode)
