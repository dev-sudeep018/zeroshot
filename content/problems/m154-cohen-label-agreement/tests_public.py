def run_tests(namespace, mode="all"):
    cases = [
        ('Partial agreement', lambda f: assert_close(f([0,0,1,1],[0,1,1,1],2), {'observed':0.75,'chance':0.5,'kappa':0.5})),
        ('Perfect agreement', lambda f: assert_close(f([0,1,2],[0,1,2],3), {'observed':1.0,'chance':0.3333333333333333,'kappa':1.0})),
        ('Complete reversal', lambda f: assert_close(f([0,0,1,1],[1,1,0,0],2), {'observed':0.0,'chance':0.5,'kappa':-1.0})),
        ('Constant shared label', lambda f: assert_close(f([1,1],[1,1],3), {'observed':1.0,'chance':1.0,'kappa':1.0})),
        ('Different constant labels', lambda f: assert_close(f([0,0],[1,1],2), {'observed':0.0,'chance':0.0,'kappa':0.0})),
        ('Unbalanced labels', lambda f: assert_close(f([0,0,0,1],[0,0,1,1],3), {'observed':0.75,'chance':0.5,'kappa':0.5})),
        ('Reject out of range label', lambda f: rejects(f,[0,2],[0,1],2)),
        ('Reject fractional label', lambda f: rejects(f,[0,.5],[0,1],2)),
        ('Reject length mismatch', lambda f: rejects(f,[0,1],[0],2)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,0,1,1],[0,1,1,1],2), {'observed':0.75,'chance':0.5,'kappa':0.5})),
    ]
    return run_cases(namespace, 'cohen_agreement', cases, mode)
