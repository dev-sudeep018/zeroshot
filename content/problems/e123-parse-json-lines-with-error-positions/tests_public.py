def run_tests(namespace, mode="all"):
    cases = [
        ('Recover after bad line', lambda f: assert_close(f('{"x":1}\nbad\n{"x":2}'), dict(records=[{'x':1},{'x':2}],rejected_lines=[2]))),
        ('Physical line numbers', lambda f: assert_close(f('\n[]\n\n{}'), dict(records=[{}],rejected_lines=[2]))),
        ('Duplicate key rejected', lambda f: assert_close(f('{"x":1,"x":2}\n{}'), dict(records=[{}],rejected_lines=[1]))),
        ('Empty text', lambda f: assert_close(f(''), dict(records=[],rejected_lines=[]))),
        ('Nested JSON object', lambda f: assert_close(f('{"x":[true,null]}'), dict(records=[{'x':[True,None]}],rejected_lines=[]))),
        ('Nonfinite rejected', lambda f: assert_close(f('{"x":NaN}'), dict(records=[],rejected_lines=[1]))),
        ('Reject nonstring', lambda f: rejects(f, None)),
        ('Reject oversized', lambda f: rejects(f, ' '*10001)),
        ('Reject surrogate text', lambda f: rejects(f, '\ud800')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, '{"x":1}\nbad\n{"x":2}'), dict(records=[{'x':1},{'x':2}],rejected_lines=[2])))
    ]
    return run_cases(namespace, 'parse_json_lines', cases, mode)
