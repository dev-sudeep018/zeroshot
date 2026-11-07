def run_tests(namespace, mode="all"):
    cases = [
        ('Two winning locations', lambda f: assert_close(f([[3,5]],[[1,6]],[2,4]), np.array([[0.0, 3.0, 0.0, 0.0], [0.0, 0.0, 5.0, 0.0]], dtype='float64'))),
        ('First and last positions', lambda f: assert_close(f([[2,4]],[[0,3]],[2,2]), np.array([[2.0, 0.0], [0.0, 4.0]], dtype='float64'))),
        ('Single maximum', lambda f: assert_close(f([[7]],[[4]],[3,3]), np.array([[0.0, 0.0, 0.0], [0.0, 7.0, 0.0], [0.0, 0.0, 0.0]], dtype='float64'))),
        ('Negative retained value', lambda f: assert_close(f([[-2]],[[1]],[1,3]), np.array([[0.0, -2.0, 0.0]], dtype='float64'))),
        ('Full scatter permutation', lambda f: assert_close(f([[1,2],[3,4]],[[3,1],[0,2]],[2,2]), np.array([[3.0, 2.0], [4.0, 1.0]], dtype='float64'))),
        ('Retained zero', lambda f: assert_close(f([[0]],[[0]],[1,1]), np.array([[0.0]], dtype='float64'))),
        ('Reject duplicate switch', lambda f: rejects(f, [[1,2]],[[0,0]],[1,2])),
        ('Reject switch outside map', lambda f: rejects(f, [[1]],[[4]],[2,2])),
        ('Reject shape mismatch', lambda f: rejects(f, [[1,2]],[[0]],[1,2])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[3,5]],[[1,6]],[2,4]), np.array([[0.0, 3.0, 0.0, 0.0], [0.0, 0.0, 5.0, 0.0]], dtype='float64'))),
    ]
    return run_cases(namespace, 'max_unpool', cases, mode)
