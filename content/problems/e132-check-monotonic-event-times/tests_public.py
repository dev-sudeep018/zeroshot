def run_tests(namespace, mode="all"):
    cases = [
        ('Two local decreases', lambda f: assert_close(f([3,1,2,0]), [[1,3,1],[3,2,0]])),
        ('Ties allowed', lambda f: assert_close(f([1,1,2]), [])),
        ('Negative timestamps', lambda f: assert_close(f([-1,-3,-2]), [[1,-1,-3]])),
        ('Empty trace', lambda f: assert_close(f([]), [])),
        ('One timestamp', lambda f: assert_close(f([5]), [])),
        ('Adjacent not global maximum', lambda f: assert_close(f([5,1,2,3]), [[1,5,1]])),
        ('Reject fractional time', lambda f: rejects(f, [1.5])),
        ('Reject boolean time', lambda f: rejects(f, [True])),
        ('Reject out of bounds', lambda f: rejects(f, [1000000001])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [3,1,2,0]), [[1,3,1],[3,2,0]]))
    ]
    return run_cases(namespace, 'timestamp_decreases', cases, mode)
