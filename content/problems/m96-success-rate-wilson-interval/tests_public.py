def run_tests(namespace, mode="all"):
    cases = [
        ('Balanced count', lambda f: assert_close(f(5,10,1.96), np.array([0.23658959361548731, 0.7634104063845126], dtype=float).reshape((2,)))),
        ('No successes', lambda f: assert_close(f(0,10,1.96), np.array([0.0, 0.2775401687666166], dtype=float).reshape((2,)))),
        ('All successes', lambda f: assert_close(f(10,10,1.96), np.array([0.7224598312333834, 1.0], dtype=float).reshape((2,)))),
        ('One trial', lambda f: assert_close(f(1,1,1), np.array([0.5, 1.0], dtype=float).reshape((2,)))),
        ('Large sample', lambda f: assert_close(f(700,1000,2), np.array([0.6702672528957491, 0.7281391216062428], dtype=float).reshape((2,)))),
        ('Narrow interval', lambda f: assert_close(f(4,10,.5), np.array([0.3258909520659746, 0.47898709671451334], dtype=float).reshape((2,)))),
        ('Reject impossible count', lambda f: rejects(f,11,10,2)),
        ('Reject no trials', lambda f: rejects(f,0,0,2)),
        ('Reject zero z', lambda f: rejects(f,1,2,0)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,5,10,1.96), np.array([0.23658959361548731, 0.7634104063845126], dtype=float).reshape((2,)))),
    ]
    return run_cases(namespace, 'wilson_interval', cases, mode)
