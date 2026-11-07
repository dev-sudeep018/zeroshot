def run_tests(namespace, mode="all"):
    cases = [
        ('Overlapping repetition', lambda f: assert_close(f(['a','a','a'], 2), {('a','a'):2})),
        ('Unigram frequencies', lambda f: assert_close(f(['a','b','a'], 1), {('a',):2,('b',):1})),
        ('Window longer than text', lambda f: assert_close(f(['a'], 2), {})),
        ('Empty document', lambda f: assert_close(f([], 1), {})),
        ('Tokens preserve boundaries', lambda f: assert_close(f(['a b','c','a','b c'], 2), {('a b','c'):1,('c','a'):1,('a','b c'):1})),
        ('Case sensitivity', lambda f: assert_close(f(['A','a'], 1), {('A',):1,('a',):1})),
        ('Reject zero window', lambda f: rejects(f, ['a'], 0)),
        ('Reject string instead of tokens', lambda f: rejects(f, 'abc', 2)),
        ('Reject empty token', lambda f: rejects(f, [''], 1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, ['a','a','a'], 2), {('a','a'):2}))
    ]
    return run_cases(namespace, 'ngram_counts', cases, mode)
