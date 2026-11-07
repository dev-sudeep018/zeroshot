def run_tests(namespace, mode="all"):
    cases = [
        ('Boundary embargo', lambda f: assert_close(f([0,1,2,3,4], 2, 1), dict(train=np.array([0]),test=np.array([3,4]),gap=np.array([1,2])))),
        ('Zero embargo', lambda f: assert_close(f([1,2,3], 2), dict(train=np.array([0]),test=np.array([1,2]),gap=np.array([],dtype=int)))),
        ('Unsorted timestamps', lambda f: assert_close(f([4,0,2], 2, 1), dict(train=np.array([1]),test=np.array([0]),gap=np.array([2])))),
        ('Empty input', lambda f: assert_close(f([], 0), dict(train=np.array([],dtype=int),test=np.array([],dtype=int),gap=np.array([],dtype=int)))),
        ('Entirely in gap', lambda f: assert_close(f([1,2], 2, 3), dict(train=np.array([],dtype=int),test=np.array([],dtype=int),gap=np.array([0,1])))),
        ('Repeated cutoff values', lambda f: assert_close(f([2,2], 2), dict(train=np.array([],dtype=int),test=np.array([0,1]),gap=np.array([],dtype=int)))),
        ('Reject negative embargo', lambda f: rejects(f, [1], 2, -1)),
        ('Reject matrix of times', lambda f: rejects(f, [[1]], 2)),
        ('Reject nonfinite cutoff', lambda f: rejects(f, [1], np.inf)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [0,1,2,3,4], 2, 1), dict(train=np.array([0]),test=np.array([3,4]),gap=np.array([1,2]))))
    ]
    return run_cases(namespace, 'temporal_split', cases, mode)
