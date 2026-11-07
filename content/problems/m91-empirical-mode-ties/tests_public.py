def run_tests(namespace, mode="all"):
    cases = [
        ('Single mode', lambda f: assert_close(f([2,1,2,3,2]), {'modes':np.array([2.0], dtype=float).reshape((1,)),'frequency':3,'unique':3})),
        ('Tied modes', lambda f: assert_close(f([3,1,3,1,2]), {'modes':np.array([1.0, 3.0], dtype=float).reshape((2,)),'frequency':2,'unique':3})),
        ('All unique', lambda f: assert_close(f([4,2,8]), {'modes':np.array([2.0, 4.0, 8.0], dtype=float).reshape((3,)),'frequency':1,'unique':3})),
        ('Constant sample', lambda f: assert_close(f([5,5,5]), {'modes':np.array([5.0], dtype=float).reshape((1,)),'frequency':3,'unique':1})),
        ('Negative values', lambda f: assert_close(f([-1,-2,-1,-2]), {'modes':np.array([-2.0, -1.0], dtype=float).reshape((2,)),'frequency':2,'unique':2})),
        ('Fractional repeats', lambda f: assert_close(f([.5,.25,.5]), {'modes':np.array([0.5], dtype=float).reshape((1,)),'frequency':2,'unique':2})),
        ('Reject empty', lambda f: rejects(f,[])),
        ('Reject booleans', lambda f: rejects(f,[True,False])),
        ('Reject nonfinite', lambda f: rejects(f,[1,np.inf])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[2,1,2,3,2]), {'modes':np.array([2.0], dtype=float).reshape((1,)),'frequency':3,'unique':3})),
    ]
    return run_cases(namespace, 'mode_summary', cases, mode)
