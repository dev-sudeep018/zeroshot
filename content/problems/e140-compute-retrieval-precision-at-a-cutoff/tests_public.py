def run_tests(namespace, mode="all"):
    cases = [
        ('Duplicates consume rank', lambda f: assert_close(f(['a','a','b'], ['a','b'], 2), dict(hits=1,precision=.5))),
        ('Short ranking denominator', lambda f: assert_close(f(['a'], ['a'], 4), dict(hits=1,precision=.25))),
        ('Irrelevant result', lambda f: assert_close(f(['x','a'], ['a'], 2), dict(hits=1,precision=.5))),
        ('Empty ranking', lambda f: assert_close(f([], ['a'], 2), dict(hits=0,precision=0.0))),
        ('No relevant IDs', lambda f: assert_close(f(['a'], [], 1), dict(hits=0,precision=0.0))),
        ('Cutoff excludes hit', lambda f: assert_close(f(['x','a'], ['a'], 1), dict(hits=0,precision=0.0))),
        ('Reject zero cutoff', lambda f: rejects(f, [], [], 0)),
        ('Reject duplicate relevance', lambda f: rejects(f, [], ['a','a'], 1)),
        ('Reject empty rank ID', lambda f: rejects(f, [''], [], 1)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['a','a','b'], ['a','b'], 2), dict(hits=1,precision=.5)))
    ]
    return run_cases(namespace, 'retrieval_precision', cases, mode)
