def run_tests(namespace, mode="all"):
    cases = [
        ('Positive line', lambda f: assert_close(f([1,2,3],[5,7,9]), 1)),
        ('Negative line', lambda f: assert_close(f([1,2,3],[9,7,5]), -1)),
        ('Zero linear association', lambda f: assert_close(f([-1,0,1],[1,-2,1]), 0)),
        ('Translation invariance', lambda f: assert_close(f([101,102,103],[5,7,9]), 1)),
        ('Two distinct pairs', lambda f: assert_close(f([4,8],[3,1]), -1)),
        ('Non-perfect association', lambda f: assert_close(f([0,1,2],[0,1,1]), np.sqrt(3)/2)),
        ('Reject constant vector', lambda f: rejects(f,[1,1],[2,3])),
        ('Reject unequal lengths', lambda f: rejects(f,[1,2],[1,2,3])),
        ('Reject single pair', lambda f: rejects(f,[1],[2])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([1.,2,3]),np.array([5.,7,9])),1)),
    ]
    return run_cases(namespace, 'pearson_correlation', cases, mode)
