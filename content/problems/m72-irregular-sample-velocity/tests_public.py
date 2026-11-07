def run_tests(namespace, mode="all"):
    cases = [
        ('Uneven steps', lambda f: assert_close(f([0,1,3],[0,2,8]), {'time':np.array([0.5, 2.0], dtype=float).reshape((2,)),'velocity':np.array([2.0, 3.0], dtype=float).reshape((2,))})),
        ('Stationary', lambda f: assert_close(f([0,2,5],[4,4,4]), {'time':np.array([1.0, 3.5], dtype=float).reshape((2,)),'velocity':np.array([0.0, 0.0], dtype=float).reshape((2,))})),
        ('Reverse motion', lambda f: assert_close(f([1,2,4],[5,3,-1]), {'time':np.array([1.5, 3.0], dtype=float).reshape((2,)),'velocity':np.array([-2.0, -2.0], dtype=float).reshape((2,))})),
        ('One interval', lambda f: assert_close(f([0,4],[2,10]), {'time':np.array([2.0], dtype=float).reshape((1,)),'velocity':np.array([2.0], dtype=float).reshape((1,))})),
        ('Negative timestamps', lambda f: assert_close(f([-3,-1,2],[1,3,9]), {'time':np.array([-2.0, 0.5], dtype=float).reshape((2,)),'velocity':np.array([1.0, 2.0], dtype=float).reshape((2,))})),
        ('Different speeds', lambda f: assert_close(f([0,.5,2],[0,1,1]), {'time':np.array([0.25, 1.25], dtype=float).reshape((2,)),'velocity':np.array([2.0, 0.0], dtype=float).reshape((2,))})),
        ('Reject duplicate time', lambda f: rejects(f,[0,0],[1,2])),
        ('Reject unequal length', lambda f: rejects(f,[0,1],[2])),
        ('Reject tiny gap', lambda f: rejects(f,[0,1e-8],[0,1])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,1,3],[0,2,8]), {'time':np.array([0.5, 2.0], dtype=float).reshape((2,)),'velocity':np.array([2.0, 3.0], dtype=float).reshape((2,))})),
    ]
    return run_cases(namespace, 'interval_velocities', cases, mode)
