def run_tests(namespace, mode="all"):
    cases = [
        ('Slow return trip', lambda f: assert_close(f([20,60],10), {'segment_time':np.array([0.5, 0.16666666666666666], dtype=float).reshape((2,)),'total_time':0.6666666666666666,'mean_speed':30.0})),
        ('Equal speeds', lambda f: assert_close(f([4,4,4],2), {'segment_time':np.array([0.5, 0.5, 0.5], dtype=float).reshape((3,)),'total_time':1.5,'mean_speed':4.0})),
        ('One segment', lambda f: assert_close(f([3],9), {'segment_time':np.array([3.0], dtype=float).reshape((1,)),'total_time':3.0,'mean_speed':3.0})),
        ('Fractional speeds', lambda f: assert_close(f([.5,2],1), {'segment_time':np.array([2.0, 0.5], dtype=float).reshape((2,)),'total_time':2.5,'mean_speed':0.8})),
        ('Different distance', lambda f: assert_close(f([2,8],3), {'segment_time':np.array([1.5, 0.375], dtype=float).reshape((2,)),'total_time':1.875,'mean_speed':3.2})),
        ('Three rates', lambda f: assert_close(f([1,2,4],4), {'segment_time':np.array([4.0, 2.0, 1.0], dtype=float).reshape((3,)),'total_time':7.0,'mean_speed':1.7142857142857142})),
        ('Reject zero speed', lambda f: rejects(f,[1,0],2)),
        ('Reject negative distance', lambda f: rejects(f,[1,2],-1)),
        ('Reject tiny speed', lambda f: rejects(f,[1e-8],1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[20,60],10), {'segment_time':np.array([0.5, 0.16666666666666666], dtype=float).reshape((2,)),'total_time':0.6666666666666666,'mean_speed':30.0})),
    ]
    return run_cases(namespace, 'equal_distance_rates', cases, mode)
