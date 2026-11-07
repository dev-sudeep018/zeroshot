def run_tests(namespace, mode="all"):
    cases = [
        ('Missing and unknown', lambda f: assert_close(f([{'x':'a'},{'x':'b'},{}], 'x', ['a']), [1,2])),
        ('Null and number issues', lambda f: assert_close(f([{'x':None},{'x':1}], 'x', ['1']), [0,1])),
        ('Empty string allowed', lambda f: assert_close(f([{'x':''}], 'x', ['']), [])),
        ('No rows', lambda f: assert_close(f([], 'x', ['a']), [])),
        ('Case-sensitive vocabulary', lambda f: assert_close(f([{'x':'A'},{'x':'a'}], 'x', ['a']), [0])),
        ('Empty vocabulary', lambda f: assert_close(f([{'x':'a'}], 'x', []), [0])),
        ('Reject duplicate vocabulary', lambda f: rejects(f, [], 'x', ['a','a'])),
        ('Reject nontext vocabulary', lambda f: rejects(f, [], 'x', [1])),
        ('Reject empty field name', lambda f: rejects(f, [], '', [])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'x':'a'},{'x':'b'},{}], 'x', ['a']), [1,2]))
    ]
    return run_cases(namespace, 'invalid_categories', cases, mode)
