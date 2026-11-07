def run_tests(namespace, mode="all"):
    cases = [
        ('Set then delete', lambda f: assert_close(f({'a':1}, [['set','b',2],['delete','a']]), {'b':2})),
        ('Set None stores None', lambda f: assert_close(f({}, [['set','a',None]]), {'a':None})),
        ('Repeated assignment', lambda f: assert_close(f({}, [['set','x',1],['set','x',2]]), {'x':2})),
        ('No operations', lambda f: assert_close(f({'x':1}, []), {'x':1})),
        ('Delete then recreate', lambda f: assert_close(f({'x':1}, [['delete','x'],['set','x',3]]), {'x':3})),
        ('Nested set', lambda f: assert_close(f({}, [['set','x',{'a':1}]]), {'x':{'a':1}})),
        ('Reject delete missing', lambda f: rejects(f, {}, [['delete','x']])),
        ('Reject unknown operation', lambda f: rejects(f, {}, [['add','x',1]])),
        ('Reject malformed set', lambda f: rejects(f, {}, [['set','x']])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, {'a':1}, [['set','b',2],['delete','a']]), {'b':2}))
    ]
    return run_cases(namespace, 'patch_record', cases, mode)
