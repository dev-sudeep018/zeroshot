def run_tests(namespace, mode="all"):
    cases = [
        ('Asymmetric errors change threshold', lambda f: assert_close(f([.1,.3,.9], 1, 3), dict(predictions=np.array([0,1,1]),expected_cost=np.array([.3,.7,.1])))),
        ('Tie chooses positive', lambda f: assert_close(f([.5], 1, 1), dict(predictions=np.array([1]),expected_cost=np.array([.5])))),
        ('False positives are free', lambda f: assert_close(f([0,.5,1], 0, 1), dict(predictions=np.array([1,1,1]),expected_cost=np.zeros(3)))),
        ('False negatives are free', lambda f: assert_close(f([0,.5,1], 1, 0), dict(predictions=np.array([0,0,1]),expected_cost=np.zeros(3)))),
        ('Certain predictions', lambda f: assert_close(f([0,1], 4, 2), dict(predictions=np.array([0,1]),expected_cost=np.zeros(2)))),
        ('Empty batch', lambda f: assert_close(f([], 1, 1), dict(predictions=np.array([],dtype=int),expected_cost=np.array([])))),
        ('Reject out-of-range probability', lambda f: rejects(f, [1.1], 1, 1)),
        ('Reject negative cost', lambda f: rejects(f, [.5], -1, 1)),
        ('Reject zero costs', lambda f: rejects(f, [.5], 0, 0)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [.1,.3,.9], 1, 3), dict(predictions=np.array([0,1,1]),expected_cost=np.array([.3,.7,.1]))))
    ]
    return run_cases(namespace, 'cost_sensitive_predict', cases, mode)
