def run_tests(namespace, mode="all"):
    cases = [
        ('Repeated category', lambda f: assert_close(f([{'g':'a','v':1},{'g':'b'},{'g':'a','v':2}], 'g', '?'), {'a':[{'g':'a','v':1},{'g':'a','v':2}],'b':[{'g':'b'}]})),
        ('Missing bucket', lambda f: assert_close(f([{}], 'g', '?'), {'?':[{}]})),
        ('Empty records', lambda f: assert_close(f([], 'g', '?'), {})),
        ('Explicit missing label', lambda f: assert_close(f([{}, {'g':'?'}], 'g', '?'), {'?':[{}, {'g':'?'}]})),
        ('Case separate', lambda f: assert_close(f([{'g':'A'},{'g':'a'}], 'g', '?'), {'A':[{'g':'A'}],'a':[{'g':'a'}]})),
        ('Custom field', lambda f: assert_close(f([{'kind':'x'}], 'kind', 'unknown'), {'x':[{'kind':'x'}]})),
        ('Reject None group', lambda f: rejects(f, [{'g':None}], 'g', '?')),
        ('Reject empty missing label', lambda f: rejects(f, [], 'g', '')),
        ('Reject invalid row', lambda f: rejects(f, [1], 'g', '?')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'g':'a','v':1},{'g':'b'},{'g':'a','v':2}], 'g', '?'), {'a':[{'g':'a','v':1},{'g':'a','v':2}],'b':[{'g':'b'}]}))
    ]
    return run_cases(namespace, 'group_records', cases, mode)
