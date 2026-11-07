def run_tests(namespace, mode="all"):
    cases = [
        ('Repeated key', lambda f: assert_close(f('x=1&x=2&y='), {'x':['1','2'],'y':['']})),
        ('Space and plus', lambda f: assert_close(f('q=a+b%2Bc'), {'q':['a b+c']})),
        ('UTF-8 escape', lambda f: assert_close(f('name=caf%C3%A9'), {'name':['café']})),
        ('Empty query', lambda f: assert_close(f(''), {})),
        ('Absent equals', lambda f: assert_close(f('flag'), {'flag':['']})),
        ('First equals only', lambda f: assert_close(f('x=a=b&&'), {'x':['a=b']})),
        ('Reject bad percent escape', lambda f: rejects(f, 'x=%G0')),
        ('Reject invalid UTF-8', lambda f: rejects(f, 'x=%FF')),
        ('Reject blank key', lambda f: rejects(f, '=x')),
        ('Reject leading question', lambda f: rejects(f, '?x=1')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, 'x=1&x=2&y='), {'x':['1','2'],'y':['']}))
    ]
    return run_cases(namespace, 'parse_query_values', cases, mode)
