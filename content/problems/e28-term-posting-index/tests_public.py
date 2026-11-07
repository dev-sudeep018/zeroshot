def run_tests(namespace, mode="all"):
    cases = [
        ('Repeated term keeps positions', lambda f: assert_close(f([['a','b','a'], ['b']]), {'a':[[0,[0,2]]],'b':[[0,[1]],[1,[0]]]})),
        ('Empty corpus', lambda f: assert_close(f([]), {})),
        ('Empty document preserves IDs', lambda f: assert_close(f([[], ['x']]), {'x':[[1,[0]]]})),
        ('Separate documents', lambda f: assert_close(f([['a'], ['a']]), {'a':[[0,[0]],[1,[0]]]})),
        ('Case-sensitive terms', lambda f: assert_close(f([['A','a']]), {'A':[[0,[0]]],'a':[[0,[1]]]})),
        ('No populated documents', lambda f: assert_close(f([[], []]), {})),
        ('Reject raw corpus text', lambda f: rejects(f, 'abc')),
        ('Reject raw document', lambda f: rejects(f, ['abc'])),
        ('Reject empty token', lambda f: rejects(f, [['']])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [['a','b','a'], ['b']]), {'a':[[0,[0,2]]],'b':[[0,[1]],[1,[0]]]}))
    ]
    return run_cases(namespace, 'posting_index', cases, mode)
