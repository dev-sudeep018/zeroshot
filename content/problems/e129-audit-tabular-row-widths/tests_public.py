def run_tests(namespace, mode="all"):
    cases = [
        ('Both ragged directions', lambda f: assert_close(f([[1,2],[3],[],[4,5,6]], 2), [[1,1],[2,0],[3,3]])),
        ('All aligned', lambda f: assert_close(f([[1],[2]], 1), [])),
        ('Zero-width schema', lambda f: assert_close(f([[],[1]], 0), [[1,1]])),
        ('No rows', lambda f: assert_close(f([], 3), [])),
        ('Nested cell counts once', lambda f: assert_close(f([[[1,2],3]], 2), [])),
        ('Tuple row', lambda f: assert_close(f([(1,2),(3,)], 2), [[1,1]])),
        ('Reject negative width', lambda f: rejects(f, [], -1)),
        ('Reject raw row', lambda f: rejects(f, ['abc'], 3)),
        ('Reject boolean width', lambda f: rejects(f, [], True)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [[1,2],[3],[],[4,5,6]], 2), [[1,1],[2,0],[3,3]]))
    ]
    return run_cases(namespace, 'row_width_issues', cases, mode)
