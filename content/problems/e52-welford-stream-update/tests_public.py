def run_tests(namespace, mode="all"):
    cases = [
        ('Start a stream', lambda f: assert_close(f(0, 0, 0, [1,2,3]), dict(count=3,mean=2.,m2=2.))),
        ('Continue existing state', lambda f: assert_close(f(2, 1.5, .5, [3]), dict(count=3,mean=2.,m2=2.))),
        ('No new values', lambda f: assert_close(f(3, 2, 2, []), dict(count=3,mean=2.,m2=2.))),
        ('Constant stream', lambda f: assert_close(f(0, 0, 0, [5,5,5]), dict(count=3,mean=5.,m2=0.))),
        ('Single observation', lambda f: assert_close(f(0, 0, 0, [-4]), dict(count=1,mean=-4.,m2=0.))),
        ('Symmetric observations', lambda f: assert_close(f(0, 0, 0, [-2,2]), dict(count=2,mean=0.,m2=8.))),
        ('Reject negative count', lambda f: rejects(f, -1, 0, 0, [1])),
        ('Reject negative m2', lambda f: rejects(f, 1, 0, -1, [1])),
        ('Reject invalid empty state', lambda f: rejects(f, 0, 1, 0, [1])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, 0, 0, 0, [1,2,3]), dict(count=3,mean=2.,m2=2.)))
        ,('Reject state beyond stream limit', lambda f: rejects(f, 1000000, 0, 0, [1]))
    ]
    return run_cases(namespace, 'welford_update', cases, mode)
