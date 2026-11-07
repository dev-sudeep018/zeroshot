def run_tests(namespace, mode="all"):
    cases = [
        ('Absent field fallback', lambda f: assert_close(f([{'x':2},{}], 'x', 9), [2,9])),
        ('Preserve falsy values', lambda f: assert_close(f([{'x':0},{'x':False},{'x':''},{'x':None}], 'x', 9), [0,False,'',None])),
        ('Nested fallback', lambda f: assert_close(f([{}], 'x', {'v':1}), [{'v':1}])),
        ('No rows', lambda f: assert_close(f([], 'x', None), [])),
        ('Different fields', lambda f: assert_close(f([{'y':1}], 'x', 'missing'), ['missing'])),
        ('Nested existing value', lambda f: assert_close(f([{'x':[1,2]}], 'x', 0), [[1,2]])),
        ('Reject empty field', lambda f: rejects(f, [], '', 0)),
        ('Reject invalid row', lambda f: rejects(f, [None], 'x', 0)),
        ('Reject unsupported fallback', lambda f: rejects(f, [], 'x', {1,2})),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'x':2},{}], 'x', 9), [2,9]))
    ]
    return run_cases(namespace, 'extract_field', cases, mode)
