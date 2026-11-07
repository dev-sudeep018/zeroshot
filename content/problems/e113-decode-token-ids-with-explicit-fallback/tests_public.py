def run_tests(namespace, mode="all"):
    cases = [
        ('Unknown fallback', lambda f: assert_close(f([2,9,3], {'a':2,'b':3}, '?'), dict(tokens=['a','?','b'],unknown_ids=[9]))),
        ('Repeated unknown', lambda f: assert_close(f([1,1], {}, 'UNK'), dict(tokens=['UNK','UNK'],unknown_ids=[1,1]))),
        ('Zero ID', lambda f: assert_close(f([0], {'x':0}, '?'), dict(tokens=['x'],unknown_ids=[]))),
        ('Empty IDs', lambda f: assert_close(f([], {}, '?'), dict(tokens=[],unknown_ids=[]))),
        ('Empty fallback', lambda f: assert_close(f([7], {}, ''), dict(tokens=[''],unknown_ids=[7]))),
        ('Decode ordering', lambda f: assert_close(f([3,2,3], {'a':2,'b':3}, '?'), dict(tokens=['b','a','b'],unknown_ids=[]))),
        ('Reject negative ID', lambda f: rejects(f, [-1], {}, '?')),
        ('Reject duplicate vocabulary ID', lambda f: rejects(f, [], {'a':1,'b':1}, '?')),
        ('Reject nontext fallback', lambda f: rejects(f, [], {}, None)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [2,9,3], {'a':2,'b':3}, '?'), dict(tokens=['a','?','b'],unknown_ids=[9])))
    ]
    return run_cases(namespace, 'decode_tokens', cases, mode)
