def run_tests(namespace, mode="all"):
    cases = [
        ('Unequal measurements', lambda f: assert_close(f([1,2,3]), {'mean':2.0,'std':0.816496580927726,'cv':0.408248290463863})),
        ('Constant sample', lambda f: assert_close(f([5,5,5]), {'mean':5.0,'std':0.0,'cv':0.0})),
        ('Single observation', lambda f: assert_close(f([2]), {'mean':2.0,'std':0.0,'cv':0.0})),
        ('Scaled sample', lambda f: assert_close(f([10,20,30]), {'mean':20.0,'std':8.16496580927726,'cv':0.408248290463863})),
        ('Small positives', lambda f: assert_close(f([.01,.02,.04]), {'mean':0.023333333333333334,'std':0.012472191289246471,'cv':0.5345224838248487})),
        ('Uneven spread', lambda f: assert_close(f([1,1,8,10]), {'mean':5.0,'std':4.06201920231798,'cv':0.812403840463596})),
        ('Reject zero mean inputs', lambda f: rejects(f,[0,0])),
        ('Reject negative values', lambda f: rejects(f,[-1,2])),
        ('Reject too small', lambda f: rejects(f,[1e-8])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,2,3]), {'mean':2.0,'std':0.816496580927726,'cv':0.408248290463863})),
    ]
    return run_cases(namespace, 'relative_dispersion', cases, mode)
