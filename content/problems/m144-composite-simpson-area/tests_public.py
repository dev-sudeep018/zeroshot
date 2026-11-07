def run_tests(namespace, mode="all"):
    cases = [
        ('Quadratic samples', lambda f: assert_close(f([0,1,4],1), 2.6666666666666665)),
        ('Cubic samples', lambda f: assert_close(f([0,1,8,27,64],1), 64.0)),
        ('Constant samples', lambda f: assert_close(f([3,3,3,3,3],.5), 6.0)),
        ('Signed cancellation', lambda f: assert_close(f([-1,0,1],1), 0.0)),
        ('Uneven values', lambda f: assert_close(f([2,-1,4,0,3],.25), 0.75)),
        ('Negative constant', lambda f: assert_close(f([-2,-2,-2],2), -8.0)),
        ('Reject even sample count', lambda f: rejects(f,[1,2,3,4],1)),
        ('Reject too few samples', lambda f: rejects(f,[1],1)),
        ('Reject nonpositive spacing', lambda f: rejects(f,[1,2,3],0)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,1,4],1), 2.6666666666666665)),
    ]
    return run_cases(namespace, 'simpson_samples', cases, mode)
