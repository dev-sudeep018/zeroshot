def run_tests(namespace, mode="all"):
    cases = [
        ('Interior match', lambda f: assert_close(f('abcdefgh', [[3,5]], 2), [dict(left='bc',match='de',right='fg')])),
        ('Clip at edges', lambda f: assert_close(f('abc', [[0,1]], 9), [dict(left='',match='a',right='bc')])),
        ('Zero context', lambda f: assert_close(f('abc', [[1,2]], 0), [dict(left='',match='b',right='')])),
        ('No spans', lambda f: assert_close(f('abc', [], 2), [])),
        ('Empty match', lambda f: assert_close(f('abc', [[1,1]], 1), [dict(left='a',match='',right='b')])),
        ('End match', lambda f: assert_close(f('abc', [[2,3]], 1), [dict(left='b',match='c',right='')])),
        ('Reject negative radius', lambda f: rejects(f, 'a', [], -1)),
        ('Reject out of bounds', lambda f: rejects(f, 'a', [[0,2]], 1)),
        ('Reject wrong span width', lambda f: rejects(f, 'a', [[0]], 1)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, 'abcdefgh', [[3,5]], 2), [dict(left='bc',match='de',right='fg')]))
    ]
    return run_cases(namespace, 'context_windows', cases, mode)
