def run_tests(namespace, mode="all"):
    cases = [
        ('First page', lambda f: assert_close(f(['a','b','c'], 0, 2), dict(items=['a','b'],total=3,next_offset=2))),
        ('Final partial page', lambda f: assert_close(f(['a','b','c'], 2, 2), dict(items=['c'],total=3,next_offset=None))),
        ('Beyond end', lambda f: assert_close(f([1], 9, 2), dict(items=[],total=1,next_offset=None))),
        ('Empty collection', lambda f: assert_close(f([], 0, 2), dict(items=[],total=0,next_offset=None))),
        ('Exact final page', lambda f: assert_close(f([1,2], 0, 2), dict(items=[1,2],total=2,next_offset=None))),
        ('Middle page', lambda f: assert_close(f([0,1,2,3], 1, 1), dict(items=[1],total=4,next_offset=2))),
        ('Reject negative offset', lambda f: rejects(f, [], -1, 1)),
        ('Reject zero limit', lambda f: rejects(f, [], 0, 0)),
        ('Reject invalid collection', lambda f: rejects(f, {}, 0, 1)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['a','b','c'], 0, 2), dict(items=['a','b'],total=3,next_offset=2)))
    ]
    return run_cases(namespace, 'record_page', cases, mode)
