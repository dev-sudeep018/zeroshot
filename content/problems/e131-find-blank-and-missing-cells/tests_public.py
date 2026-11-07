def run_tests(namespace, mode="all"):
    cases = [
        ('Three missingness reasons', lambda f: assert_close(f([{}, {'x':None},{'x':'  '}], ['x']), [[0,'x','missing'],[1,'x','null'],[2,'x','blank']])),
        ('Falsy data retained', lambda f: assert_close(f([{'a':0,'b':False,'c':[]}], ['a','b','c']), [])),
        ('Field order', lambda f: assert_close(f([{}], ['b','a']), [[0,'b','missing'],[0,'a','missing']])),
        ('No rows', lambda f: assert_close(f([], ['x']), [])),
        ('Nonblank string', lambda f: assert_close(f([{'x':' 0 '}], ['x']), [])),
        ('Unicode whitespace', lambda f: assert_close(f([{'x':'\u2003'}], ['x']), [[0,'x','blank']])),
        ('Reject duplicate field', lambda f: rejects(f, [], ['x','x'])),
        ('Reject nonrecord row', lambda f: rejects(f, [1], ['x'])),
        ('Reject empty field', lambda f: rejects(f, [], [''])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{}, {'x':None},{'x':'  '}], ['x']), [[0,'x','missing'],[1,'x','null'],[2,'x','blank']]))
    ]
    return run_cases(namespace, 'blank_cells', cases, mode)
