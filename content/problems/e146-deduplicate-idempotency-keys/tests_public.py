def run_tests(namespace, mode="all"):
    cases = [
        ('Replay within history', lambda f: assert_close(f(['a','a','b','a'],2), dict(accepted=[0,2],history=['a','b']))),
        ('Evicted key accepted', lambda f: assert_close(f(['a','b','c','a'],2), dict(accepted=[0,1,2,3],history=['c','a']))),
        ('No refresh on rejection', lambda f: assert_close(f(['a','b','a','c','a'],2), dict(accepted=[0,1,3,4],history=['c','a']))),
        ('Empty stream', lambda f: assert_close(f([],2), dict(accepted=[],history=[]))),
        ('Capacity one', lambda f: assert_close(f(['a','b','a'],1), dict(accepted=[0,1,2],history=['a']))),
        ('Case-sensitive keys', lambda f: assert_close(f(['A','a','A'],2), dict(accepted=[0,1],history=['A','a']))),
        ('Reject zero capacity', lambda f: rejects(f, [],0)),
        ('Reject empty key', lambda f: rejects(f, [''],2)),
        ('Reject bool capacity', lambda f: rejects(f, [],True)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['a','a','b','a'],2), dict(accepted=[0,2],history=['a','b'])))
    ]
    return run_cases(namespace, 'idempotent_accepts', cases, mode)
