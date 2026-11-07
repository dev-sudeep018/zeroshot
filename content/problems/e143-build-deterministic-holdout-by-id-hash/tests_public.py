def run_tests(namespace, mode="all"):
    cases = [
        ('Mixed hash buckets', lambda f: assert_close(f(['a','b','abc'],5000), dict(train=['b'],holdout=['a','abc']))),
        ('Bucket equality stays training', lambda f: assert_close(f(['a','abc'],2250), dict(train=['a'],holdout=['abc']))),
        ('Threshold just above bucket', lambda f: assert_close(f(['b','a'],2251), dict(train=['b'],holdout=['a']))),
        ('All training', lambda f: assert_close(f(['a','b'],0), dict(train=['a','b'],holdout=[]))),
        ('All holdout', lambda f: assert_close(f(['b','a'],10000), dict(train=[],holdout=['b','a']))),
        ('No IDs', lambda f: assert_close(f([],5000), dict(train=[],holdout=[]))),
        ('Stable singleton', lambda f: assert_close(f(['a'],0), dict(train=['a'],holdout=[]))),
        ('Unicode key', lambda f: assert_close(f(['資料'],10000), dict(train=[],holdout=['資料']))),
        ('Order preserved', lambda f: assert_close(f(['z','m','a'],0), dict(train=['z','m','a'],holdout=[]))),
        ('Reject duplicate ID', lambda f: rejects(f, ['x','x'],5000)),
        ('Reject bool threshold', lambda f: rejects(f, [],True)),
        ('Reject outside range', lambda f: rejects(f, [],10001)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['a','b','abc'],5000), dict(train=['b'],holdout=['a','abc'])))
    ]
    return run_cases(namespace, 'hash_holdout', cases, mode)
