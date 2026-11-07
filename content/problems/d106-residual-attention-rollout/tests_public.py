def run_tests(namespace, mode="all"):
    cases = [
        ('Identity stack', lambda f: assert_close(f(np.array([np.eye(2),np.eye(2)]),1), np.array([[[1.0, 0.0], [0.0, 1.0]], [[1.0, 0.0], [0.0, 1.0]]], dtype='float64'))),
        ('Single swap with residual', lambda f: assert_close(f([[[0,1],[1,0]]],1), np.array([[[0.5, 0.5], [0.5, 0.5]]], dtype='float64'))),
        ('Two swaps', lambda f: assert_close(f([[[0,1],[1,0]],[[0,1],[1,0]]],0), np.array([[[0.0, 1.0], [1.0, 0.0]], [[1.0, 0.0], [0.0, 1.0]]], dtype='float64'))),
        ('Noncommuting layers', lambda f: assert_close(f([[[1,0],[1,0]],[[0,1],[1,0]]],0), np.array([[[1.0, 0.0], [1.0, 0.0]], [[1.0, 0.0], [1.0, 0.0]]], dtype='float64'))),
        ('Uniform mixing', lambda f: assert_close(f(np.full((2,2,2),0.5),0.5), np.array([[[0.6666666666666666, 0.3333333333333333], [0.3333333333333333, 0.6666666666666666]], [[0.5555555555555555, 0.4444444444444444], [0.4444444444444444, 0.5555555555555555]]], dtype='float64'))),
        ('Single token', lambda f: assert_close(f(np.ones((3,1,1)),1), np.array([[[1.0]], [[1.0]], [[1.0]]], dtype='float64'))),
        ('Reject rectangular attention', lambda f: rejects(f, [[[0.2,0.3,0.5],[0.5,0.3,0.2]]],0)),
        ('Reject invalid row sum', lambda f: rejects(f, [[[0.1,0.1],[0.5,0.5]]],0)),
        ('Reject negative residual', lambda f: rejects(f, [[[1]]],-0.1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, np.array([np.eye(2),np.eye(2)]),1), np.array([[[1.0, 0.0], [0.0, 1.0]], [[1.0, 0.0], [0.0, 1.0]]], dtype='float64'))),
    ]
    return run_cases(namespace, 'attention_rollout', cases, mode)
