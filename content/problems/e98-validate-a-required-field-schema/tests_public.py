def run_tests(namespace, mode="all"):
    cases = [
        ('Both issue types', lambda f: assert_close(f([{'a':1,'x':2}], ['a','b'], ['a','b']), [dict(missing=['b'],unexpected=['x'])])),
        ('Optional field omitted', lambda f: assert_close(f([{'a':1}], ['a'], ['a','b']), [dict(missing=[],unexpected=[])])),
        ('Empty row', lambda f: assert_close(f([{}], ['x'], ['x']), [dict(missing=['x'],unexpected=[])])),
        ('No rows', lambda f: assert_close(f([], [], []), [])),
        ('None still present', lambda f: assert_close(f([{'a':None}], ['a'], ['a']), [dict(missing=[],unexpected=[])])),
        ('Unexpected order sorted', lambda f: assert_close(f([{'z':1,'a':2}], [], []), [dict(missing=[],unexpected=['a','z'])])),
        ('Reject impossible schema', lambda f: rejects(f, [], ['a'], [])),
        ('Reject duplicate allowed field', lambda f: rejects(f, [], [], ['x','x'])),
        ('Reject nonrecord row', lambda f: rejects(f, [1], [], [])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'a':1,'x':2}], ['a','b'], ['a','b']), [dict(missing=['b'],unexpected=['x'])]))
    ]
    return run_cases(namespace, 'schema_issues', cases, mode)
