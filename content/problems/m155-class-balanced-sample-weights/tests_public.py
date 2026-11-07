def run_tests(namespace, mode="all"):
    cases = [
        ('Imbalanced binary classes', lambda f: assert_close(f([0,0,0,1],2), {'counts':np.array([3, 1], dtype=float).reshape((2,)),'weights':np.array([0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 2.0], dtype=float).reshape((4,))})),
        ('Balanced classes', lambda f: assert_close(f([0,1,2,0,1,2],3), {'counts':np.array([2, 2, 2], dtype=float).reshape((3,)),'weights':np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0], dtype=float).reshape((6,))})),
        ('One class', lambda f: assert_close(f([0,0,0],1), {'counts':np.array([3], dtype=float).reshape((1,)),'weights':np.array([1.0, 1.0, 1.0], dtype=float).reshape((3,))})),
        ('Unsorted labels', lambda f: assert_close(f([2,0,2,1,2,0],3), {'counts':np.array([2, 1, 3], dtype=float).reshape((3,)),'weights':np.array([0.6666666666666666, 1.0, 0.6666666666666666, 2.0, 0.6666666666666666, 1.0], dtype=float).reshape((6,))})),
        ('One sample per class', lambda f: assert_close(f([1,0],2), {'counts':np.array([1, 1], dtype=float).reshape((2,)),'weights':np.array([1.0, 1.0], dtype=float).reshape((2,))})),
        ('Minority middle class', lambda f: assert_close(f([0,0,1,2,2],3), {'counts':np.array([2, 1, 2], dtype=float).reshape((3,)),'weights':np.array([0.8333333333333334, 0.8333333333333334, 1.6666666666666667, 0.8333333333333334, 0.8333333333333334], dtype=float).reshape((5,))})),
        ('Reject missing class', lambda f: rejects(f,[0,0],2)),
        ('Reject negative label', lambda f: rejects(f,[-1,0],2)),
        ('Reject fractional label', lambda f: rejects(f,[0,.5],2)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,0,0,1],2), {'counts':np.array([3, 1], dtype=float).reshape((2,)),'weights':np.array([0.6666666666666666, 0.6666666666666666, 0.6666666666666666, 2.0], dtype=float).reshape((4,))})),
    ]
    return run_cases(namespace, 'balanced_sample_weights', cases, mode)
