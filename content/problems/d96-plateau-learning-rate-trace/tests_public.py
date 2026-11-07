def run_tests(namespace, mode="all"):
    cases = [
        ('Repeated plateaus', lambda f: assert_close(f([3,3,3,3,3],1,0.5,2,0.1), np.array([1.0, 1.0, 0.5, 0.5, 0.25], dtype='float64'))),
        ('Rate floor', lambda f: assert_close(f([2,2,2,2],0.4,0.5,1,0.15), np.array([0.4, 0.2, 0.15, 0.15], dtype='float64'))),
        ('Improvement resets', lambda f: assert_close(f([3,3,2,2,2],1,0.5,2,0), np.array([1.0, 1.0, 1.0, 1.0, 0.5], dtype='float64'))),
        ('No plateau', lambda f: assert_close(f([4,3,2],0.1,0.5,1,0), np.array([0.1, 0.1, 0.1], dtype='float64'))),
        ('Single epoch', lambda f: assert_close(f([1],0.2,0.8,3,0.01), np.array([0.2], dtype='float64'))),
        ('Zero rate', lambda f: assert_close(f([1,1],0,0.5,1,0), np.array([0.0, 0.0], dtype='float64'))),
        ('Reject invalid factor', lambda f: rejects(f, [1],0.1,1,2,0)),
        ('Reject floor exceeds rate', lambda f: rejects(f, [1],0.1,0.5,2,0.2)),
        ('Reject negative loss', lambda f: rejects(f, [-1],0.1,0.5,2,0)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [3,3,3,3,3],1,0.5,2,0.1), np.array([1.0, 1.0, 0.5, 0.5, 0.25], dtype='float64'))),
    ]
    return run_cases(namespace, 'plateau_rates', cases, mode)
