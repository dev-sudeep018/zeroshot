def run_tests(namespace, mode="all"):
    cases = [
        ('Unequal prior', lambda f: assert_close(f([.2,.8],[.8,.1]), {"posterior":np.array([2/3,1/3]),"evidence":.24})),
        ('Uninformative event', lambda f: assert_close(f([.1,.9],[.4,.4]), {"posterior":np.array([.1,.9]),"evidence":.4})),
        ('Impossible hypothesis', lambda f: assert_close(f([0,1],[1,.2]), {"posterior":np.array([0,1]),"evidence":.2})),
        ('Three hypotheses', lambda f: assert_close(f([.2,.3,.5],[.5,0,.2]), {"posterior":np.array([.5,0,.5]),"evidence":.2})),
        ('Certain event', lambda f: assert_close(f([.3,.7],[1,1]), {"posterior":np.array([.3,.7]),"evidence":1})),
        ('One hypothesis', lambda f: assert_close(f([1],[.3]), {"posterior":np.array([1.]),"evidence":.3})),
        ('Reject zero evidence', lambda f: rejects(f,[.5,.5],[0,0])),
        ('Reject unnormalized prior', lambda f: rejects(f,[1,1],[.5,.5])),
        ('Reject shape mismatch', lambda f: rejects(f,[.5,.5],[.2])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([.2,.8]),np.array([.8,.1])),{"posterior":np.array([2/3,1/3]),"evidence":.24})),
    ]
    return run_cases(namespace, 'bayes_update', cases, mode)
