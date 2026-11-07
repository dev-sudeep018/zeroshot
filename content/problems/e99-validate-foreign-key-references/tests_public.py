def run_tests(namespace, mode="all"):
    cases = [
        ('One orphan', lambda f: assert_close(f(['a'], [{'parent':'a'},{'parent':'b'}], 'parent'), [1])),
        ('No parents', lambda f: assert_close(f([], [{'p':'x'},{'p':'y'}], 'p'), [0,1])),
        ('No children', lambda f: assert_close(f(['a'], [], 'p'), [])),
        ('Repeated orphan', lambda f: assert_close(f([], [{'p':'x'},{'p':'x'}], 'p'), [0,1])),
        ('All matched', lambda f: assert_close(f(['a','b'], [{'p':'b'},{'p':'a'}], 'p'), [])),
        ('Case matters', lambda f: assert_close(f(['A'], [{'p':'a'}], 'p'), [0])),
        ('Reject duplicate parent IDs', lambda f: rejects(f, ['a','a'], [], 'p')),
        ('Reject missing foreign key', lambda f: rejects(f, [], [{}], 'p')),
        ('Reject numeric foreign key', lambda f: rejects(f, [], [{'p':1}], 'p')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['a'], [{'parent':'a'},{'parent':'b'}], 'parent'), [1]))
    ]
    return run_cases(namespace, 'orphan_rows', cases, mode)
