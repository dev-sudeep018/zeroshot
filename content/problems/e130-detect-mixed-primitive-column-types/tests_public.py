def run_tests(namespace, mode="all"):
    cases = [
        ('Separate booleans and numbers', lambda f: assert_close(f([{'x':True},{'x':1},{'x':1.0}], ['x']), {'x':['bool','float','int']})),
        ('Missing versus null', lambda f: assert_close(f([{}, {'x':None}], ['x']), {'x':['missing','null']})),
        ('Mixed text and integer', lambda f: assert_close(f([{'x':'1'},{'x':1}], ['x']), {'x':['int','str']})),
        ('No rows', lambda f: assert_close(f([], ['x']), {'x':[]})),
        ('No selected fields', lambda f: assert_close(f([{'x':[1]}], []), {})),
        ('Homogeneous column', lambda f: assert_close(f([{'x':'a'},{'x':'b'}], ['x']), {'x':['str']})),
        ('Reject nested selected cell', lambda f: rejects(f, [{'x':[]}], ['x'])),
        ('Reject duplicate field', lambda f: rejects(f, [], ['x','x'])),
        ('Reject nonfinite cell', lambda f: rejects(f, [{'x':float('inf')}], ['x'])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'x':True},{'x':1},{'x':1.0}], ['x']), {'x':['bool','float','int']}))
    ]
    return run_cases(namespace, 'column_type_audit', cases, mode)
