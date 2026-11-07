def run_tests(namespace, mode="all"):
    cases = [
        ('Unequal lengths', lambda f: assert_close(f([[1,2],['a']]), [[1,'a'],[2,None]])),
        ('Empty first column', lambda f: assert_close(f([[],[1,2]]), [[None,1],[None,2]])),
        ('Equal lengths', lambda f: assert_close(f([[1,2],[3,4]]), [[1,3],[2,4]])),
        ('No columns', lambda f: assert_close(f([]), [])),
        ('All empty', lambda f: assert_close(f([[],[]]), [])),
        ('Present None', lambda f: assert_close(f([[None],[2]]), [[None,2]])),
        ('Reject raw column', lambda f: rejects(f, ['ab'])),
        ('Reject invalid outer', lambda f: rejects(f, {})),
        ('Reject unsupported cell', lambda f: rejects(f, [[{1}]])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [[1,2],['a']]), [[1,'a'],[2,None]]))
    ]
    return run_cases(namespace, 'zip_columns', cases, mode)
