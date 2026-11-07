def run_tests(namespace, mode="all"):
    cases = [
        ('Mixed byte widths', lambda f: assert_close(f('aé🙂'), [0,1,3,7])),
        ('Combining mark', lambda f: assert_close(f('e\u0301'), [0,1,3])),
        ('ASCII text', lambda f: assert_close(f('abc'), [0,1,2,3])),
        ('Empty text', lambda f: assert_close(f(''), [0])),
        ('Three-byte character', lambda f: assert_close(f('漢'), [0,3])),
        ('Null byte character', lambda f: assert_close(f('a\x00b'), [0,1,2,3])),
        ('Reject surrogate', lambda f: rejects(f, '\ud800')),
        ('Reject nonstring', lambda f: rejects(f, b"abc")),
        ('Reject oversized', lambda f: rejects(f, 'x'*10001)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, 'aé🙂'), [0,1,3,7]))
    ]
    return run_cases(namespace, 'utf8_offsets', cases, mode)
