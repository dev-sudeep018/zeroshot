def run_tests(namespace, mode="all"):
    cases = [
        ('Open and block', lambda f: assert_close(f(['failure','failure','success'],2), dict(states=['closed','open','open'],blocked=[2]))),
        ('Success clears streak', lambda f: assert_close(f(['failure','success','failure'],2), dict(states=['closed','closed','closed'],blocked=[]))),
        ('Explicit reset', lambda f: assert_close(f(['failure','reset','success'],1), dict(states=['open','closed','closed'],blocked=[]))),
        ('No events', lambda f: assert_close(f([],1), dict(states=[],blocked=[]))),
        ('Reset closed circuit', lambda f: assert_close(f(['reset','failure'],2), dict(states=['closed','closed'],blocked=[]))),
        ('Blocked failure ignored', lambda f: assert_close(f(['failure','failure','reset','failure'],1), dict(states=['open','open','closed','open'],blocked=[1]))),
        ('Reject invalid event', lambda f: rejects(f, ['pending'],2)),
        ('Reject zero threshold', lambda f: rejects(f, [],0)),
        ('Reject bool threshold', lambda f: rejects(f, [],True)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['failure','failure','success'],2), dict(states=['closed','open','open'],blocked=[2])))
    ]
    return run_cases(namespace, 'circuit_trace', cases, mode)
