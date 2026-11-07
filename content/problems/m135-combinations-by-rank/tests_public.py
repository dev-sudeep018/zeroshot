def run_tests(namespace, mode="all"):
    cases = [
        ('Middle pair', lambda f: assert_close(f(5,2,4), [1,2])),
        ('First triple', lambda f: assert_close(f(6,3,0), [0,1,2])),
        ('Last triple', lambda f: assert_close(f(6,3,19), [3,4,5])),
        ('Empty choice', lambda f: assert_close(f(5,0,0), [])),
        ('Choose everything', lambda f: assert_close(f(4,4,0), [0,1,2,3])),
        ('Large rank', lambda f: assert_close(f(30,4,20000), [7,20,26,27])),
        ('Reject rank at count', lambda f: rejects(f,5,2,10)),
        ('Reject excess chosen', lambda f: rejects(f,4,5,0)),
        ('Reject negative rank', lambda f: rejects(f,4,2,-1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,5,2,4), [1,2])),
    ]
    return run_cases(namespace, 'unrank_combination', cases, mode)
