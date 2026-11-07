def run_tests(namespace, mode="all"):
    cases = [
        ('Column order', lambda f: assert_close(f([{'a':'1','b':'2'}], ['b','a']), 'b,a\n2,1\n')),
        ('Quoted comma', lambda f: assert_close(f([{'x':'a,b'}], ['x']), 'x\n"a,b"\n')),
        ('Embedded quote', lambda f: assert_close(f([{'x':'a"b'}], ['x']), 'x\n"a""b"\n')),
        ('No records', lambda f: assert_close(f([], ['x']), 'x\n')),
        ('Single empty cell', lambda f: assert_close(f([{'x':''}], ['x']), 'x\n""\n')),
        ('Embedded newline', lambda f: assert_close(f([{'x':'a\nb'}], ['x']), 'x\n"a\nb"\n')),
        ('Reject missing cell', lambda f: rejects(f, [{}], ['x'])),
        ('Reject numeric cell', lambda f: rejects(f, [{'x':1}], ['x'])),
        ('Reject duplicate field', lambda f: rejects(f, [], ['x','x'])),
        ('Reject empty schema', lambda f: rejects(f, [], [])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'a':'1','b':'2'}], ['b','a']), 'b,a\n2,1\n'))
    ]
    return run_cases(namespace, 'serialize_csv_records', cases, mode)
