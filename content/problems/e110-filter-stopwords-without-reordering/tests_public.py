def run_tests(namespace, mode="all"):
    cases = [
        ('Keep repeated content', lambda f: assert_close(f(['the','cat','cat','and','dog'], ['the','and']), ['cat','cat','dog'])),
        ('Case matters', lambda f: assert_close(f(['The','the'], ['the']), ['The'])),
        ('No stopwords', lambda f: assert_close(f(['a','b'], []), ['a','b'])),
        ('No tokens', lambda f: assert_close(f([], ['a']), [])),
        ('Empty token rule', lambda f: assert_close(f(['','a'], ['']), ['a'])),
        ('Remove all', lambda f: assert_close(f(['x','x'], ['x']), [])),
        ('Reject numeric token', lambda f: rejects(f, [1], [])),
        ('Reject raw stopwords', lambda f: rejects(f, [], 'a')),
        ('Reject nontext stopword', lambda f: rejects(f, [], [None])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['the','cat','cat','and','dog'], ['the','and']), ['cat','cat','dog']))
    ]
    return run_cases(namespace, 'remove_stopwords', cases, mode)
