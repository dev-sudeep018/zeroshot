def run_tests(namespace, mode="all"):
    cases = [
        ('Prerequisite before task', lambda f: assert_close(f({'train':['load'],'load':[]}), ['load','train'])),
        ('Reconsider earliest ready', lambda f: assert_close(f({'a':['b'],'b':[],'c':[]}), ['b','a','c'])),
        ('Diamond graph', lambda f: assert_close(f({'d':['b','c'],'b':['a'],'c':['a'],'a':[]}), ['a','b','c','d'])),
        ('Empty graph', lambda f: assert_close(f({}), [])),
        ('Independent input order', lambda f: assert_close(f({'z':[],'a':[]}), ['z','a'])),
        ('Shared prerequisite', lambda f: assert_close(f({'x':['z'],'y':['z'],'z':[]}), ['z','x','y'])),
        ('Reject cycle', lambda f: rejects(f, {'a':['b'],'b':['a']})),
        ('Reject unknown dependency', lambda f: rejects(f, {'a':['missing']})),
        ('Reject duplicate prerequisite', lambda f: rejects(f, {'a':[],'b':['a','a']})),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, {'train':['load'],'load':[]}), ['load','train']))
    ]
    return run_cases(namespace, 'dependency_order', cases, mode)
