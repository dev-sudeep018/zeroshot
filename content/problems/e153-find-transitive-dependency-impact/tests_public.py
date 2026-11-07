def run_tests(namespace, mode="all"):
    cases = [
        ('Transitive chain', lambda f: assert_close(f({'a':[],'b':['a'],'c':['b']},['a']), ['b','c'])),
        ('Exclude all seeds', lambda f: assert_close(f({'a':[],'b':['a'],'c':['b']},['a','b']), ['c'])),
        ('Cycle terminates', lambda f: assert_close(f({'a':['b'],'b':['a'],'c':['b']},['a']), ['b','c'])),
        ('No changes', lambda f: assert_close(f({'a':[]},[]), [])),
        ('Only seed affected', lambda f: assert_close(f({'a':[],'b':[]},['a']), [])),
        ('Output graph order', lambda f: assert_close(f({'c':['b'],'b':['a'],'a':[]},['a']), ['c','b'])),
        ('Reject unknown seed', lambda f: rejects(f, {'a':[]},['x'])),
        ('Reject unknown prerequisite', lambda f: rejects(f, {'a':['x']},[])),
        ('Reject duplicate seeds', lambda f: rejects(f, {'a':[]},['a','a'])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, {'a':[],'b':['a'],'c':['b']},['a']), ['b','c']))
    ]
    return run_cases(namespace, 'downstream_impact', cases, mode)
