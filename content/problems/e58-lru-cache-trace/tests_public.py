def run_tests(namespace, mode="all"):
    cases = [
        ('Hit refreshes recency', lambda f: assert_close(f(['a','b','a','c'], 2), dict(hits=np.array([False,False,True,False]),keys=['c','a'],evicted=['b']))),
        ('Capacity zero', lambda f: assert_close(f(['a','a'], 0), dict(hits=np.array([False,False]),keys=[],evicted=[]))),
        ('Repeated hit', lambda f: assert_close(f(['a','a','a'], 1), dict(hits=np.array([False,True,True]),keys=['a'],evicted=[]))),
        ('Repeated evictions', lambda f: assert_close(f(['a','b','c'], 1), dict(hits=np.array([False,False,False]),keys=['c'],evicted=['a','b']))),
        ('Empty requests', lambda f: assert_close(f([], 2), dict(hits=np.array([],dtype=bool),keys=[],evicted=[]))),
        ('Cache larger than stream', lambda f: assert_close(f(['a','b'], 5), dict(hits=np.array([False,False]),keys=['b','a'],evicted=[]))),
        ('Reject negative capacity', lambda f: rejects(f, ['a'], -1)),
        ('Reject raw request string', lambda f: rejects(f, 'aba', 2)),
        ('Reject empty key', lambda f: rejects(f, [''], 2)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, ['a','b','a','c'], 2), dict(hits=np.array([False,False,True,False]),keys=['c','a'],evicted=['b'])))
    ]
    return run_cases(namespace, 'lru_trace', cases, mode)
