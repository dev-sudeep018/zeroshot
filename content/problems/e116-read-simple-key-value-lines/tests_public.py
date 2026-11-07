def run_tests(namespace, mode="all"):
    cases = [
        ('Trim fields', lambda f: assert_close(f(' x = 1\ny= two '), {'x':'1','y':'two'})),
        ('First separator only', lambda f: assert_close(f('token=a=b=c'), {'token':'a=b=c'})),
        ('Empty value', lambda f: assert_close(f('x='), {'x':''})),
        ('Blank lines ignored', lambda f: assert_close(f('\n x=1\n\n'), {'x':'1'})),
        ('Empty text', lambda f: assert_close(f(''), {})),
        ('Case-sensitive keys', lambda f: assert_close(f('A=1\na=2'), {'A':'1','a':'2'})),
        ('Reject missing equals', lambda f: rejects(f, 'abc')),
        ('Reject duplicate key', lambda f: rejects(f, 'x=1\nx=2')),
        ('Reject empty key', lambda f: rejects(f, '=1')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ' x = 1\ny= two '), {'x':'1','y':'two'}))
    ]
    return run_cases(namespace, 'parse_settings', cases, mode)
