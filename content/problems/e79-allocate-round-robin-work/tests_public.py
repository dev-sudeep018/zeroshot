def run_tests(namespace, mode="all"):
    cases = [
        ('Uneven distribution', lambda f: assert_close(f(['a','b','c','d','e'], 2), [['a','c','e'],['b','d']])),
        ('More workers than jobs', lambda f: assert_close(f(['a'], 3), [['a'],[],[]])),
        ('No jobs', lambda f: assert_close(f([], 2), [[],[]])),
        ('Single worker', lambda f: assert_close(f(['a','b'], 1), [['a','b']])),
        ('Exact rounds', lambda f: assert_close(f(['a','b','c','d'], 2), [['a','c'],['b','d']])),
        ('Repeated jobs', lambda f: assert_close(f(['a','a'], 2), [['a'],['a']])),
        ('Reject zero workers', lambda f: rejects(f, [], 0)),
        ('Reject fractional workers', lambda f: rejects(f, [], 1.5)),
        ('Reject empty job ID', lambda f: rejects(f, [''], 1)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['a','b','c','d','e'], 2), [['a','c','e'],['b','d']]))
    ]
    return run_cases(namespace, 'distribute_jobs', cases, mode)
