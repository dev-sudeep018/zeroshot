def run_tests(namespace, mode="all"):
    cases = [
        ('Quartiles of four values', lambda f: assert_close(f([0,10,20,30],[.25,.5,.75]), np.array([7.5,15,22.5]))),
        ('Unsorted observations', lambda f: assert_close(f([9,1,5],[0,.5,1]), np.array([1,5,9]))),
        ('Singleton sample', lambda f: assert_close(f([7],[0,.3,1]), np.array([7,7,7]))),
        ('Repeated values', lambda f: assert_close(f([2,2,2,8],[.5,.75]), np.array([2,3.5]))),
        ('Query order', lambda f: assert_close(f([0,10],[1,0,.2]), np.array([10,0,2]))),
        ('Negative observations', lambda f: assert_close(f([-4,-2,0],[.25,.75]), np.array([-3,-1]))),
        ('Reject out-of-range q', lambda f: rejects(f,[1,2],[-.1])),
        ('Reject empty observations', lambda f: rejects(f,[],[.5])),
        ('Reject matrix', lambda f: rejects(f,[[1,2]],[.5])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([3.,1.,2.]),np.array([.5])),np.array([2.]))),
    ]
    return run_cases(namespace, 'empirical_quantiles', cases, mode)
