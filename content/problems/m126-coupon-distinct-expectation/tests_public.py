def run_tests(namespace, mode="all"):
    cases = [
        ('Two fair categories', lambda f: assert_close(f([.5,.5],2), {'seen':np.array([0.75, 0.75], dtype=float).reshape((2,)),'expected':1.5})),
        ('No draws', lambda f: assert_close(f([.2,.8],0), {'seen':np.array([0.0, 0.0], dtype=float).reshape((2,)),'expected':0.0})),
        ('One draw', lambda f: assert_close(f([.1,.2,.7],1), {'seen':np.array([0.1, 0.19999999999999998, 0.7], dtype=float).reshape((3,)),'expected':1.0})),
        ('Impossible category', lambda f: assert_close(f([0,1],9), {'seen':np.array([0.0, 1.0], dtype=float).reshape((2,)),'expected':1.0})),
        ('Unequal categories', lambda f: assert_close(f([.1,.9],3), {'seen':np.array([0.27099999999999996, 0.999], dtype=float).reshape((2,)),'expected':1.27})),
        ('Many draws', lambda f: assert_close(f([.25,.25,.5],10000), {'seen':np.array([1.0, 1.0, 1.0], dtype=float).reshape((3,)),'expected':3.0})),
        ('Reject negative draws', lambda f: rejects(f,[1],-1)),
        ('Reject fractional draws', lambda f: rejects(f,[1],1.5)),
        ('Reject invalid masses', lambda f: rejects(f,[.5,-.5,1],2)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[.5,.5],2), {'seen':np.array([0.75, 0.75], dtype=float).reshape((2,)),'expected':1.5})),
    ]
    return run_cases(namespace, 'expected_distinct', cases, mode)
