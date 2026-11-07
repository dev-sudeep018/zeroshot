def run_tests(namespace, mode="all"):
    cases = [
        ('Two binary measurements', lambda f: assert_close(f([.5,.5],0,[.5,.5],0), {'start':0,'probabilities':np.array([0.25, 0.5, 0.25], dtype=float).reshape((3,))})),
        ('Shifted support', lambda f: assert_close(f([.2,.8],-2,[.1,.3,.6],4), {'start':2,'probabilities':np.array([0.020000000000000004, 0.14, 0.36, 0.48], dtype=float).reshape((4,))})),
        ('Deterministic shift', lambda f: assert_close(f([1],7,[.2,.8],-1), {'start':6,'probabilities':np.array([0.2, 0.8], dtype=float).reshape((2,))})),
        ('Internal zero bins', lambda f: assert_close(f([.5,0,.5],0,[0,1],0), {'start':0,'probabilities':np.array([0.0, 0.5, 0.0, 0.5], dtype=float).reshape((4,))})),
        ('Two constants', lambda f: assert_close(f([1],-4,[1],2), {'start':-2,'probabilities':np.array([1.0], dtype=float).reshape((1,))})),
        ('Unequal lengths', lambda f: assert_close(f([.1,.2,.7],0,[.25,.75],0), {'start':0,'probabilities':np.array([0.025, 0.125, 0.325, 0.5249999999999999], dtype=float).reshape((4,))})),
        ('Reject invalid probabilities', lambda f: rejects(f,[.2],0,[1],0)),
        ('Reject noninteger offset', lambda f: rejects(f,[1],.5,[1],0)),
        ('Reject negative mass', lambda f: rejects(f,[-1,2],0,[1],0)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[.5,.5],0,[.5,.5],0), {'start':0,'probabilities':np.array([0.25, 0.5, 0.25], dtype=float).reshape((3,))})),
    ]
    return run_cases(namespace, 'independent_sum', cases, mode)
