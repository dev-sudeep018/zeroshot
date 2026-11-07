def run_tests(namespace, mode="all"):
    cases = [
        ('Inclusive repeated values', lambda f: assert_close(f([1,2,2,4],[0,1,2,3,4]), np.array([0,.25,.75,.75,1]))),
        ('Unsorted sample', lambda f: assert_close(f([4,1,3,2],[2,0,4]), np.array([.5,0,1]))),
        ('Single observation', lambda f: assert_close(f([5],[4,5,6]), np.array([0.,1,1]))),
        ('All equal', lambda f: assert_close(f([2,2,2],[1,2,3]), np.array([0.,1,1]))),
        ('Negative thresholds', lambda f: assert_close(f([-3,-1,2],[-2,0]), np.array([1/3,2/3]))),
        ('Repeated queries', lambda f: assert_close(f([0,1],[0,0,1]), np.array([.5,.5,1]))),
        ('Reject empty sample', lambda f: rejects(f,[],[1])),
        ('Reject matrix query', lambda f: rejects(f,[1],[[1]])),
        ('Reject nonfinite sample', lambda f: rejects(f,[np.inf],[1])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([4.,1,2,2]),np.array([2.,1])),np.array([.75,.25]))),
    ]
    return run_cases(namespace, 'empirical_cdf', cases, mode)
