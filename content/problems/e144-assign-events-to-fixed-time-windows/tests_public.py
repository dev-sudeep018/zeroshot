def run_tests(namespace, mode="all"):
    cases = [
        ('Boundary belongs to next window', lambda f: assert_close(f([0,9,10,19,20],10,0), [[0,2],[10,2],[20,1]])),
        ('Negative offsets', lambda f: assert_close(f([-11,-10,-1,0],10,0), [[-20,1],[-10,2],[0,1]])),
        ('Shifted origin', lambda f: assert_close(f([2,3,7,8],5,3), [[-2,1],[3,2],[8,1]])),
        ('No events', lambda f: assert_close(f([],5,0), [])),
        ('Unsorted repeats', lambda f: assert_close(f([7,1,7,1],3,0), [[0,2],[6,2]])),
        ('Unit windows', lambda f: assert_close(f([-1,0,1],1,0), [[-1,1],[0,1],[1,1]])),
        ('Reject zero width', lambda f: rejects(f, [],0,0)),
        ('Reject fractional time', lambda f: rejects(f, [1.5],2,0)),
        ('Reject bool origin', lambda f: rejects(f, [],2,True)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [0,9,10,19,20],10,0), [[0,2],[10,2],[20,1]]))
    ]
    return run_cases(namespace, 'fixed_windows', cases, mode)
