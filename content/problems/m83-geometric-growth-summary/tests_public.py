def run_tests(namespace, mode="all"):
    cases = [
        ('Growth then decline', lambda f: assert_close(f([1.2,.5,2]), {'geometric_mean':1.0626585691826111,'cumulative':np.array([1.2, 0.6, 1.2], dtype=float).reshape((3,))})),
        ('No change', lambda f: assert_close(f([1,1,1]), {'geometric_mean':1.0,'cumulative':np.array([1.0, 1.0, 1.0], dtype=float).reshape((3,))})),
        ('Opposite scales', lambda f: assert_close(f([.01,100]), {'geometric_mean':1.0000000000000004,'cumulative':np.array([0.010000000000000004, 1.0000000000000009], dtype=float).reshape((2,))})),
        ('Single factor', lambda f: assert_close(f([3]), {'geometric_mean':3.0000000000000004,'cumulative':np.array([3.0000000000000004], dtype=float).reshape((1,))})),
        ('Small factors', lambda f: assert_close(f([.1,.2,.5]), {'geometric_mean':0.2154434690031884,'cumulative':np.array([0.10000000000000002, 0.02000000000000001, 0.010000000000000004], dtype=float).reshape((3,))})),
        ('Repeated growth', lambda f: assert_close(f([2,2,2,2]), {'geometric_mean':2.0,'cumulative':np.array([2.0, 4.0, 7.999999999999998, 15.999999999999998], dtype=float).reshape((4,))})),
        ('Reject zero', lambda f: rejects(f,[1,0])),
        ('Reject negative', lambda f: rejects(f,[-1,2])),
        ('Reject tiny factor', lambda f: rejects(f,[1e-8])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1.2,.5,2]), {'geometric_mean':1.0626585691826111,'cumulative':np.array([1.2, 0.6, 1.2], dtype=float).reshape((3,))})),
    ]
    return run_cases(namespace, 'growth_summary', cases, mode)
