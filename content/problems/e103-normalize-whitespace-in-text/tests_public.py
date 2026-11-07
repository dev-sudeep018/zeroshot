def run_tests(namespace, mode="all"):
    cases = [
        ('Mixed whitespace', lambda f: assert_close(f('  North\tstar\n data  '), 'North star data')),
        ('Unicode space', lambda f: assert_close(f('A\u2003B\u00a0C'), 'A B C')),
        ('Punctuation survives', lambda f: assert_close(f(' Hello,   WORLD! '), 'Hello, WORLD!')),
        ('Empty text', lambda f: assert_close(f(''), '')),
        ('Only whitespace', lambda f: assert_close(f(' \t\n'), '')),
        ('No changes', lambda f: assert_close(f('x-y_z'), 'x-y_z')),
        ('Reject nonstring', lambda f: rejects(f, None)),
        ('Reject oversized', lambda f: rejects(f, 'x'*10001)),
        ('Reject surrogate', lambda f: rejects(f, '\ud800')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, '  North\tstar\n data  '), 'North star data'))
    ]
    return run_cases(namespace, 'normalize_whitespace', cases, mode)
