def run_tests(namespace, mode="all"):
    cases = [
        ('Words and punctuation', lambda f: assert_close(f(' Model: V2! '), 'model-v2')),
        ('Repeated separators', lambda f: assert_close(f('a___b---c'), 'a-b-c')),
        ('Already normalized', lambda f: assert_close(f('ml-data'), 'ml-data')),
        ('Digits allowed', lambda f: assert_close(f(' 2026 '), '2026')),
        ('Mixed case', lambda f: assert_close(f('HTTPServer'), 'httpserver')),
        ('ASCII controls separate', lambda f: assert_close(f('a\tb\nc'), 'a-b-c')),
        ('Reject empty input', lambda f: rejects(f, '')),
        ('Reject no alphanumeric', lambda f: rejects(f, '--- !')),
        ('Reject non-ASCII', lambda f: rejects(f, 'café')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ' Model: V2! '), 'model-v2'))
    ]
    return run_cases(namespace, 'ascii_slug', cases, mode)
