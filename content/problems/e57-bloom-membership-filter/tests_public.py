def run_tests(namespace, mode="all"):
    cases = [
        ('Known and absent item', lambda f: assert_close(f([[0,2]], [[0,2],[0,1]], 4), dict(bits=np.array([True,False,True,False]),maybe_present=np.array([True,False])))),
        ('A false positive from combined bits', lambda f: assert_close(f([[0,1],[2,3]], [[0,3]], 4), dict(bits=np.ones(4,dtype=bool),maybe_present=np.array([True])))),
        ('Empty filter', lambda f: assert_close(f(np.empty((0,2)), [[0,1]], 2), dict(bits=np.zeros(2,dtype=bool),maybe_present=np.array([False])))),
        ('Repeated hash index', lambda f: assert_close(f([[1,1]], [[1,1]], 2), dict(bits=np.array([False,True]),maybe_present=np.array([True])))),
        ('No queries', lambda f: assert_close(f([[0]], np.empty((0,1)), 1), dict(bits=np.array([True]),maybe_present=np.array([],dtype=bool)))),
        ('Repeated insertion is idempotent', lambda f: assert_close(f([[0],[0]], [[0]], 2), dict(bits=np.array([True,False]),maybe_present=np.array([True])))),
        ('Reject out-of-range bit', lambda f: rejects(f, [[2]], [[0]], 2)),
        ('Reject zero hashes per item', lambda f: rejects(f, np.empty((1,0)), np.empty((1,0)), 2)),
        ('Reject mismatched hash count', lambda f: rejects(f, [[0,1]], [[0]], 2)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[0,2]], [[0,2],[0,1]], 4), dict(bits=np.array([True,False,True,False]),maybe_present=np.array([True,False]))))
    ]
    return run_cases(namespace, 'bloom_filter', cases, mode)
