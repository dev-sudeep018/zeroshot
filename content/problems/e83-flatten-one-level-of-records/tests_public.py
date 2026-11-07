def run_tests(namespace, mode="all"):
    cases = [
        ('Keep nested payload', lambda f: assert_close(f([[1,[2,3]],[4]]), [1,[2,3],4])),
        ('Empty batches skipped', lambda f: assert_close(f([[],[1],[]]), [1])),
        ('Records remain records', lambda f: assert_close(f([[{'x':1}],[{'x':2}]]), [{'x':1},{'x':2}])),
        ('Empty outer', lambda f: assert_close(f([]), [])),
        ('Tuple batches', lambda f: assert_close(f([(1,2),(3,)]), [1,2,3])),
        ('None payload preserved', lambda f: assert_close(f([[None],[]]), [None])),
        ('Reject raw batch', lambda f: rejects(f, ['abc'])),
        ('Reject numeric batch', lambda f: rejects(f, [1])),
        ('Reject raw outer', lambda f: rejects(f, 'abc')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [[1,[2,3]],[4]]), [1,[2,3],4]))
    ]
    return run_cases(namespace, 'flatten_batches', cases, mode)
