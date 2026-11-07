def run_tests(namespace, mode="all"):
    cases = [
        ('One substitution', lambda f: assert_close(f(['red','cat'], ['blue','cat']), 1)),
        ('Insert a missing word', lambda f: assert_close(f(['a','cat'], ['a','small','cat']), 1)),
        ('Empty hypothesis', lambda f: assert_close(f([], ['a','b']), 2)),
        ('Equal sequences', lambda f: assert_close(f(['a','b'], ['a','b']), 0)),
        ('Transposition needs two edits', lambda f: assert_close(f(['a','b'], ['b','a']), 2)),
        ('Delete repeated word', lambda f: assert_close(f(['a','a','b'], ['a','b']), 1)),
        ('Reject text instead of tokens', lambda f: rejects(f, 'ab', ['a'])),
        ('Reject invalid token', lambda f: rejects(f, ['a'], [None])),
        ('Reject excessive length', lambda f: rejects(f, ['a']*501, [])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, ['red','cat'], ['blue','cat']), 1))
    ]
    return run_cases(namespace, 'edit_distance', cases, mode)
