def run_tests(namespace, mode="all"):
    cases = [
        ('Different units', lambda f: assert_close(f(['2ms','3s','1m']), [2,3000,60000])),
        ('Outer spaces', lambda f: assert_close(f([' 4s ']), [4000])),
        ('Zero duration', lambda f: assert_close(f(['0m','0002ms']), [0,2])),
        ('Empty list', lambda f: assert_close(f([]), [])),
        ('Maximum milliseconds', lambda f: assert_close(f(['1000000000ms']), [1000000000])),
        ('Long zero prefix', lambda f: assert_close(f(['0'*5000+'1ms']), [1])),
        ('Reject fractional duration', lambda f: rejects(f, ['1.5s'])),
        ('Reject internal space', lambda f: rejects(f, ['1 s'])),
        ('Reject overflow', lambda f: rejects(f, ['1000000000s'])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['2ms','3s','1m']), [2,3000,60000]))
    ]
    return run_cases(namespace, 'duration_milliseconds', cases, mode)
