def run_tests(namespace, mode="all"):
    cases = [
        ('Monotone nonlinear relation', lambda f: assert_close(f([1,2,3],[1,4,9]), 1)),
        ('Reversed order', lambda f: assert_close(f([1,2,3],[9,4,1]), -1)),
        ('Average tied ranks', lambda f: assert_close(f([1,1,3],[1,2,3]), np.sqrt(3)/2)),
        ('Matching ties', lambda f: assert_close(f([1,1,3,4],[5,5,8,9]), 1)),
        ('Crossing orders', lambda f: assert_close(f([1,2,3],[2,3,1]), -.5)),
        ('Ties on both sides', lambda f: assert_close(f([1,1,2,2],[1,2,1,2]), 0)),
        ('Reject constant ranks', lambda f: rejects(f,[2,2,2],[1,2,3])),
        ('Reject one pair', lambda f: rejects(f,[1],[2])),
        ('Reject length mismatch', lambda f: rejects(f,[1,2],[3,4,5])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([1.,1,3]),np.array([1.,2,3])),np.sqrt(3)/2)),
    ]
    return run_cases(namespace, 'spearman_correlation', cases, mode)
