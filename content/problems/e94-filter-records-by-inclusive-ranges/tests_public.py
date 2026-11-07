def run_tests(namespace, mode="all"):
    cases = [
        ('Inclusive endpoints', lambda f: assert_close(f([{'x':0},{'x':1},{'x':2}], {'x':[0,1]}), [{'x':0},{'x':1}])),
        ('All constraints', lambda f: assert_close(f([{'x':1,'y':9},{'x':1,'y':2}], {'x':[0,2],'y':[1,3]}), [{'x':1,'y':2}])),
        ('Empty constraints', lambda f: assert_close(f([{'x':'a'},{}], {}), [{'x':'a'},{}])),
        ('No rows', lambda f: assert_close(f([], {'x':[0,1]}), [])),
        ('Exact bound', lambda f: assert_close(f([{'x':2},{'x':3}], {'x':[2,2]}), [{'x':2}])),
        ('Negative range', lambda f: assert_close(f([{'x':-2},{'x':0}], {'x':[-3,-1]}), [{'x':-2}])),
        ('Reject reversed bound', lambda f: rejects(f, [], {'x':[2,1]})),
        ('Reject missing field', lambda f: rejects(f, [{}], {'x':[0,1]})),
        ('Reject nonnumeric field', lambda f: rejects(f, [{'x':'1'}], {'x':[0,2]})),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'x':0},{'x':1},{'x':2}], {'x':[0,1]}), [{'x':0},{'x':1}]))
    ]
    return run_cases(namespace, 'filter_ranges', cases, mode)
