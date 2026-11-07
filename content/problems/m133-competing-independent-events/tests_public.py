def run_tests(namespace, mode="all"):
    cases = [
        ('Three unequal events', lambda f: assert_close(f([.2,.5,.8]), {'counts':np.array([0.07999999999999999, 0.42000000000000004, 0.42000000000000004, 0.08000000000000002], dtype=float).reshape((4,)),'none':0.07999999999999999,'one':0.42000000000000004,'several':0.5})),
        ('Certain and impossible', lambda f: assert_close(f([1,0,1]), {'counts':np.array([0.0, 0.0, 1.0, 0.0], dtype=float).reshape((4,)),'none':0.0,'one':0.0,'several':1.0})),
        ('Single event', lambda f: assert_close(f([.3]), {'counts':np.array([0.7, 0.3], dtype=float).reshape((2,)),'none':0.7,'one':0.3,'several':0.0})),
        ('All impossible', lambda f: assert_close(f([0,0]), {'counts':np.array([1.0, 0.0, 0.0], dtype=float).reshape((3,)),'none':1.0,'one':0.0,'several':0.0})),
        ('Fair pair', lambda f: assert_close(f([.5,.5]), {'counts':np.array([0.25, 0.5, 0.25], dtype=float).reshape((3,)),'none':0.25,'one':0.5,'several':0.25})),
        ('Three rare events', lambda f: assert_close(f([.01,.02,.03]), {'counts':np.array([0.9410939999999999, 0.057817999999999994, 0.001082, 6e-06], dtype=float).reshape((4,)),'none':0.9410939999999999,'one':0.057817999999999994,'several':0.001088})),
        ('Reject negative probability', lambda f: rejects(f,[-.1])),
        ('Reject excess probability', lambda f: rejects(f,[1.1])),
        ('Reject mixed boolean values', lambda f: rejects(f,[True,.5])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[.2,.5,.8]), {'counts':np.array([0.07999999999999999, 0.42000000000000004, 0.42000000000000004, 0.08000000000000002], dtype=float).reshape((4,)),'none':0.07999999999999999,'one':0.42000000000000004,'several':0.5})),
    ]
    return run_cases(namespace, 'independent_event_counts', cases, mode)
