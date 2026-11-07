def run_tests(namespace, mode="all"):
    cases = [
        ('Rename one key', lambda f: assert_close(f({'old':1,'x':2}, {'old':'new'}), {'new':1,'x':2})),
        ('Swap keys simultaneously', lambda f: assert_close(f({'a':1,'b':2}, {'a':'b','b':'a'}), {'b':1,'a':2})),
        ('Absent mapping ignored', lambda f: assert_close(f({'a':1}, {'z':'a'}), {'a':1})),
        ('Empty record', lambda f: assert_close(f({}, {'x':'y'}), {})),
        ('Identity mapping', lambda f: assert_close(f({'a':None}, {'a':'a'}), {'a':None})),
        ('No mappings', lambda f: assert_close(f({'x':[1]}, {}), {'x':[1]})),
        ('Reject collision', lambda f: rejects(f, {'a':1,'b':2}, {'a':'b'})),
        ('Reject empty target', lambda f: rejects(f, {'a':1}, {'a':''})),
        ('Reject numeric destination', lambda f: rejects(f, {}, {'x':2})),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, {'old':1,'x':2}, {'old':'new'}), {'new':1,'x':2}))
    ]
    return run_cases(namespace, 'rename_fields', cases, mode)
