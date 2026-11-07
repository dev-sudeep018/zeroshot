def run_tests(namespace, mode="all"):
    cases = [
        ('Last position order', lambda f: assert_close(f([{'id':'a','v':1},{'id':'b','v':2},{'id':'a','v':3}], 'id'), [{'id':'b','v':2},{'id':'a','v':3}])),
        ('One ID repeats', lambda f: assert_close(f([{'id':'a','v':1},{'id':'a','v':2}], 'id'), [{'id':'a','v':2}])),
        ('Already unique', lambda f: assert_close(f([{'id':'b'},{'id':'a'}], 'id'), [{'id':'b'},{'id':'a'}])),
        ('Empty records', lambda f: assert_close(f([], 'id'), [])),
        ('Custom field', lambda f: assert_close(f([{'k':'x'},{'k':'x','n':0}], 'k'), [{'k':'x','n':0}])),
        ('Case distinction', lambda f: assert_close(f([{'id':'A'},{'id':'a'}], 'id'), [{'id':'A'},{'id':'a'}])),
        ('Reject missing ID', lambda f: rejects(f, [{}], 'id')),
        ('Reject empty ID', lambda f: rejects(f, [{'id':''}], 'id')),
        ('Reject invalid field', lambda f: rejects(f, [], 2)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'id':'a','v':1},{'id':'b','v':2},{'id':'a','v':3}], 'id'), [{'id':'b','v':2},{'id':'a','v':3}]))
    ]
    return run_cases(namespace, 'keep_last_records', cases, mode)
