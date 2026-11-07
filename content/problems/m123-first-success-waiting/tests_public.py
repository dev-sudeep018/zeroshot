def run_tests(namespace, mode="all"):
    cases = [
        ('Changing rates', lambda f: assert_close(f([.2,.5,.25]), {'first':np.array([0.2, 0.4, 0.1], dtype=float).reshape((3,)),'none':0.30000000000000004})),
        ('Certain later success', lambda f: assert_close(f([0,1,.5]), {'first':np.array([0.0, 1.0, 0.0], dtype=float).reshape((3,)),'none':0.0})),
        ('All fail', lambda f: assert_close(f([0,0,0]), {'first':np.array([0.0, 0.0, 0.0], dtype=float).reshape((3,)),'none':1.0})),
        ('Certain first trial', lambda f: assert_close(f([1,.5]), {'first':np.array([1.0, 0.0], dtype=float).reshape((2,)),'none':0.0})),
        ('One trial', lambda f: assert_close(f([.3]), {'first':np.array([0.3], dtype=float).reshape((1,)),'none':0.7})),
        ('Repeated rate', lambda f: assert_close(f([.5,.5,.5,.5]), {'first':np.array([0.5, 0.25, 0.125, 0.0625], dtype=float).reshape((4,)),'none':0.0625})),
        ('Reject negative rate', lambda f: rejects(f,[-.1,.5])),
        ('Reject rate above one', lambda f: rejects(f,[1.1])),
        ('Reject empty trials', lambda f: rejects(f,[])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[.2,.5,.25]), {'first':np.array([0.2, 0.4, 0.1], dtype=float).reshape((3,)),'none':0.30000000000000004})),
    ]
    return run_cases(namespace, 'first_success', cases, mode)
