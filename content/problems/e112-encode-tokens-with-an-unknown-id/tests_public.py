def run_tests(namespace, mode="all"):
    cases = [
        ('Known and unknown', lambda f: assert_close(f(['a','z','b'], {'a':2,'b':3}, 0), dict(ids=[2,0,3],unknown_positions=[1]))),
        ('Repeated unknown', lambda f: assert_close(f(['x','x'], {}, 9), dict(ids=[9,9],unknown_positions=[0,1]))),
        ('Empty tokens', lambda f: assert_close(f([], {'a':1}, 0), dict(ids=[],unknown_positions=[]))),
        ('ID zero valid', lambda f: assert_close(f(['a'], {'a':0}, 1), dict(ids=[0],unknown_positions=[]))),
        ('Case sensitive', lambda f: assert_close(f(['A','a'], {'a':2}, 0), dict(ids=[0,2],unknown_positions=[0]))),
        ('Empty token unknown', lambda f: assert_close(f([''], {}, 0), dict(ids=[0],unknown_positions=[0]))),
        ('Reject duplicate IDs', lambda f: rejects(f, [], {'a':1,'b':1}, 0)),
        ('Reject unknown collides', lambda f: rejects(f, [], {'a':0}, 0)),
        ('Reject negative ID', lambda f: rejects(f, [], {'a':-1}, 0)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['a','z','b'], {'a':2,'b':3}, 0), dict(ids=[2,0,3],unknown_positions=[1])))
    ]
    return run_cases(namespace, 'encode_tokens', cases, mode)
