def run_tests(namespace, mode="all"):
    cases = [
        ('Partial right edge', lambda f: assert_close(f([[1,2,3],[4,5,6]],2,2), np.array([[12.0, 9.0]], dtype=float).reshape((1, 2)))),
        ('Partial bottom edge', lambda f: assert_close(f([[1,2],[3,4],[5,6]],2,1), np.array([[4.0, 6.0], [5.0, 6.0]], dtype=float).reshape((2, 2)))),
        ('Whole grid', lambda f: assert_close(f([[1,2],[3,4]],8,8), np.array([[10.0]], dtype=float).reshape((1, 1)))),
        ('Unit blocks', lambda f: assert_close(f([[1,-2],[0,4]],1,1), np.array([[1.0, -2.0], [0.0, 4.0]], dtype=float).reshape((2, 2)))),
        ('Cancellation', lambda f: assert_close(f([[1,-1],[2,-2]],2,2), np.array([[0.0]], dtype=float).reshape((1, 1)))),
        ('Rectangular blocks', lambda f: assert_close(f([[1,2,3,4],[5,6,7,8]],1,3), np.array([[6.0, 4.0], [18.0, 8.0]], dtype=float).reshape((2, 2)))),
        ('Reject zero block', lambda f: rejects(f,[[1]],0,1)),
        ('Reject noninteger block', lambda f: rejects(f,[[1]],1.5,1)),
        ('Reject vector grid', lambda f: rejects(f,[1,2],1,1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[1,2,3],[4,5,6]],2,2), np.array([[12.0, 9.0]], dtype=float).reshape((1, 2)))),
    ]
    return run_cases(namespace, 'grid_block_sums', cases, mode)
