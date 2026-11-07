def run_tests(namespace, mode="all"):
    cases = [
        ('Sequential stock use', lambda f: assert_close(f({'a':5}, [['a',3],['a',4]]), dict(remaining={'a':0},filled=[3,2],unfilled=[0,2]))),
        ('Unknown item', lambda f: assert_close(f({}, [['x',2]]), dict(remaining={},filled=[0],unfilled=[2]))),
        ('Zero request', lambda f: assert_close(f({'a':2}, [['a',0]]), dict(remaining={'a':2},filled=[0],unfilled=[0]))),
        ('No requests', lambda f: assert_close(f({'a':2}, []), dict(remaining={'a':2},filled=[],unfilled=[]))),
        ('Independent items', lambda f: assert_close(f({'a':1,'b':2}, [['b',1],['a',2]]), dict(remaining={'a':0,'b':1},filled=[1,1],unfilled=[0,1]))),
        ('Exact exhaustion', lambda f: assert_close(f({'a':2}, [['a',2]]), dict(remaining={'a':0},filled=[2],unfilled=[0]))),
        ('Reject negative stock', lambda f: rejects(f, {'a':-1}, [])),
        ('Reject malformed request', lambda f: rejects(f, {}, [['x']])),
        ('Reject fractional quantity', lambda f: rejects(f, {}, [['a',1.5]])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, {'a':5}, [['a',3],['a',4]]), dict(remaining={'a':0},filled=[3,2],unfilled=[0,2])))
    ]
    return run_cases(namespace, 'fill_requests', cases, mode)
