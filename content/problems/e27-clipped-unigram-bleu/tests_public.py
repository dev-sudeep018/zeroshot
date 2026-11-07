def run_tests(namespace, mode="all"):
    cases = [
        ('Repetition is clipped', lambda f: assert_close(f(['a','a','a'], ['a','b']), 1/3)),
        ('Short output penalty', lambda f: assert_close(f(['a'], ['a','b']), np.exp(-1))),
        ('Perfect unigram overlap', lambda f: assert_close(f(['b','a'], ['a','b']), 1.0)),
        ('Empty candidate', lambda f: assert_close(f([], ['a']), 0.0)),
        ('No matching token', lambda f: assert_close(f(['x'], ['a']), 0.0)),
        ('Extra unmatched token', lambda f: assert_close(f(['a','b','x'], ['a','b']), 2/3)),
        ('Reject empty reference', lambda f: rejects(f, ['a'], [])),
        ('Reject raw text', lambda f: rejects(f, 'a', ['a'])),
        ('Reject empty token', lambda f: rejects(f, [''], ['a'])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, ['a','a','a'], ['a','b']), 1/3))
    ]
    return run_cases(namespace, 'bleu_one', cases, mode)
