def run_tests(namespace, mode="all"):
    cases = [
        ('Fill missing only', lambda f: assert_close(f({'a':1}, {'a':9,'b':2}), {'a':1,'b':2})),
        ('Explicit None', lambda f: assert_close(f({'x':None}, {'x':3}), {'x':None})),
        ('All falsy values', lambda f: assert_close(f({'a':False,'b':0,'c':''}, {'a':1,'b':2,'c':'x'}), {'a':False,'b':0,'c':''})),
        ('No defaults', lambda f: assert_close(f({'x':1}, {}), {'x':1})),
        ('Empty config', lambda f: assert_close(f({}, {'x':[1]}), {'x':[1]})),
        ('No recursive fill', lambda f: assert_close(f({'x':{}}, {'x':{'a':1}}), {'x':{}})),
        ('Reject invalid config', lambda f: rejects(f, [], {})),
        ('Reject invalid default key', lambda f: rejects(f, {}, {'':2})),
        ('Reject nonfinite value', lambda f: rejects(f, {'x':float('inf')}, {})),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, {'a':1}, {'a':9,'b':2}), {'a':1,'b':2}))
    ]
    return run_cases(namespace, 'apply_defaults', cases, mode)
