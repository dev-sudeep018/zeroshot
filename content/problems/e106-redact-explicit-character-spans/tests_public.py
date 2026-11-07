def run_tests(namespace, mode="all"):
    cases = [
        ('One span', lambda f: assert_close(f('name: Ada', [[6,9]], '*'), 'name: ***')),
        ('Overlap union', lambda f: assert_close(f('abcdef', [[1,4],[3,5]], '#'), 'a####f')),
        ('Unicode positions', lambda f: assert_close(f('a🙂b', [[1,2]], '*'), 'a*b')),
        ('No spans', lambda f: assert_close(f('abc', [], '*'), 'abc')),
        ('Zero-width span', lambda f: assert_close(f('abc', [[1,1]], '*'), 'abc')),
        ('Whole empty text', lambda f: assert_close(f('', [[0,0]], '*'), '')),
        ('Reject reversed span', lambda f: rejects(f, 'abc', [[2,1]], '*')),
        ('Reject outside span', lambda f: rejects(f, 'abc', [[0,4]], '*')),
        ('Reject multi-character marker', lambda f: rejects(f, 'abc', [], '**')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, 'name: Ada', [[6,9]], '*'), 'name: ***'))
    ]
    return run_cases(namespace, 'redact_spans', cases, mode)
