def run_tests(namespace, mode="all"):
    cases = [
        ('Exponential then capped', lambda f: assert_close(f(5,1,5), dict(delays=[1,2,4,5,5],total=17))),
        ('Cap below base', lambda f: assert_close(f(3,10,2), dict(delays=[2,2,2],total=6))),
        ('Fractional base', lambda f: assert_close(f(4,0.5,3), dict(delays=[0.5,1,2,3],total=6.5))),
        ('No retries', lambda f: assert_close(f(0,2,10), dict(delays=[],total=0))),
        ('Zero base', lambda f: assert_close(f(3,0,5), dict(delays=[0,0,0],total=0))),
        ('Zero cap', lambda f: assert_close(f(2,5,0), dict(delays=[0,0],total=0))),
        ('Reject too many retries', lambda f: rejects(f, 61,1,10)),
        ('Reject negative base', lambda f: rejects(f, 2,-1,5)),
        ('Reject nonfinite cap', lambda f: rejects(f, 2,1,float("inf"))),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, 5,1,5), dict(delays=[1,2,4,5,5],total=17)))
    ]
    return run_cases(namespace, 'retry_schedule', cases, mode)
