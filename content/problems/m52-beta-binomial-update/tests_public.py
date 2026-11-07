def run_tests(namespace, mode="all"):
    cases = [
        ('Uniform prior and one success', lambda f: assert_close(f(1,1,1,0), {"alpha":2,"beta":1,"mean":2/3,"variance":1/18})),
        ('No observations', lambda f: assert_close(f(1,1,0,0), {"alpha":1,"beta":1,"mean":.5,"variance":1/12})),
        ('Balanced evidence', lambda f: assert_close(f(1,1,4,4), {"alpha":5,"beta":5,"mean":.5,"variance":1/44})),
        ('Asymmetric prior', lambda f: assert_close(f(2,3,0,0), {"alpha":2,"beta":3,"mean":.4,"variance":.04})),
        ('One failure', lambda f: assert_close(f(1,1,0,1), {"alpha":1,"beta":2,"mean":1/3,"variance":1/18})),
        ('Fractional prior counts', lambda f: assert_close(f(.5,.5,1,1), {"alpha":1.5,"beta":1.5,"mean":.5,"variance":1/16})),
        ('Reject zero prior parameter', lambda f: rejects(f,0,1,1,1)),
        ('Reject negative count', lambda f: rejects(f,1,1,-1,0)),
        ('Reject fractional count', lambda f: rejects(f,1,1,.5,0)),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,2,3,1,2),{"alpha":3,"beta":5,"mean":3/8,"variance":5/192})),
    ]
    return run_cases(namespace, 'beta_update', cases, mode)
