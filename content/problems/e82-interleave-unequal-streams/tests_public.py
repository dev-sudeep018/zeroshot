def run_tests(namespace, mode="all"):
    cases = [
        ('Unequal stream lengths', lambda f: assert_close(f([[1,2,3],['a']]), [1,'a',2,3])),
        ('Empty middle stream', lambda f: assert_close(f([[1],[],[2,3]]), [1,2,3])),
        ('Two full rounds', lambda f: assert_close(f([[1,2],[3,4]]), [1,3,2,4])),
        ('No streams', lambda f: assert_close(f([]), [])),
        ('All empty', lambda f: assert_close(f([[],[]]), [])),
        ('Duplicates retained', lambda f: assert_close(f([['x','x'],['x']]), ['x','x','x'])),
        ('Reject raw stream', lambda f: rejects(f, ['abc'])),
        ('Reject nonsequence outer', lambda f: rejects(f, {})),
        ('Reject invalid nested value', lambda f: rejects(f, [[{1,2}]])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [[1,2,3],['a']]), [1,'a',2,3]))
    ]
    return run_cases(namespace, 'interleave_streams', cases, mode)
