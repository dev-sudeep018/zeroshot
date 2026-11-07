def run_tests(namespace, mode="all"):
    cases = [
        ('Zero hidden activation', lambda f: assert_close(f([[0]],[[[2]]],[[[3]]]),np.array([[0.]]))),
        ('One exact GELU branch', lambda f: assert_close(f([[1]],[[[1]]],[[[1]]]),np.array([[0.8413447460685429]]))),
        ('Opposite hidden branches', lambda f: assert_close(f([[1]],[[[1]],[[-1]]],[[[1]],[[-1]]]),np.array([[1.]]))),
        ('Sum instead of average', lambda f: assert_close(f([[1]],[[[1]],[[1]]],[[[1]],[[1]]]),np.array([[1.6826894921370859]]))),
        ('Output channels', lambda f: assert_close(f([[1]],[[[1]]],[[[1,2]]]),np.array([[.8413447460685429,1.6826894921370859]]))),
        ('Negative GELU retained', lambda f: assert_close(f([[-1]],[[[1]]],[[[1]]]),np.array([[-.15865525393145707]]))),
        ('Batch independence', lambda f: assert_close(f([[1],[0]],[[[1]]],[[[1]]]),np.array([[.8413447460685429],[0.]]))),
        ('Reject shard count mismatch', lambda f: rejects(f,[[1]],[[[1]],[[1]]],[[[1]]])),
        ('Reject hidden width mismatch', lambda f: rejects(f,[[1]],[[[1,2]]],[[[1]]])),
        ('Reject nonfinite weights', lambda f: rejects(f,[[1]],[[[np.inf]]],[[[1]]])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[0]],[[[2]]],[[[3]]]),np.array([[0.]]))),
    ]
    return run_cases(namespace, 'sharded_mlp', cases, mode)
