def run_tests(namespace, mode="all"):
    cases = [
        ('Bounded missing run', lambda f: assert_close(f([1,None,None,None,2,None], 2), [1,1,1,None,2,2])),
        ('Leading missing values', lambda f: assert_close(f([None,None,3,None], 1), [None,None,3,3])),
        ('Zero and false observed', lambda f: assert_close(f([0,None,False,None], 1), [0,0,False,False])),
        ('Empty values', lambda f: assert_close(f([], 2), [])),
        ('Zero limit', lambda f: assert_close(f([1,None], 0), [1,None])),
        ('Nested payload copy', lambda f: assert_close(f([[1],None], 1), [[1],[1]])),
        ('Reject negative limit', lambda f: rejects(f, [], -1)),
        ('Reject boolean limit', lambda f: rejects(f, [], True)),
        ('Reject raw values', lambda f: rejects(f, 'abc', 2)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [1,None,None,None,2,None], 2), [1,1,1,None,2,2]))
    ]
    return run_cases(namespace, 'forward_fill', cases, mode)
