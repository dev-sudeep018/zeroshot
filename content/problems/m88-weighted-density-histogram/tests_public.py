def run_tests(namespace, mode="all"):
    cases = [
        ('Uneven bin widths', lambda f: assert_close(f([0,1,2,4],[1,1,2,2],[0,1,4]), {'mass':np.array([0.16666666666666666, 0.8333333333333334], dtype=float).reshape((2,)),'density':np.array([0.16666666666666666, 0.2777777777777778], dtype=float).reshape((2,))})),
        ('Right endpoint', lambda f: assert_close(f([2],[3],[0,1,2]), {'mass':np.array([0.0, 1.0], dtype=float).reshape((2,)),'density':np.array([0.0, 1.0], dtype=float).reshape((2,))})),
        ('Zero weight', lambda f: assert_close(f([0,1],[0,2],[0,1,3]), {'mass':np.array([0.0, 1.0], dtype=float).reshape((2,)),'density':np.array([0.0, 0.5], dtype=float).reshape((2,))})),
        ('Single bin', lambda f: assert_close(f([1,2,3],[1,2,1],[0,4]), {'mass':np.array([1.0], dtype=float).reshape((1,)),'density':np.array([0.25], dtype=float).reshape((1,))})),
        ('Repeated edges values', lambda f: assert_close(f([1,1,2],[2,1,1],[0,1,2]), {'mass':np.array([0.0, 1.0], dtype=float).reshape((2,)),'density':np.array([0.0, 1.0], dtype=float).reshape((2,))})),
        ('Negative coordinates', lambda f: assert_close(f([-2,-1,0],[1,2,1],[-3,-1,1]), {'mass':np.array([0.25, 0.75], dtype=float).reshape((2,)),'density':np.array([0.125, 0.375], dtype=float).reshape((2,))})),
        ('Reject uncovered sample', lambda f: rejects(f,[3],[1],[0,2])),
        ('Reject zero weight total', lambda f: rejects(f,[1],[0],[0,2])),
        ('Reject repeated edge', lambda f: rejects(f,[1],[1],[0,1,1,2])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,1,2,4],[1,1,2,2],[0,1,4]), {'mass':np.array([0.16666666666666666, 0.8333333333333334], dtype=float).reshape((2,)),'density':np.array([0.16666666666666666, 0.2777777777777778], dtype=float).reshape((2,))})),
    ]
    return run_cases(namespace, 'weighted_density', cases, mode)
