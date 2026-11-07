def run_tests(namespace, mode="all"):
    cases = [
        ('Sort object keys', lambda f: assert_close(f({'z':1,'a':2}), '{"a":2,"z":1}')),
        ('Nested sort', lambda f: assert_close(f({'x':{'b':2,'a':1}}), '{"x":{"a":1,"b":2}}')),
        ('Unicode preserved', lambda f: assert_close(f({'word':'café'}), '{"word":"café"}')),
        ('Empty array', lambda f: assert_close(f([]), '[]')),
        ('Primitive null', lambda f: assert_close(f(None), 'null')),
        ('Array order retained', lambda f: assert_close(f([2,1,True]), '[2,1,true]')),
        ('Reject nonfinite', lambda f: rejects(f, float("nan"))),
        ('Reject tuple array', lambda f: rejects(f, (1,2))),
        ('Reject nonstring key', lambda f: rejects(f, {1:"a"})),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, {'z':1,'a':2}), '{"a":2,"z":1}'))
    ]
    return run_cases(namespace, 'canonical_json', cases, mode)
