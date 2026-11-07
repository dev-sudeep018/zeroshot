def run_tests(namespace, mode="all"):
    cases = [
        ('Missing and extra', lambda f: assert_close(f([['a','b'],[]], [['a'],['c']], ['a','b','c']), dict(missing=[1,0],extra=[0,1],total_errors=2,loss=1/3))),
        ('Exact agreement', lambda f: assert_close(f([['a']], [['a']], ['a','b']), dict(missing=[0],extra=[0],total_errors=0,loss=0.0))),
        ('Complete mismatch', lambda f: assert_close(f([['a']], [['b']], ['a','b']), dict(missing=[1],extra=[1],total_errors=2,loss=1.0))),
        ('No rows', lambda f: assert_close(f([], [], ['a']), dict(missing=[],extra=[],total_errors=0,loss=0.0))),
        ('Empty label sets', lambda f: assert_close(f([[]], [[]], ['a']), dict(missing=[0],extra=[0],total_errors=0,loss=0.0))),
        ('Vocabulary controls denominator', lambda f: assert_close(f([['a']], [[]], ['a','b','c','d']), dict(missing=[1],extra=[0],total_errors=1,loss=0.25))),
        ('Reject unknown label', lambda f: rejects(f, [['x']], [[]], ['a'])),
        ('Reject duplicate row label', lambda f: rejects(f, [['a','a']], [[]], ['a'])),
        ('Reject row mismatch', lambda f: rejects(f, [[]], [], ['a'])),
        ('Reject empty vocabulary', lambda f: rejects(f, [], [], [])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [['a','b'],[]], [['a'],['c']], ['a','b','c']), dict(missing=[1,0],extra=[0,1],total_errors=2,loss=1/3)))
    ]
    return run_cases(namespace, 'hamming_label_errors', cases, mode)
