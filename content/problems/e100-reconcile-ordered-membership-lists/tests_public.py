def run_tests(namespace, mode="all"):
    cases = [
        ('Denial takes precedence', lambda f: assert_close(f(['a','b','c'], ['a','b'], ['b']), dict(accepted=['a'],rejected=['b','c']))),
        ('Duplicate candidates', lambda f: assert_close(f(['a','a'], ['a'], []), dict(accepted=['a','a'],rejected=[]))),
        ('Empty allow list', lambda f: assert_close(f(['a'], [], []), dict(accepted=[],rejected=['a']))),
        ('No candidates', lambda f: assert_close(f([], ['a'], []), dict(accepted=[],rejected=[]))),
        ('Unknown denied ID', lambda f: assert_close(f(['a'], ['a'], ['z']), dict(accepted=['a'],rejected=[]))),
        ('Both sets contain ID', lambda f: assert_close(f(['x'], ['x'], ['x']), dict(accepted=[],rejected=['x']))),
        ('Reject empty candidate', lambda f: rejects(f, [''], [], [])),
        ('Reject invalid allowed', lambda f: rejects(f, [], [1], [])),
        ('Reject raw denied', lambda f: rejects(f, [], [], 'x')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['a','b','c'], ['a','b'], ['b']), dict(accepted=['a'],rejected=['b','c'])))
    ]
    return run_cases(namespace, 'reconcile_membership', cases, mode)
