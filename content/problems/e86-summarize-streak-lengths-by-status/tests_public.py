def run_tests(namespace, mode="all"):
    cases = [
        ('Separated runs', lambda f: assert_close(f(['a','a','b','a']), {'a':2,'b':1})),
        ('Longer later run', lambda f: assert_close(f(['a','b','a','a','a']), {'a':3,'b':1})),
        ('Single item', lambda f: assert_close(f(['x']), {'x':1})),
        ('Empty trace', lambda f: assert_close(f([]), {})),
        ('Alternation', lambda f: assert_close(f(['a','b','a','b']), {'a':1,'b':1})),
        ('One long run', lambda f: assert_close(f(['z']*4), {'z':4})),
        ('Reject numeric status', lambda f: rejects(f, [1])),
        ('Reject empty status', lambda f: rejects(f, [''])),
        ('Reject nonsequence', lambda f: rejects(f, {})),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['a','a','b','a']), {'a':2,'b':1}))
    ]
    return run_cases(namespace, 'longest_streaks', cases, mode)
