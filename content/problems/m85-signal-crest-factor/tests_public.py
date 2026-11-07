def run_tests(namespace, mode="all"):
    cases = [
        ('One pulse', lambda f: assert_close(f([0,0,3,0]), {'rms':1.5,'peak':3.0,'crest':2.0})),
        ('Constant magnitude', lambda f: assert_close(f([-2,2,-2,2]), {'rms':2.0,'peak':2.0,'crest':1.0})),
        ('All zero', lambda f: assert_close(f([0,0]), {'rms':0.0,'peak':0.0,'crest':0.0})),
        ('Single negative', lambda f: assert_close(f([-4]), {'rms':4.0,'peak':4.0,'crest':1.0})),
        ('Mixed signal', lambda f: assert_close(f([1,-2,3]), {'rms':2.160246899469287,'peak':3.0,'crest':1.3887301496588271})),
        ('Small signal', lambda f: assert_close(f([.1,-.2,0]), {'rms':0.12909944487358058,'peak':0.2,'crest':1.5491933384829666})),
        ('Reject empty', lambda f: rejects(f,[])),
        ('Reject nonfinite', lambda f: rejects(f,[np.inf])),
        ('Reject boolean', lambda f: rejects(f,[True])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,0,3,0]), {'rms':1.5,'peak':3.0,'crest':2.0})),
    ]
    return run_cases(namespace, 'crest_summary', cases, mode)
