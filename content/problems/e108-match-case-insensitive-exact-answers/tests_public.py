def run_tests(namespace, mode="all"):
    cases = [
        ('Case and whitespace', lambda f: assert_close(f('  New YORK ', ['New York']), True)),
        ('Casefold expansion', lambda f: assert_close(f('STRASSE', ['Straße']), True)),
        ('Punctuation matters', lambda f: assert_close(f('yes!', ['yes']), False)),
        ('No accepted answer', lambda f: assert_close(f('yes', []), False)),
        ('Empty normalized answer', lambda f: assert_close(f(' \t', ['']), True)),
        ('Any accepted alternative', lambda f: assert_close(f('b', ['a','B']), True)),
        ('Reject nontext answer', lambda f: rejects(f, None, ['a'])),
        ('Reject nontext alternative', lambda f: rejects(f, 'a', [1])),
        ('Reject raw alternatives', lambda f: rejects(f, 'a', 'a')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, '  New YORK ', ['New York']), True))
    ]
    return run_cases(namespace, 'answer_matches', cases, mode)
