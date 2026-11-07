def run_tests(namespace, mode="all"):
    cases = [
        ('Shared target', lambda f: assert_close(f({'a':'x','b':'y','c':'x'}), {'x':['a','c'],'y':['b']})),
        ('One mapping', lambda f: assert_close(f({'a':'z'}), {'z':['a']})),
        ('Empty lookup', lambda f: assert_close(f({}), {})),
        ('Identity mapping', lambda f: assert_close(f({'a':'a','b':'b'}), {'a':['a'],'b':['b']})),
        ('Insertion order', lambda f: assert_close(f({'z':'x','a':'x'}), {'x':['z','a']})),
        ('Case-sensitive targets', lambda f: assert_close(f({'a':'X','b':'x'}), {'X':['a'],'x':['b']})),
        ('Reject numeric target', lambda f: rejects(f, {'a':1})),
        ('Reject empty target', lambda f: rejects(f, {'a':''})),
        ('Reject nonmapping', lambda f: rejects(f, [])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, {'a':'x','b':'y','c':'x'}), {'x':['a','c'],'y':['b']}))
    ]
    return run_cases(namespace, 'invert_lookup', cases, mode)
