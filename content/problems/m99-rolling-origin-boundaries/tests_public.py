def run_tests(namespace, mode="all"):
    cases = [
        ('Expanding origins', lambda f: assert_close(f(10,4,2,2), np.array([[0, 4, 4, 6], [0, 6, 6, 8], [0, 8, 8, 10]], dtype=float).reshape((3, 4)))),
        ('Overlapping windows', lambda f: assert_close(f(7,3,2,1), np.array([[0, 3, 3, 5], [0, 4, 4, 6], [0, 5, 5, 7]], dtype=float).reshape((3, 4)))),
        ('One full horizon', lambda f: assert_close(f(6,4,2,3), np.array([[0, 4, 4, 6]], dtype=float).reshape((1, 4)))),
        ('Skip incomplete tail', lambda f: assert_close(f(10,3,3,3), np.array([[0, 3, 3, 6], [0, 6, 6, 9]], dtype=float).reshape((2, 4)))),
        ('Unit horizon', lambda f: assert_close(f(5,2,1,1), np.array([[0, 2, 2, 3], [0, 3, 3, 4], [0, 4, 4, 5]], dtype=float).reshape((3, 4)))),
        ('Large stride', lambda f: assert_close(f(9,2,2,6), np.array([[0, 2, 2, 4]], dtype=float).reshape((1, 4)))),
        ('Reject no horizon', lambda f: rejects(f,5,4,2,1)),
        ('Reject zero stride', lambda f: rejects(f,5,2,1,0)),
        ('Reject noninteger length', lambda f: rejects(f,5.5,2,1,1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,10,4,2,2), np.array([[0, 4, 4, 6], [0, 6, 6, 8], [0, 8, 8, 10]], dtype=float).reshape((3, 4)))),
    ]
    return run_cases(namespace, 'rolling_origin_splits', cases, mode)
