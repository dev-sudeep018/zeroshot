def run_tests(namespace, mode="all"):
    cases = [
        ('Composite equality', lambda f: assert_close(f([{'a':'x','b':'1'},{'a':'x','b':'2'},{'a':'x','b':'1'}], ['a','b']), [[0,2]])),
        ('Multiple duplicate groups', lambda f: assert_close(f([{'x':'a'},{'x':'b'},{'x':'b'},{'x':'a'}], ['x']), [[0,3],[1,2]])),
        ('Delimiter-safe tuples', lambda f: assert_close(f([{'a':'x|y','b':'z'},{'a':'x','b':'y|z'}], ['a','b']), [])),
        ('No rows', lambda f: assert_close(f([], ['x']), [])),
        ('All unique', lambda f: assert_close(f([{'x':'a'},{'x':'b'}], ['x']), [])),
        ('Empty strings valid', lambda f: assert_close(f([{'x':''},{'x':''}], ['x']), [[0,1]])),
        ('Reject missing field', lambda f: rejects(f, [{}], ['x'])),
        ('Reject nontext key value', lambda f: rejects(f, [{'x':1}], ['x'])),
        ('Reject empty key definition', lambda f: rejects(f, [], [])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'a':'x','b':'1'},{'a':'x','b':'2'},{'a':'x','b':'1'}], ['a','b']), [[0,2]]))
    ]
    return run_cases(namespace, 'duplicate_composite_keys', cases, mode)
