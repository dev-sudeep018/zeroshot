def run_tests(namespace, mode="all"):
    cases = [
        ('Four channels to square', lambda f: assert_close(f(np.arange(4).reshape(4,1,1),2), np.array([[[0.0, 1.0], [2.0, 3.0]]], dtype='float64'))),
        ('Two output channels', lambda f: assert_close(f(np.arange(8).reshape(8,1,1),2), np.array([[[0.0, 1.0], [2.0, 3.0]], [[4.0, 5.0], [6.0, 7.0]]], dtype='float64'))),
        ('Spatial ordering', lambda f: assert_close(f(np.arange(16).reshape(4,2,2),2), np.array([[[0.0, 4.0, 1.0, 5.0], [8.0, 12.0, 9.0, 13.0], [2.0, 6.0, 3.0, 7.0], [10.0, 14.0, 11.0, 15.0]]], dtype='float64'))),
        ('Identity factor', lambda f: assert_close(f(np.arange(6).reshape(1,2,3),1), np.array([[[0.0, 1.0, 2.0], [3.0, 4.0, 5.0]]], dtype='float64'))),
        ('Threefold shuffle', lambda f: assert_close(f(np.arange(9).reshape(9,1,1),3), np.array([[[0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0]]], dtype='float64'))),
        ('Rectangular spatial grid', lambda f: assert_close(f(np.arange(12).reshape(4,1,3),2), np.array([[[0.0, 3.0, 1.0, 4.0, 2.0, 5.0], [6.0, 9.0, 7.0, 10.0, 8.0, 11.0]]], dtype='float64'))),
        ('Reject incomplete channels', lambda f: rejects(f, np.ones((3,1,1)),2)),
        ('Reject zero factor', lambda f: rejects(f, np.ones((1,1,1)),0)),
        ('Reject missing channel axis', lambda f: rejects(f, [[1]],1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, np.arange(4).reshape(4,1,1),2), np.array([[[0.0, 1.0], [2.0, 3.0]]], dtype='float64'))),
    ]
    return run_cases(namespace, 'pixel_shuffle', cases, mode)
