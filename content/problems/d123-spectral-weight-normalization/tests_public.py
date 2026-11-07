def run_tests(namespace, mode="all"):
    cases = [
        ('Diagonal gains', lambda f: assert_close(f([[3,0],[0,4]],1), {'weights':np.array([[0.75, 0.0], [0.0, 1.0]], dtype='float64'),'original_norm':4.0,'scale':0.25})),
        ('Rectangular row', lambda f: assert_close(f([[3,4]],2), {'weights':np.array([[1.2000000000000002, 1.6]], dtype='float64'),'original_norm':5.0,'scale':0.4})),
        ('Already unit gain', lambda f: assert_close(f(np.eye(2),1), {'weights':np.array([[1.0, 0.0], [0.0, 1.0]], dtype='float64'),'original_norm':1.0,'scale':1.0})),
        ('Increase a small map', lambda f: assert_close(f([[0.25]],1), {'weights':np.array([[1.0]], dtype='float64'),'original_norm':0.25,'scale':4.0})),
        ('Negative scalar', lambda f: assert_close(f([[-3]],2), {'weights':np.array([[-2.0]], dtype='float64'),'original_norm':3.0,'scale':0.6666666666666666})),
        ('Rank one matrix', lambda f: assert_close(f([[1,2],[2,4]],0.5), {'weights':np.array([[0.1, 0.2], [0.2, 0.4]], dtype='float64'),'original_norm':5.0,'scale':0.1})),
        ('Reject zero weights', lambda f: rejects(f, np.zeros((2,2)),1)),
        ('Reject zero bound', lambda f: rejects(f, [[1]],0)),
        ('Reject vector weights', lambda f: rejects(f, [1,2],1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[3,0],[0,4]],1), {'weights':np.array([[0.75, 0.0], [0.0, 1.0]], dtype='float64'),'original_norm':4.0,'scale':0.25})),
    ]
    return run_cases(namespace, 'spectral_normalize', cases, mode)
