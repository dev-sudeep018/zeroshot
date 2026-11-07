def run_tests(namespace, mode="all"):
    cases = [
        ('Partial tail', lambda f: assert_close(f([1,2,3,4,5], 2), [[1,2],[3,4],[5]])),
        ('Exact multiple', lambda f: assert_close(f([1,2,3,4], 2), [[1,2],[3,4]])),
        ('Empty input', lambda f: assert_close(f([], 3), [])),
        ('Oversized batch', lambda f: assert_close(f([1,2], 9), [[1,2]])),
        ('Size one', lambda f: assert_close(f(['a','b'], 1), [['a'],['b']])),
        ('Record payloads', lambda f: assert_close(f([{'x':1},{'x':2}], 1), [[{'x':1}],[{'x':2}]])),
        ('Reject zero size', lambda f: rejects(f, [], 0)),
        ('Reject raw items', lambda f: rejects(f, 'abc', 2)),
        ('Reject boolean size', lambda f: rejects(f, [], True)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [1,2,3,4,5], 2), [[1,2],[3,4],[5]]))
    ]
    return run_cases(namespace, 'fixed_batches', cases, mode)
