def run_tests(namespace, mode="all"):
    cases = [
        ('Priority route', lambda f: assert_close(f([dict(id='a',priority=4,blocked=False),dict(id='b',priority=2,blocked=False)]), dict(urgent=['a'],normal=['b']))),
        ('Blocked low priority', lambda f: assert_close(f([dict(id='x',priority=0,blocked=True)]), dict(urgent=['x'],normal=[]))),
        ('Boundary three', lambda f: assert_close(f([dict(id='x',priority=3,blocked=False)]), dict(urgent=[],normal=['x']))),
        ('Empty queue', lambda f: assert_close(f([]), dict(urgent=[],normal=[]))),
        ('Repeated identifiers', lambda f: assert_close(f([dict(id='a',priority=5,blocked=True)]*2), dict(urgent=['a','a'],normal=[]))),
        ('Both conditions', lambda f: assert_close(f([dict(id='x',priority=5,blocked=True),dict(id='y',priority=0,blocked=False)]), dict(urgent=['x'],normal=['y']))),
        ('Reject missing flag', lambda f: rejects(f, [dict(id='x',priority=4)])),
        ('Reject numeric flag', lambda f: rejects(f, [dict(id='x',priority=2,blocked=1)])),
        ('Reject bad priority', lambda f: rejects(f, [dict(id='x',priority=6,blocked=False)])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [dict(id='a',priority=4,blocked=False),dict(id='b',priority=2,blocked=False)]), dict(urgent=['a'],normal=['b'])))
    ]
    return run_cases(namespace, 'route_tickets', cases, mode)
