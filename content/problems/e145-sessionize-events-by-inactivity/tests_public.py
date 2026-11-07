def run_tests(namespace, mode="all"):
    cases = [
        ('Separate after inactivity', lambda f: assert_close(f([0,2,5,11,12],5), [[0,1,2],[3,4]])),
        ('Exact timeout stays', lambda f: assert_close(f([0,5,10],5), [[0,1,2]])),
        ('Zero timeout', lambda f: assert_close(f([1,1,2,2,3],0), [[0,1],[2,3],[4]])),
        ('Empty events', lambda f: assert_close(f([],3), [])),
        ('One event', lambda f: assert_close(f([-4],0), [[0]])),
        ('Negative times', lambda f: assert_close(f([-10,-9,0],2), [[0,1],[2]])),
        ('Reject unsorted', lambda f: rejects(f, [2,1],3)),
        ('Reject negative timeout', lambda f: rejects(f, [], -1)),
        ('Reject bool time', lambda f: rejects(f, [False],3)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [0,2,5,11,12],5), [[0,1,2],[3,4]]))
    ]
    return run_cases(namespace, 'sessionize', cases, mode)
