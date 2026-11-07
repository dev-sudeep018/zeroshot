def run_tests(namespace, mode="all"):
    cases = [
        ('One success in two trials', lambda f: assert_close(f(1,2,.5), np.log(.5))),
        ('Two successes in three trials', lambda f: assert_close(f(2,3,.5), np.log(3/8))),
        ('No successes', lambda f: assert_close(f(0,4,.5), np.log(1/16))),
        ('Certain absence', lambda f: assert_close(f(0,3,0), 0)),
        ('Certain success', lambda f: assert_close(f(3,3,1), 0)),
        ('No observations', lambda f: assert_close(f(0,0,.3), 0)),
        ('Reject impossible endpoint', lambda f: rejects(f,1,2,0)),
        ('Reject excessive successes', lambda f: rejects(f,3,2,.5)),
        ('Reject fractional trials', lambda f: rejects(f,1,2.5,.5)),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,2,3,.5),np.log(3/8))),
    ]
    return run_cases(namespace, 'binomial_log_likelihood', cases, mode)
