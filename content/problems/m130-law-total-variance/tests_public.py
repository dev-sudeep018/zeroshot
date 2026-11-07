def run_tests(namespace, mode="all"):
    cases = [
        ('Two subpopulations', lambda f: assert_close(f([.5,.5],[0,4],[1,1]), {'mean':2.0,'within':1.0,'between':4.0,'variance':5.0})),
        ('Only between variance', lambda f: assert_close(f([.25,.75],[0,8],[0,0]), {'mean':6.0,'within':0.0,'between':12.0,'variance':12.0})),
        ('Identical means', lambda f: assert_close(f([.2,.8],[3,3],[2,7]), {'mean':3.0,'within':6.0,'between':0.0,'variance':6.0})),
        ('Single group', lambda f: assert_close(f([1],[5],[2]), {'mean':5.0,'within':2.0,'between':0.0,'variance':2.0})),
        ('Zero weight group', lambda f: assert_close(f([0,1],[99,2],[7,3]), {'mean':2.0,'within':3.0,'between':0.0,'variance':3.0})),
        ('Unequal groups', lambda f: assert_close(f([.1,.3,.6],[-2,1,5],[2,0,4]), {'mean':3.0999999999999996,'within':2.6,'between':6.09,'variance':8.69})),
        ('Reject negative variance', lambda f: rejects(f,[1],[0],[-1])),
        ('Reject mismatch', lambda f: rejects(f,[.5,.5],[1],[1,1])),
        ('Reject invalid weights', lambda f: rejects(f,[1,1],[0,1],[0,0])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[.5,.5],[0,4],[1,1]), {'mean':2.0,'within':1.0,'between':4.0,'variance':5.0})),
    ]
    return run_cases(namespace, 'mixture_variance', cases, mode)
