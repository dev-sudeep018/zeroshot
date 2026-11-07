def run_tests(namespace, mode="all"):
    cases = [
        ('Propagate changed source', lambda f: assert_close(f({'a':[],'b':['a'],'c':['b']},{'a':'1','b':'1','c':'1'},{'a':'2','b':'1','c':'1'}), ['a','b','c'])),
        ('Only changed leaf', lambda f: assert_close(f({'a':[],'b':['a']},{'a':'1','b':'1'},{'a':'1','b':'2'}), ['b'])),
        ('No changes', lambda f: assert_close(f({'a':[]},{'a':'1'},{'a':'1'}), [])),
        ('Empty graph', lambda f: assert_close(f({},{},{}), [])),
        ('Independent task unaffected', lambda f: assert_close(f({'b':['a'],'a':[],'c':[]},{'a':'1','b':'1','c':'1'},{'a':'2','b':'1','c':'1'}), ['a','b'])),
        ('Stable ready ties', lambda f: assert_close(f({'a':[],'b':[]},{'a':'1','b':'1'},{'a':'2','b':'2'}), ['a','b'])),
        ('Reject cycle', lambda f: rejects(f, {'a':['a']},{'a':'1'},{'a':'2'})),
        ('Reject missing fingerprint', lambda f: rejects(f, {'a':[]},{},{'a':'1'})),
        ('Reject unknown dependency', lambda f: rejects(f, {'a':['x']},{'a':'1'},{'a':'2'})),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, {'a':[],'b':['a'],'c':['b']},{'a':'1','b':'1','c':'1'},{'a':'2','b':'1','c':'1'}), ['a','b','c']))
    ]
    return run_cases(namespace, 'incremental_rebuild', cases, mode)
