def run_tests(namespace, mode="all"):
    cases = [
        ('Boundary and overflow', lambda f: assert_close(f([0,2,3,5,6], [2,5]), [2,2,1])),
        ('No bounds', lambda f: assert_close(f([1,2,3], []), [3])),
        ('Empty values', lambda f: assert_close(f([], [2,5]), [0,0,0])),
        ('Zero bound', lambda f: assert_close(f([0,1], [0]), [1,1])),
        ('Repeated values', lambda f: assert_close(f([2,2,2], [2]), [3,0])),
        ('Large final bin', lambda f: assert_close(f([100], [1,2,3]), [0,0,0,1])),
        ('Reject duplicate bounds', lambda f: rejects(f, [], [1,1])),
        ('Reject negative value', lambda f: rejects(f, [-1], [0])),
        ('Reject fractional bound', lambda f: rejects(f, [], [1.5])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [0,2,3,5,6], [2,5]), [2,2,1]))
    ]
    return run_cases(namespace, 'quantity_histogram', cases, mode)
