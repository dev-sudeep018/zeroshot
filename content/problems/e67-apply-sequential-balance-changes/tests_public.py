def run_tests(namespace, mode="all"):
    cases = [
        ('Rejected withdrawal', lambda f: assert_close(f(5, [-3,-4,2]), dict(balances=[2,2,4],accepted=[True,False,True]))),
        ('Exact withdrawal', lambda f: assert_close(f(5, [-5]), dict(balances=[0],accepted=[True]))),
        ('Zero change', lambda f: assert_close(f(0, [0]), dict(balances=[0],accepted=[True]))),
        ('No changes', lambda f: assert_close(f(2, []), dict(balances=[],accepted=[]))),
        ('Deposit then withdrawal', lambda f: assert_close(f(0, [2,-1]), dict(balances=[2,1],accepted=[True,True]))),
        ('Rejected then deposit', lambda f: assert_close(f(0, [-1,3]), dict(balances=[0,3],accepted=[False,True]))),
        ('Reject negative initial', lambda f: rejects(f, -1, [])),
        ('Reject boolean change', lambda f: rejects(f, 0, [True])),
        ('Reject fractional initial', lambda f: rejects(f, 0.5, [])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, 5, [-3,-4,2]), dict(balances=[2,2,4],accepted=[True,False,True])))
    ]
    return run_cases(namespace, 'balance_trace', cases, mode)
