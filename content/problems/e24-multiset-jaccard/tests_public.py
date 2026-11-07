def run_tests(namespace, mode="all"):
    cases = [
        ('Repetition changes overlap', lambda f: assert_close(f(['a','a','b'], ['a','b','b']), 0.5)),
        ('Two empty documents', lambda f: assert_close(f([], []), 1.0)),
        ('Disjoint documents', lambda f: assert_close(f(['a'], ['b']), 0.0)),
        ('Identical repeated text', lambda f: assert_close(f(['a','a'], ['a','a']), 1.0)),
        ('One empty document', lambda f: assert_close(f([], ['x']), 0.0)),
        ('Partial multiplicity', lambda f: assert_close(f(['x','x','x'], ['x']), 1/3)),
        ('Reject raw text', lambda f: rejects(f, 'a', ['a'])),
        ('Reject numeric token', lambda f: rejects(f, [1], ['a'])),
        ('Reject empty token', lambda f: rejects(f, ['a'], [''])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, ['a','a','b'], ['a','b','b']), 0.5))
    ]
    return run_cases(namespace, 'multiset_jaccard', cases, mode)
