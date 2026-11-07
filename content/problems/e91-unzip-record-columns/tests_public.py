def run_tests(namespace, mode="all"):
    cases = [
        ('Aligned columns', lambda f: assert_close(f([{'a':1,'b':2},{'a':3,'b':4}], ['b','a']), {'b':[2,4],'a':[1,3]})),
        ('Ignore extra fields', lambda f: assert_close(f([{'x':1,'y':9}], ['x']), {'x':[1]})),
        ('Empty rows', lambda f: assert_close(f([], ['x','y']), {'x':[],'y':[]})),
        ('Empty schema', lambda f: assert_close(f([{'x':1}], []), {})),
        ('Present None', lambda f: assert_close(f([{'x':None}], ['x']), {'x':[None]})),
        ('Nested payload', lambda f: assert_close(f([{'x':[1]}], ['x']), {'x':[[1]]})),
        ('Reject missing selected field', lambda f: rejects(f, [{}], ['x'])),
        ('Reject duplicate fields', lambda f: rejects(f, [], ['x','x'])),
        ('Reject nonrecord input', lambda f: rejects(f, [1], ['x'])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'a':1,'b':2},{'a':3,'b':4}], ['b','a']), {'b':[2,4],'a':[1,3]}))
    ]
    return run_cases(namespace, 'record_columns', cases, mode)
