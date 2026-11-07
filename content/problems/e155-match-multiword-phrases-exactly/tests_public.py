def run_tests(namespace, mode="all"):
    cases = [
        ('Overlapping phrases', lambda f: assert_close(f(['a','a','a'],['a','a']), [0,1])),
        ('Whole-token matching', lambda f: assert_close(f(['cat','cats','cat'],['cat']), [0,2])),
        ('Case matters', lambda f: assert_close(f(['New','York','new','York'],['New','York']), [0])),
        ('Empty document', lambda f: assert_close(f([],['a']), [])),
        ('Phrase longer', lambda f: assert_close(f(['a'],['a','b']), [])),
        ('Empty token as value', lambda f: assert_close(f(['','x',''],['']), [0,2])),
        ('Reject empty phrase', lambda f: rejects(f, [],[])),
        ('Reject nontext token', lambda f: rejects(f, [1],['a'])),
        ('Reject raw string phrase', lambda f: rejects(f, ['a'],'a')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['a','a','a'],['a','a']), [0,1]))
    ]
    return run_cases(namespace, 'phrase_starts', cases, mode)
