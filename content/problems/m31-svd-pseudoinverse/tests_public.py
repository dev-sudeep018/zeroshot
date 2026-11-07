def run_tests(namespace, mode="all"):
    cases = [
        ('Diagonal inverse', lambda f: assert_close(f([[2,0],[0,4]]), np.diag([.5,.25]))),
        ('Rank deficient', lambda f: assert_close(f([[1,2],[2,4]]), np.array([[1,2],[2,4]])/25)),
        ('Wide matrix', lambda f: assert_close(f([[1,0,0],[0,2,0]]), np.array([[1.,0],[0,.5],[0,0]]))),
        ('Zero matrix', lambda f: assert_close(f([[0,0]]), np.zeros((2,1)))),
        ('Cut off small direction', lambda f: assert_close(f([[4,0],[0,1]],.3), np.diag([.25,0]))),
        ('Strict cutoff boundary', lambda f: assert_close(f([[4,0],[0,1]],.25), np.diag([.25,0]))),
        ('Reject negative cutoff', lambda f: rejects(f,[[1]],-.1)),
        ('Reject matrix rank', lambda f: rejects(f,[1,2],.1)),
        ('Reject nonfinite input', lambda f: rejects(f,[[np.nan]],.1)),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[2.,0],[0,4.]])),np.diag([.5,.25]))),
        ('Reject nonfinite inverse range', lambda f: rejects(f,[[1e-320]],0)),
    ]
    return run_cases(namespace, 'svd_pseudoinverse', cases, mode)
