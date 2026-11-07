def run_tests(namespace, mode="all"):
    cases = [
        ('L shaped path', lambda f: assert_close(f([[0,0],[3,0],[3,4]],[0,2,5,7]), np.array([[0.0, 0.0], [2.0, 0.0], [3.0, 2.0], [3.0, 4.0]], dtype=float).reshape((4, 2)))),
        ('Repeated vertex', lambda f: assert_close(f([[0,0],[0,0],[2,0]],[0,1,2]), np.array([[0.0, 0.0], [1.0, 0.0], [2.0, 0.0]], dtype=float).reshape((3, 2)))),
        ('Unsorted queries', lambda f: assert_close(f([[0,0],[2,0],[2,2]],[4,1,3,0]), np.array([[2.0, 2.0], [1.0, 0.0], [2.0, 1.0], [0.0, 0.0]], dtype=float).reshape((4, 2)))),
        ('Diagonal segment', lambda f: assert_close(f([[0,0],[3,4]],[2.5]), np.array([[1.5, 2.0]], dtype=float).reshape((1, 2)))),
        ('Repeated endpoint', lambda f: assert_close(f([[0,0],[2,0],[2,0]],[0,2]), np.array([[0.0, 0.0], [2.0, 0.0]], dtype=float).reshape((2, 2)))),
        ('Negative positions', lambda f: assert_close(f([[-2,0],[0,0],[0,-3]],[1,3]), np.array([[-1.0, 0.0], [0.0, -1.0]], dtype=float).reshape((2, 2)))),
        ('Reject zero-length path', lambda f: rejects(f,[[1,1],[1,1]],[0])),
        ('Reject query beyond path', lambda f: rejects(f,[[0,0],[1,0]],[2])),
        ('Reject negative distance', lambda f: rejects(f,[[0,0],[1,0]],[-1])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[0,0],[3,0],[3,4]],[0,2,5,7]), np.array([[0.0, 0.0], [2.0, 0.0], [3.0, 2.0], [3.0, 4.0]], dtype=float).reshape((4, 2)))),
    ]
    return run_cases(namespace, 'resample_polyline', cases, mode)
