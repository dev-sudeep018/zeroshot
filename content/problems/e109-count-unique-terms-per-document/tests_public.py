def run_tests(namespace, mode="all"):
    cases = [
        ('Within-document duplicates', lambda f: assert_close(f([['a','a','b'],['a','c']]), {'a':2,'b':1,'c':1})),
        ('Repeated documents', lambda f: assert_close(f([['x'],['x']]), {'x':2})),
        ('Empty documents', lambda f: assert_close(f([[],['a'],[]]), {'a':1})),
        ('No documents', lambda f: assert_close(f([]), {})),
        ('Case-sensitive terms', lambda f: assert_close(f([['A','a']]), {'A':1,'a':1})),
        ('All empty', lambda f: assert_close(f([[],[]]), {})),
        ('Reject raw document', lambda f: rejects(f, ['abc'])),
        ('Reject empty term', lambda f: rejects(f, [['']])),
        ('Reject numeric term', lambda f: rejects(f, [[1]])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [['a','a','b'],['a','c']]), {'a':2,'b':1,'c':1}))
    ]
    return run_cases(namespace, 'document_frequencies', cases, mode)
