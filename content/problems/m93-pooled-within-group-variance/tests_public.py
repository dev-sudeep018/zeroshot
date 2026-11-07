def run_tests(namespace, mode="all"):
    cases = [
        ('Unequal group sizes', lambda f: assert_close(f([3,5],[1,4]), {'variance':3.0,'degrees_freedom':6})),
        ('Equal sizes', lambda f: assert_close(f([4,4],[2,8]), {'variance':5.0,'degrees_freedom':6})),
        ('Zero variance group', lambda f: assert_close(f([2,3],[0,6]), {'variance':4.0,'degrees_freedom':3})),
        ('Single group', lambda f: assert_close(f([5],[3]), {'variance':3.0,'degrees_freedom':4})),
        ('Many groups', lambda f: assert_close(f([2,3,4],[1,2,3]), {'variance':2.3333333333333335,'degrees_freedom':6})),
        ('All zero', lambda f: assert_close(f([3,6],[0,0]), {'variance':0.0,'degrees_freedom':7})),
        ('Reject singleton group', lambda f: rejects(f,[1,3],[1,2])),
        ('Reject fractional size', lambda f: rejects(f,[2.5],[1])),
        ('Reject negative variance', lambda f: rejects(f,[2],[-1])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[3,5],[1,4]), {'variance':3.0,'degrees_freedom':6})),
    ]
    return run_cases(namespace, 'pooled_variance', cases, mode)
