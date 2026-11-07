def run_tests(namespace, mode="all"):
    cases = [
        ('Sorted keys repeated values', lambda f: assert_close(f({'z':['2','1'],'a':['x']}), 'a=x&z=2&z=1')),
        ('Space and plus', lambda f: assert_close(f({'q':['a b+c']}), 'q=a+b%2Bc')),
        ('Unicode', lambda f: assert_close(f({'name':['café']}), 'name=caf%C3%A9')),
        ('Empty mapping', lambda f: assert_close(f({}), '')),
        ('Omit empty value list', lambda f: assert_close(f({'x':[],'y':['']}), 'y=')),
        ('Escape separators', lambda f: assert_close(f({'a&b':['x=y']}), 'a%26b=x%3Dy')),
        ('Reject raw value list', lambda f: rejects(f, {'x':'a'})),
        ('Reject nontext value', lambda f: rejects(f, {'x':[1]})),
        ('Reject empty key', lambda f: rejects(f, {'':['a']})),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, {'z':['2','1'],'a':['x']}), 'a=x&z=2&z=1'))
    ]
    return run_cases(namespace, 'encode_query_values', cases, mode)
