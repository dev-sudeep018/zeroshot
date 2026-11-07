def run_tests(namespace, mode="all"):
    cases = [
        ('Field changes', lambda f: assert_close(f({'a':1,'b':2}, {'b':3,'c':4}), dict(added={'c':4},removed={'a':1},changed={'b':[2,3]}))),
        ('None added', lambda f: assert_close(f({}, {'a':None}), dict(added={'a':None},removed={},changed={}))),
        ('Nested value changed', lambda f: assert_close(f({'x':{'a':1}}, {'x':{'a':2}}), dict(added={},removed={},changed={'x':[{'a':1},{'a':2}]}))),
        ('Both empty', lambda f: assert_close(f({}, {}), dict(added={},removed={},changed={}))),
        ('Equal values', lambda f: assert_close(f({'x':[1]}, {'x':[1]}), dict(added={},removed={},changed={}))),
        ('Removed None', lambda f: assert_close(f({'x':None}, {}), dict(added={},removed={'x':None},changed={}))),
        ('Reject invalid before', lambda f: rejects(f, [], {})),
        ('Reject invalid after', lambda f: rejects(f, {}, [])),
        ('Reject empty field key', lambda f: rejects(f, {'':1}, {})),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, {'a':1,'b':2}, {'b':3,'c':4}), dict(added={'c':4},removed={'a':1},changed={'b':[2,3]})))
    ]
    return run_cases(namespace, 'record_diff', cases, mode)
