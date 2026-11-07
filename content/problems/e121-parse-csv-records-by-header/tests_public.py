def run_tests(namespace, mode="all"):
    cases = [
        ('Quoted comma', lambda f: assert_close(f('name,note\nAda,"x,y"\n'), [{'name':'Ada','note':'x,y'}])),
        ('Quoted newline', lambda f: assert_close(f('x\n"a\nb"\n'), [{'x':'a\nb'}])),
        ('Escaped quote', lambda f: assert_close(f('x\n"a""b"\n'), [{'x':'a"b'}])),
        ('Header only', lambda f: assert_close(f('x,y\n'), [])),
        ('Empty cell', lambda f: assert_close(f('x,y\n,2\n'), [{'x':'','y':'2'}])),
        ('String numeric cell', lambda f: assert_close(f('x\n001\n'), [{'x':'001'}])),
        ('Reject duplicate header', lambda f: rejects(f, 'x,x\n1,2')),
        ('Reject ragged row', lambda f: rejects(f, 'x,y\n1')),
        ('Reject unterminated quote', lambda f: rejects(f, 'x\n"a')),
        ('Reject empty input', lambda f: rejects(f, '')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, 'name,note\nAda,"x,y"\n'), [{'name':'Ada','note':'x,y'}]))
    ]
    return run_cases(namespace, 'parse_csv_records', cases, mode)
