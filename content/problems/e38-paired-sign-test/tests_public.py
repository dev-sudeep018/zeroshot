def run_tests(namespace, mode="all"):
    cases = [
        ('Three consistent improvements', lambda f: assert_close(f([1,2,3]), dict(wins=3,losses=0,ties=0,p_value=.25))),
        ('Balanced signs', lambda f: assert_close(f([10,-1]), dict(wins=1,losses=1,ties=0,p_value=1.))),
        ('Ties do not count as trials', lambda f: assert_close(f([0,1,0,1]), dict(wins=2,losses=0,ties=2,p_value=.5))),
        ('No pairs', lambda f: assert_close(f([]), dict(wins=0,losses=0,ties=0,p_value=1.))),
        ('All ties', lambda f: assert_close(f([0,0]), dict(wins=0,losses=0,ties=2,p_value=1.))),
        ('Magnitude does not matter', lambda f: assert_close(f([-100,-.01,-3,-2]), dict(wins=0,losses=4,ties=0,p_value=.125))),
        ('Reject matrix', lambda f: rejects(f, [[1,2]])),
        ('Reject nonfinite difference', lambda f: rejects(f, [np.nan])),
        ('Reject too many pairs', lambda f: rejects(f, [1]*1001)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1,2,3]), dict(wins=3,losses=0,ties=0,p_value=.25)))
    ]
    return run_cases(namespace, 'paired_sign_test', cases, mode)
