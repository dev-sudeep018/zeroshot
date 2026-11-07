def run_tests(namespace, mode="all"):
    cases = [
        ('Mixed small population', lambda f: assert_close(f(5,2,2), {'support':[0,1,2],'probabilities':np.array([0.3, 0.6, 0.1], dtype=float).reshape((3,))})),
        ('Entire population', lambda f: assert_close(f(6,4,6), {'support':[4],'probabilities':np.array([1.0], dtype=float).reshape((1,))})),
        ('No draws', lambda f: assert_close(f(8,3,0), {'support':[0],'probabilities':np.array([1.0], dtype=float).reshape((1,))})),
        ('No successes present', lambda f: assert_close(f(7,0,3), {'support':[0],'probabilities':np.array([1.0], dtype=float).reshape((1,))})),
        ('All successes', lambda f: assert_close(f(7,7,3), {'support':[3],'probabilities':np.array([1.0], dtype=float).reshape((1,))})),
        ('Forced successes', lambda f: assert_close(f(8,6,5), {'support':[3,4,5],'probabilities':np.array([0.35714285714285715, 0.5357142857142857, 0.10714285714285714], dtype=float).reshape((3,))})),
        ('Reject excess draws', lambda f: rejects(f,4,2,5)),
        ('Reject negative successes', lambda f: rejects(f,4,-1,2)),
        ('Reject boolean population', lambda f: rejects(f,True,1,1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,5,2,2), {'support':[0,1,2],'probabilities':np.array([0.3, 0.6, 0.1], dtype=float).reshape((3,))})),
    ]
    return run_cases(namespace, 'hypergeometric_distribution', cases, mode)
