def run_tests(namespace, mode="all"):
    cases = [
        ('Several constraints', lambda f: assert_close(f([{'a':1,'b':2},{'a':1,'b':3}], {'a':1,'b':3}), 1)),
        ('Missing is not None', lambda f: assert_close(f([{}, {'a':None}], {'a':None}), 1)),
        ('First duplicate wins', lambda f: assert_close(f([{'x':2},{'x':2}], {'x':2}), 0)),
        ('No records', lambda f: assert_close(f([], {}), -1)),
        ('Empty query', lambda f: assert_close(f([{'x':1}], {}), 0)),
        ('No match', lambda f: assert_close(f([{'x':1}], {'x':2}), -1)),
        ('Reject nonrecord row', lambda f: rejects(f, [1], {})),
        ('Reject nonmapping query', lambda f: rejects(f, [], [])),
        ('Reject invalid key', lambda f: rejects(f, [], {'':1})),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'a':1,'b':2},{'a':1,'b':3}], {'a':1,'b':3}), 1))
    ]
    return run_cases(namespace, 'first_match', cases, mode)
