def run_tests(namespace, mode="all"):
    cases = [
        ('Double both axes', lambda f: assert_close(f([[1,2],[3,4]],[4,4]), np.array([[1, 1, 2, 2], [1, 1, 2, 2], [3, 3, 4, 4], [3, 3, 4, 4]], dtype='int64'))),
        ('Downsample', lambda f: assert_close(f(np.arange(16).reshape(4,4),[2,2]), np.array([[0, 2], [8, 10]], dtype='int64'))),
        ('Uneven resize', lambda f: assert_close(f([[1,2,3],[4,5,6]],[3,2]), np.array([[1, 2], [1, 2], [4, 5]], dtype='int64'))),
        ('Single output pixel', lambda f: assert_close(f([[7,8],[9,10]],[1,1]), np.array([[7]], dtype='int64'))),
        ('One source pixel', lambda f: assert_close(f([[5]],[2,3]), np.array([[5, 5, 5], [5, 5, 5]], dtype='int64'))),
        ('Identity resize', lambda f: assert_close(f([[0,2,1]],[1,3]), np.array([[0, 2, 1]], dtype='int64'))),
        ('Reject fractional class', lambda f: rejects(f, [[1.5]],[1,1])),
        ('Reject zero output axis', lambda f: rejects(f, [[1]],[0,1])),
        ('Reject size has wrong length', lambda f: rejects(f, [[1]],[1])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[1,2],[3,4]],[4,4]), np.array([[1, 1, 2, 2], [1, 1, 2, 2], [3, 3, 4, 4], [3, 3, 4, 4]], dtype='int64'))),
    ]
    return run_cases(namespace, 'resize_segmentation', cases, mode)
