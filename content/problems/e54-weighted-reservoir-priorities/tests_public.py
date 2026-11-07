def run_tests(namespace, mode="all"):
    cases = [
        ('Weight changes priority', lambda f: assert_close(f([1,2], [np.exp(-2),np.exp(-2)], 1), dict(indices=np.array([1]),keys=np.array([-2.,-1.])))),
        ('Exact key tie', lambda f: assert_close(f([1,1], [.5,.5], 2), dict(indices=np.array([0,1]),keys=np.array([np.log(.5),np.log(.5)])))),
        ('Zero selected items', lambda f: assert_close(f([1,2], [1,1], 0), dict(indices=np.array([],dtype=int),keys=np.zeros(2)))),
        ('Draw one gives highest key', lambda f: assert_close(f([1,1], [.5,1], 1), dict(indices=np.array([1]),keys=np.array([np.log(.5),0.])))),
        ('Selection order follows priorities', lambda f: assert_close(f([1,1,1], [np.exp(-3),np.exp(-1),np.exp(-2)], 3), dict(indices=np.array([1,2,0]),keys=np.array([-3.,-1.,-2.])))),
        ('One item', lambda f: assert_close(f([2], [np.exp(-2)], 1), dict(indices=np.array([0]),keys=np.array([-1.])))),
        ('Reject zero weight', lambda f: rejects(f, [0], [.5], 1)),
        ('Reject zero uniform', lambda f: rejects(f, [1], [0], 1)),
        ('Reject too many selections', lambda f: rejects(f, [1], [.5], 2)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1,2], [np.exp(-2),np.exp(-2)], 1), dict(indices=np.array([1]),keys=np.array([-2.,-1.]))))
    ]
    return run_cases(namespace, 'weighted_sample_keys', cases, mode)
