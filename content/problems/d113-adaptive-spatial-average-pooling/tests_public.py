def run_tests(namespace, mode="all"):
    cases = [
        ('Uneven bins', lambda f: assert_close(f(np.arange(15).reshape(3,5),[2,2]), np.array([[3.5, 5.5], [8.5, 10.5]], dtype='float64'))),
        ('Global mean', lambda f: assert_close(f([[1,2],[3,4]],[1,1]), np.array([[2.5]], dtype='float64'))),
        ('Disjoint blocks', lambda f: assert_close(f(np.arange(16).reshape(4,4),[2,2]), np.array([[2.5, 4.5], [10.5, 12.5]], dtype='float64'))),
        ('Output larger than input', lambda f: assert_close(f([[1,3]],[1,3]), np.array([[1.0, 2.0, 3.0]], dtype='float64'))),
        ('Constant image', lambda f: assert_close(f(np.full((2,3),4),[3,4]), np.array([[4.0, 4.0, 4.0, 4.0], [4.0, 4.0, 4.0, 4.0], [4.0, 4.0, 4.0, 4.0]], dtype='float64'))),
        ('Identity pooling', lambda f: assert_close(f([[1,2],[3,4]],[2,2]), np.array([[1.0, 2.0], [3.0, 4.0]], dtype='float64'))),
        ('Reject zero output', lambda f: rejects(f, [[1]],[0,1])),
        ('Reject wrong output rank', lambda f: rejects(f, [[1]],[[1,1]])),
        ('Reject nonfinite image', lambda f: rejects(f, [[np.inf]],[1,1])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, np.arange(15).reshape(3,5),[2,2]), np.array([[3.5, 5.5], [8.5, 10.5]], dtype='float64'))),
    ]
    return run_cases(namespace, 'adaptive_average_pool', cases, mode)
