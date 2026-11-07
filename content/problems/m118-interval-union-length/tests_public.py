def run_tests(namespace, mode="all"):
    cases = [
        ('Overlapping intervals', lambda f: assert_close(f([[1,4],[2,6],[8,9]]), {'intervals':np.array([[1.0, 6.0], [8.0, 9.0]], dtype=float).reshape((2, 2)),'length':6.0})),
        ('Touching intervals', lambda f: assert_close(f([[0,2],[2,3],[3,5]]), {'intervals':np.array([[0.0, 5.0]], dtype=float).reshape((1, 2)),'length':5.0})),
        ('Unsorted contained', lambda f: assert_close(f([[4,5],[0,10],[2,3]]), {'intervals':np.array([[0.0, 10.0]], dtype=float).reshape((1, 2)),'length':10.0})),
        ('Point intervals', lambda f: assert_close(f([[1,1],[2,2],[1,1]]), {'intervals':np.array([[1.0, 1.0], [2.0, 2.0]], dtype=float).reshape((2, 2)),'length':0.0})),
        ('Negative ranges', lambda f: assert_close(f([[-5,-2],[-3,1],[4,6]]), {'intervals':np.array([[-5.0, 1.0], [4.0, 6.0]], dtype=float).reshape((2, 2)),'length':8.0})),
        ('Separated intervals', lambda f: assert_close(f([[0,1],[3,4]]), {'intervals':np.array([[0.0, 1.0], [3.0, 4.0]], dtype=float).reshape((2, 2)),'length':2.0})),
        ('Reject reversed', lambda f: rejects(f,[[2,1]])),
        ('Reject wrong columns', lambda f: rejects(f,[[1,2,3]])),
        ('Reject empty', lambda f: rejects(f,[])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[1,4],[2,6],[8,9]]), {'intervals':np.array([[1.0, 6.0], [8.0, 9.0]], dtype=float).reshape((2, 2)),'length':6.0})),
    ]
    return run_cases(namespace, 'interval_union', cases, mode)
