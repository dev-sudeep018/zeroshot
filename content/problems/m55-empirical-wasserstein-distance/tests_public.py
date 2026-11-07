def run_tests(namespace, mode="all"):
    cases = [
        ('Translation cost', lambda f: assert_close(f([0,1],[2,3]), 2)),
        ('Unequal sample sizes', lambda f: assert_close(f([0],[0,2]), 1)),
        ('Same empirical distribution', lambda f: assert_close(f([1,1,3,3],[1,3]), 0)),
        ('Two point masses', lambda f: assert_close(f([-2],[5]), 7)),
        ('Interleaved support', lambda f: assert_close(f([0,4],[1,3]), 1)),
        ('Unequal masses across a gap', lambda f: assert_close(f([0,0,3],[0,3,3]), 1)),
        ('Reject empty sample', lambda f: rejects(f,[],[0])),
        ('Reject matrix', lambda f: rejects(f,[[0]],[1])),
        ('Reject nonfinite input', lambda f: rejects(f,[0],[np.inf])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([0.,4]),np.array([1.,3])),1)),
    ]
    return run_cases(namespace, 'empirical_wasserstein', cases, mode)
