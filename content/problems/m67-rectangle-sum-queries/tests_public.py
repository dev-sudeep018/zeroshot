def run_tests(namespace, mode="all"):
    cases = [
        ('Whole and corner', lambda f: assert_close(f([[1,2],[3,4]],[[0,0,2,2],[1,1,2,2]]), np.array([10.0, 4.0], dtype=float).reshape((2,)))),
        ('Empty rectangles', lambda f: assert_close(f([[1,2]],[[0,0,0,2],[0,1,1,1]]), np.array([0.0, 0.0], dtype=float).reshape((2,)))),
        ('Overlapping queries', lambda f: assert_close(f([[1,2,3],[4,5,6]],[[0,0,2,2],[0,1,2,3]]), np.array([12.0, 16.0], dtype=float).reshape((2,)))),
        ('Negative values', lambda f: assert_close(f([[-2,1],[3,-4]],[[0,0,2,2]]), np.array([-2.0], dtype=float).reshape((1,)))),
        ('Boundary row', lambda f: assert_close(f([[1,2],[3,4]],[[1,0,2,2]]), np.array([7.0], dtype=float).reshape((1,)))),
        ('Repeated query', lambda f: assert_close(f([[7]],[[0,0,1,1],[0,0,1,1]]), np.array([7.0, 7.0], dtype=float).reshape((2,)))),
        ('Reject reversed bounds', lambda f: rejects(f,[[1,2]],[[0,1,1,0]])),
        ('Reject outside bounds', lambda f: rejects(f,[[1]],[[0,0,2,1]])),
        ('Reject fractional index', lambda f: rejects(f,[[1]],[[0,0,1,.5]])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[1,2],[3,4]],[[0,0,2,2],[1,1,2,2]]), np.array([10.0, 4.0], dtype=float).reshape((2,)))),
    ]
    return run_cases(namespace, 'rectangle_sums', cases, mode)
