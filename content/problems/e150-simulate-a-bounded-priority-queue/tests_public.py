def run_tests(namespace, mode="all"):
    cases = [
        ('Highest priority first', lambda f: assert_close(f([['put','a',1],['put','b',3],['take']],2), dict(served=['b'],rejected=[],pending=['a']))),
        ('FIFO ties', lambda f: assert_close(f([['put','a',2],['put','b',2],['take']],2), dict(served=['a'],rejected=[],pending=['b']))),
        ('Reject full insert', lambda f: assert_close(f([['put','a',1],['put','b',9],['take']],1), dict(served=['a'],rejected=[1],pending=[]))),
        ('Empty queue', lambda f: assert_close(f([['take']],1), dict(served=[None],rejected=[],pending=[]))),
        ('No operations', lambda f: assert_close(f([],2), dict(served=[],rejected=[],pending=[]))),
        ('Negative priorities', lambda f: assert_close(f([['put','a',-3],['put','b',-1]],2), dict(served=[],rejected=[],pending=['b','a']))),
        ('Reject bool priority', lambda f: rejects(f, [['put','x',True]],2)),
        ('Reject zero capacity', lambda f: rejects(f, [],0)),
        ('Reject bad operation', lambda f: rejects(f, [['take',1]],2)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [['put','a',1],['put','b',3],['take']],2), dict(served=['b'],rejected=[],pending=['a'])))
    ]
    return run_cases(namespace, 'priority_queue', cases, mode)
