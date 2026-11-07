def run_tests(namespace, mode="all"):
    cases = [
        ('Nonadjacent duplicates', lambda f: assert_close(f(['a','b','a','a','b']), {'a':[0,2,3],'b':[1,4]})),
        ('Unique IDs', lambda f: assert_close(f(['a','b']), {})),
        ('Adjacent duplicates', lambda f: assert_close(f(['x','x']), {'x':[0,1]})),
        ('Empty input', lambda f: assert_close(f([]), {})),
        ('Case matters', lambda f: assert_close(f(['A','a','A']), {'A':[0,2]})),
        ('Exclude singleton', lambda f: assert_close(f(['x','y','x']), {'x':[0,2]})),
        ('Reject empty ID', lambda f: rejects(f, [''])),
        ('Reject numeric ID', lambda f: rejects(f, [1])),
        ('Reject raw IDs', lambda f: rejects(f, 'aaa')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['a','b','a','a','b']), {'a':[0,2,3],'b':[1,4]}))
    ]
    return run_cases(namespace, 'duplicate_positions', cases, mode)
