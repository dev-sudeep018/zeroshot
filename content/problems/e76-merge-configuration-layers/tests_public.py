def run_tests(namespace, mode="all"):
    cases = [
        ('Override and deletion', lambda f: assert_close(f([{'a':1,'b':2},{'a':3,'b':None}]), {'a':3})),
        ('Nested replacement', lambda f: assert_close(f([{'x':{'a':1,'b':2}},{'x':{'a':9}}]), {'x':{'a':9}})),
        ('Delete absent key', lambda f: assert_close(f([{'x':None}]), {})),
        ('No layers', lambda f: assert_close(f([]), {})),
        ('Falsy settings', lambda f: assert_close(f([{'x':1},{'x':False,'y':0}]), {'x':False,'y':0})),
        ('Reintroduce deleted key', lambda f: assert_close(f([{'a':1},{'a':None},{'a':2}]), {'a':2})),
        ('Reject nonmapping layer', lambda f: rejects(f, [1])),
        ('Reject invalid key', lambda f: rejects(f, [{'':1}])),
        ('Reject unsupported value', lambda f: rejects(f, [{'x':{1,2}}])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'a':1,'b':2},{'a':3,'b':None}]), {'a':3}))
    ]
    return run_cases(namespace, 'merge_config', cases, mode)
