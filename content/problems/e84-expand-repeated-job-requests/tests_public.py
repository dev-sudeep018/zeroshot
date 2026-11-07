def run_tests(namespace, mode="all"):
    cases = [
        ('Mixed quantities', lambda f: assert_close(f([['a',2],['b',1]]), ['a','a','b'])),
        ('Zero skipped', lambda f: assert_close(f([['a',0],['b',2]]), ['b','b'])),
        ('Repeated request IDs', lambda f: assert_close(f([['x',1],['x',2]]), ['x','x','x'])),
        ('No requests', lambda f: assert_close(f([]), [])),
        ('Single request', lambda f: assert_close(f([['a',1]]), ['a'])),
        ('All zero', lambda f: assert_close(f([['x',0],['y',0]]), [])),
        ('Reject negative count', lambda f: rejects(f, [['x',-1]])),
        ('Reject excess total', lambda f: rejects(f, [['a',600],['b',600]])),
        ('Reject malformed request', lambda f: rejects(f, [['x']])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [['a',2],['b',1]]), ['a','a','b']))
    ]
    return run_cases(namespace, 'expand_jobs', cases, mode)
