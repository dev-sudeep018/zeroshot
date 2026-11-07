def run_tests(namespace, mode="all"):
    cases = [
        ('Named values', lambda f: assert_close(f(['true','false']), [True,False])),
        ('Trim and case', lambda f: assert_close(f([' YES ','No']), [True,False])),
        ('Numeric strings', lambda f: assert_close(f(['1','0']), [True,False])),
        ('Empty list', lambda f: assert_close(f([]), [])),
        ('Repeated false', lambda f: assert_close(f(['no','FALSE','0']), [False,False,False])),
        ('Mixed aliases', lambda f: assert_close(f(['yes','true','1']), [True,True,True])),
        ('Reject ambiguous token', lambda f: rejects(f, ['on'])),
        ('Reject empty token', lambda f: rejects(f, [''])),
        ('Reject boolean instead of string', lambda f: rejects(f, [True])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['true','false']), [True,False]))
    ]
    return run_cases(namespace, 'parse_boolean_settings', cases, mode)
