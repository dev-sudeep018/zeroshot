def run_tests(namespace, mode="all"):
    cases = [
        ('Replace and then keep', lambda f: assert_close(f([10,20,30,40], 2, [0,3]), np.array([30.,20.]))),
        ('Fill without extra draws', lambda f: assert_close(f([1,2], 3, []), np.array([1.,2.]))),
        ('Every arrival replaces one slot', lambda f: assert_close(f([1,2,3], 1, [0,0]), np.array([3.]))),
        ('No replacements', lambda f: assert_close(f([1,2,3], 1, [1,2]), np.array([1.]))),
        ('Empty stream', lambda f: assert_close(f([], 2, []), np.array([]))),
        ('Two different slots replaced', lambda f: assert_close(f([1,2,3,4], 2, [1,0]), np.array([4.,3.]))),
        ('Reject zero capacity', lambda f: rejects(f, [1], 0, [])),
        ('Reject wrong draw count', lambda f: rejects(f, [1,2], 1, [])),
        ('Reject draw outside current range', lambda f: rejects(f, [1,2], 1, [2])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [10,20,30,40], 2, [0,3]), np.array([30.,20.])))
    ]
    return run_cases(namespace, 'reservoir_sample', cases, mode)
