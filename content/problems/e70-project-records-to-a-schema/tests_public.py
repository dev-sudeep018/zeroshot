def run_tests(namespace, mode="all"):
    cases = [
        ('Drop extras and fill gaps', lambda f: assert_close(f([{'a':1,'c':9},{'b':2}], ['a','b']), [{'a':1,'b':None},{'a':None,'b':2}])),
        ('Empty schema', lambda f: assert_close(f([{'a':1}], []), [{}])),
        ('Preserve zero', lambda f: assert_close(f([{'a':0}], ['a']), [{'a':0}])),
        ('No rows', lambda f: assert_close(f([], ['x']), [])),
        ('Present None', lambda f: assert_close(f([{'x':None}], ['x']), [{'x':None}])),
        ('Nested values', lambda f: assert_close(f([{'x':[1]}], ['x']), [{'x':[1]}])),
        ('Reject duplicate field', lambda f: rejects(f, [], ['x','x'])),
        ('Reject nonstring field', lambda f: rejects(f, [], [1])),
        ('Reject invalid record', lambda f: rejects(f, [[]], ['x'])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'a':1,'c':9},{'b':2}], ['a','b']), [{'a':1,'b':None},{'a':None,'b':2}]))
    ]
    return run_cases(namespace, 'project_records', cases, mode)
