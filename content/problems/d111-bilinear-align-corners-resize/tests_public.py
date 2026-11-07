def run_tests(namespace, mode="all"):
    cases = [
        ('Center average', lambda f: assert_close(f([[0,2],[4,6]],[3,3]), np.array([[0.0, 1.0, 2.0], [2.0, 3.0, 4.0], [4.0, 5.0, 6.0]], dtype='float64'))),
        ('Single output coordinate', lambda f: assert_close(f([[1,2],[3,4]],[1,1]), np.array([[1.0]], dtype='float64'))),
        ('Single source row', lambda f: assert_close(f([[0,4]],[2,5]), np.array([[0.0, 1.0, 2.0, 3.0, 4.0], [0.0, 1.0, 2.0, 3.0, 4.0]], dtype='float64'))),
        ('Single source column', lambda f: assert_close(f([[0],[4]],[5,2]), np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 2.0], [3.0, 3.0], [4.0, 4.0]], dtype='float64'))),
        ('Constant image', lambda f: assert_close(f(np.full((2,3),7),[4,5]), np.array([[7.0, 7.0, 7.0, 7.0, 7.0], [7.0, 7.0, 7.0, 7.0, 7.0], [7.0, 7.0, 7.0, 7.0, 7.0], [7.0, 7.0, 7.0, 7.0, 7.0]], dtype='float64'))),
        ('Identity shape', lambda f: assert_close(f([[1,4,2],[3,0,5]],[2,3]), np.array([[1.0, 4.0, 2.0], [3.0, 0.0, 5.0]], dtype='float64'))),
        ('Reject zero axis', lambda f: rejects(f, [[1]],[0,2])),
        ('Reject fractional size', lambda f: rejects(f, [[1]],[2.5,2])),
        ('Reject nonfinite image', lambda f: rejects(f, [[np.nan]],[2,2])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[0,2],[4,6]],[3,3]), np.array([[0.0, 1.0, 2.0], [2.0, 3.0, 4.0], [4.0, 5.0, 6.0]], dtype='float64'))),
    ]
    return run_cases(namespace, 'bilinear_resize', cases, mode)
