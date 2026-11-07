def run_tests(namespace, mode="all"):
    cases = [
        ('Overlapping patches', lambda f: assert_close(f(np.arange(9).reshape(3,3),[2,2],[1,1]), {'patches':np.array([[0.0, 1.0, 3.0, 4.0], [1.0, 2.0, 4.0, 5.0], [3.0, 4.0, 6.0, 7.0], [4.0, 5.0, 7.0, 8.0]], dtype='float64'),'positions':np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype='int64')})),
        ('Full image patch', lambda f: assert_close(f([[1,2],[3,4]],[2,2],[1,1]), {'patches':np.array([[1.0, 2.0, 3.0, 4.0]], dtype='float64'),'positions':np.array([[0, 0]], dtype='int64')})),
        ('Pointwise patches', lambda f: assert_close(f([[1,2],[3,4]],[1,1],[1,1]), {'patches':np.array([[1.0], [2.0], [3.0], [4.0]], dtype='float64'),'positions':np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype='int64')})),
        ('Strided columns', lambda f: assert_close(f(np.arange(12).reshape(3,4),[2,2],[1,2]), {'patches':np.array([[0.0, 1.0, 4.0, 5.0], [2.0, 3.0, 6.0, 7.0], [4.0, 5.0, 8.0, 9.0], [6.0, 7.0, 10.0, 11.0]], dtype='float64'),'positions':np.array([[0, 0], [0, 2], [1, 0], [1, 2]], dtype='int64')})),
        ('Rectangular kernel', lambda f: assert_close(f(np.arange(12).reshape(3,4),[1,3],[2,1]), {'patches':np.array([[0.0, 1.0, 2.0], [1.0, 2.0, 3.0], [8.0, 9.0, 10.0], [9.0, 10.0, 11.0]], dtype='float64'),'positions':np.array([[0, 0], [0, 1], [2, 0], [2, 1]], dtype='int64')})),
        ('Stride exceeds spare space', lambda f: assert_close(f(np.arange(9).reshape(3,3),[2,2],[4,4]), {'patches':np.array([[0.0, 1.0, 3.0, 4.0]], dtype='float64'),'positions':np.array([[0, 0]], dtype='int64')})),
        ('Reject oversized kernel', lambda f: rejects(f, [[1,2]],[2,2],[1,1])),
        ('Reject zero stride', lambda f: rejects(f, [[1]],[1,1],[0,1])),
        ('Reject invalid kernel rank', lambda f: rejects(f, [[1]],[1],[1,1])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, np.arange(9).reshape(3,3),[2,2],[1,1]), {'patches':np.array([[0.0, 1.0, 3.0, 4.0], [1.0, 2.0, 4.0, 5.0], [3.0, 4.0, 6.0, 7.0], [4.0, 5.0, 7.0, 8.0]], dtype='float64'),'positions':np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype='int64')})),
    ]
    return run_cases(namespace, 'image_patch_matrix', cases, mode)
