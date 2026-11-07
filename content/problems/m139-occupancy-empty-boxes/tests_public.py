def run_tests(namespace, mode="all"):
    cases = [
        ('Two balls two boxes', lambda f: assert_close(f(2,2), {'mean':0.5,'variance':0.25})),
        ('No placements', lambda f: assert_close(f(5,0), {'mean':5.0,'variance':0.0})),
        ('One box', lambda f: assert_close(f(1,4), {'mean':0.0,'variance':0.0})),
        ('One placement', lambda f: assert_close(f(4,1), {'mean':3.0,'variance':0.0})),
        ('Three boxes', lambda f: assert_close(f(3,4), {'mean':0.5925925925925929,'variance':0.3155006858710562})),
        ('Sparse placements', lambda f: assert_close(f(10,3), {'mean':7.290000000000001,'variance':0.22589999999999577})),
        ('Reject zero boxes', lambda f: rejects(f,0,2)),
        ('Reject negative placements', lambda f: rejects(f,3,-1)),
        ('Reject fractional boxes', lambda f: rejects(f,2.5,3)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,2,2), {'mean':0.5,'variance':0.25})),
    ]
    return run_cases(namespace, 'empty_box_moments', cases, mode)
