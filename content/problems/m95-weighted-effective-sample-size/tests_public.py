def run_tests(namespace, mode="all"):
    cases = [
        ('Uneven weights', lambda f: assert_close(f([1,2,3]), {'normalized':np.array([0.16666666666666666, 0.3333333333333333, 0.5], dtype=float).reshape((3,)),'effective_size':2.5714285714285716,'largest_share':0.5})),
        ('Equal weights', lambda f: assert_close(f([4,4,4,4]), {'normalized':np.array([0.25, 0.25, 0.25, 0.25], dtype=float).reshape((4,)),'effective_size':4.0,'largest_share':0.25})),
        ('One active weight', lambda f: assert_close(f([0,7,0]), {'normalized':np.array([0.0, 1.0, 0.0], dtype=float).reshape((3,)),'effective_size':1.0,'largest_share':1.0})),
        ('Single weight', lambda f: assert_close(f([3]), {'normalized':np.array([1.0], dtype=float).reshape((1,)),'effective_size':1.0,'largest_share':1.0})),
        ('Scaled weights', lambda f: assert_close(f([10,20,30]), {'normalized':np.array([0.16666666666666666, 0.3333333333333333, 0.5], dtype=float).reshape((3,)),'effective_size':2.5714285714285716,'largest_share':0.5})),
        ('Sparse weights', lambda f: assert_close(f([1,0,1,0]), {'normalized':np.array([0.5, 0.0, 0.5, 0.0], dtype=float).reshape((4,)),'effective_size':2.0,'largest_share':0.5})),
        ('Reject no mass', lambda f: rejects(f,[0,0])),
        ('Reject negative', lambda f: rejects(f,[-1,2])),
        ('Reject empty', lambda f: rejects(f,[])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,2,3]), {'normalized':np.array([0.16666666666666666, 0.3333333333333333, 0.5], dtype=float).reshape((3,)),'effective_size':2.5714285714285716,'largest_share':0.5})),
    ]
    return run_cases(namespace, 'weight_effective_size', cases, mode)
