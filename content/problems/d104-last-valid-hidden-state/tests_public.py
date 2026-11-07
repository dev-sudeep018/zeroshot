def run_tests(namespace, mode="all"):
    cases = [
        ('Different lengths', lambda f: assert_close(f([[[1,2],[3,4]],[[5,6],[7,8]]],[1,2]), np.array([[1.0, 2.0], [7.0, 8.0]], dtype='float64'))),
        ('Empty sequence', lambda f: assert_close(f([[[9,8],[7,6]]],[0]), np.array([[0.0, 0.0]], dtype='float64'))),
        ('One timestep', lambda f: assert_close(f([[[2]],[[3]]],[1,0]), np.array([[2.0], [0.0]], dtype='float64'))),
        ('Full length', lambda f: assert_close(f([[[1],[2],[3]]],[3]), np.array([[3.0]], dtype='float64'))),
        ('Ignore padded states', lambda f: assert_close(f([[[4],[999],[888]]],[1]), np.array([[4.0]], dtype='float64'))),
        ('Mixed empty and full', lambda f: assert_close(f(np.arange(12).reshape(3,2,2),[0,2,1]), np.array([[0.0, 0.0], [6.0, 7.0], [8.0, 9.0]], dtype='float64'))),
        ('Reject length beyond time', lambda f: rejects(f, [[[1]]],[2])),
        ('Reject negative length', lambda f: rejects(f, [[[1]]],[-1])),
        ('Reject batch mismatch', lambda f: rejects(f, [[[1]],[[2]]],[1])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[[1,2],[3,4]],[[5,6],[7,8]]],[1,2]), np.array([[1.0, 2.0], [7.0, 8.0]], dtype='float64'))),
    ]
    return run_cases(namespace, 'last_valid_state', cases, mode)
