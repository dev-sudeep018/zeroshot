def run_tests(namespace, mode="all"):
    cases = [
        ('Self and cross transitions', lambda f: assert_close(f(['open','open','closed','open']), {('open','open'):1,('open','closed'):1,('closed','open'):1})),
        ('Repeated transition', lambda f: assert_close(f(['a','b','a','b']), {('a','b'):2,('b','a'):1})),
        ('One status', lambda f: assert_close(f(['a']), {})),
        ('Empty trace', lambda f: assert_close(f([]), {})),
        ('All equal', lambda f: assert_close(f(['x','x','x']), {('x','x'):2})),
        ('Direction matters', lambda f: assert_close(f(['a','b','c']), {('a','b'):1,('b','c'):1})),
        ('Reject empty status', lambda f: rejects(f, [''])),
        ('Reject raw trace', lambda f: rejects(f, 'abc')),
        ('Reject numeric status', lambda f: rejects(f, [1,2])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['open','open','closed','open']), {('open','open'):1,('open','closed'):1,('closed','open'):1}))
    ]
    return run_cases(namespace, 'transition_counts', cases, mode)
