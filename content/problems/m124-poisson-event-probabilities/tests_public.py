def run_tests(namespace, mode="all"):
    cases = [
        ('Rate two', lambda f: assert_close(f(2,[0,1,2,3]), {'probabilities':np.array([0.1353352832366127, 0.2706705664732254, 0.27067056647322546, 0.18044704431548347], dtype=float).reshape((4,)),'mean':2.0})),
        ('Rare events', lambda f: assert_close(f(.1,[0,1,2]), {'probabilities':np.array([0.9048374180359595, 0.09048374180359597, 0.004524187090179805], dtype=float).reshape((3,)),'mean':0.1})),
        ('Repeated requests', lambda f: assert_close(f(3,[2,0,2]), {'probabilities':np.array([0.22404180765538786, 0.049787068367863944, 0.22404180765538786], dtype=float).reshape((3,)),'mean':3.0})),
        ('Large counts', lambda f: assert_close(f(100,[90,100]), {'probabilities':np.array([0.02503894462302893, 0.03986099680914883], dtype=float).reshape((2,)),'mean':100.0})),
        ('Tiny rate', lambda f: assert_close(f(.000001,[0,1]), {'probabilities':np.array([0.9999990000005, 9.999990000005012e-07], dtype=float).reshape((2,)),'mean':1e-06})),
        ('Single request', lambda f: assert_close(f(1,[4]), {'probabilities':np.array([0.015328310048810101], dtype=float).reshape((1,)),'mean':1.0})),
        ('Reject zero rate', lambda f: rejects(f,0,[0])),
        ('Reject fractional count', lambda f: rejects(f,2,[1.5])),
        ('Reject excess rate', lambda f: rejects(f,101,[2])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,2,[0,1,2,3]), {'probabilities':np.array([0.1353352832366127, 0.2706705664732254, 0.27067056647322546, 0.18044704431548347], dtype=float).reshape((4,)),'mean':2.0})),
    ]
    return run_cases(namespace, 'poisson_counts', cases, mode)
