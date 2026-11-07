def run_tests(namespace, mode="all"):
    cases = [
        ('Normal lifecycle', lambda f: assert_close(f([['open','a'],['close','a']]), dict(open_ids=[],invalid_indices=[]))),
        ('Duplicate open', lambda f: assert_close(f([['open','a'],['open','a']]), dict(open_ids=['a'],invalid_indices=[1]))),
        ('Absent close', lambda f: assert_close(f([['close','a'],['open','a']]), dict(open_ids=['a'],invalid_indices=[0]))),
        ('No events', lambda f: assert_close(f([]), dict(open_ids=[],invalid_indices=[]))),
        ('Sorted final IDs', lambda f: assert_close(f([['open','z'],['open','a']]), dict(open_ids=['a','z'],invalid_indices=[]))),
        ('Reopen after close', lambda f: assert_close(f([['open','x'],['close','x'],['open','x']]), dict(open_ids=['x'],invalid_indices=[]))),
        ('Reject unknown event', lambda f: rejects(f, [['pause','a']])),
        ('Reject empty task ID', lambda f: rejects(f, [['open','']])),
        ('Reject malformed event', lambda f: rejects(f, [['open']])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [['open','a'],['close','a']]), dict(open_ids=[],invalid_indices=[])))
    ]
    return run_cases(namespace, 'task_state', cases, mode)
