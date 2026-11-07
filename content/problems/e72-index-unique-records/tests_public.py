def run_tests(namespace, mode="all"):
    cases = [
        ('Index two records', lambda f: assert_close(f([{'id':'a','v':1},{'id':'b','v':2}], 'id'), {'a':{'id':'a','v':1},'b':{'id':'b','v':2}})),
        ('Custom ID field', lambda f: assert_close(f([{'key':'z'}], 'key'), {'z':{'key':'z'}})),
        ('Empty records', lambda f: assert_close(f([], 'id'), {})),
        ('Case-sensitive IDs', lambda f: assert_close(f([{'id':'A'},{'id':'a'}], 'id'), {'A':{'id':'A'},'a':{'id':'a'}})),
        ('Nested payload', lambda f: assert_close(f([{'id':'x','v':[1]}], 'id'), {'x':{'id':'x','v':[1]}})),
        ('Whitespace ID retained', lambda f: assert_close(f([{'id':' a '}], 'id'), {' a ':{'id':' a '}})),
        ('Reject duplicate ID', lambda f: rejects(f, [{'id':'a'},{'id':'a'}], 'id')),
        ('Reject missing ID', lambda f: rejects(f, [{}], 'id')),
        ('Reject numeric ID', lambda f: rejects(f, [{'id':1}], 'id')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'id':'a','v':1},{'id':'b','v':2}], 'id'), {'a':{'id':'a','v':1},'b':{'id':'b','v':2}}))
    ]
    return run_cases(namespace, 'index_records', cases, mode)
