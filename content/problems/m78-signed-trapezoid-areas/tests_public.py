def run_tests(namespace, mode="all"):
    cases = [
        ('Uneven grid', lambda f: assert_close(f([0,1,3],[0,2,2]), {'area':np.array([1.0, 4.0], dtype=float).reshape((2,)),'cumulative':np.array([0.0, 1.0, 5.0], dtype=float).reshape((3,))})),
        ('Signed cancellation', lambda f: assert_close(f([0,1,2],[-1,0,1]), {'area':np.array([-0.5, 0.5], dtype=float).reshape((2,)),'cumulative':np.array([0.0, -0.5, 0.0], dtype=float).reshape((3,))})),
        ('Constant signal', lambda f: assert_close(f([1,3,6],[2,2,2]), {'area':np.array([4.0, 6.0], dtype=float).reshape((2,)),'cumulative':np.array([0.0, 4.0, 10.0], dtype=float).reshape((3,))})),
        ('One trapezoid', lambda f: assert_close(f([0,4],[1,3]), {'area':np.array([8.0], dtype=float).reshape((1,)),'cumulative':np.array([0.0, 8.0], dtype=float).reshape((2,))})),
        ('Negative times', lambda f: assert_close(f([-3,-1,0],[1,2,0]), {'area':np.array([3.0, 1.0], dtype=float).reshape((2,)),'cumulative':np.array([0.0, 3.0, 4.0], dtype=float).reshape((3,))})),
        ('Zero signal', lambda f: assert_close(f([0,.5,2],[0,0,0]), {'area':np.array([0.0, 0.0], dtype=float).reshape((2,)),'cumulative':np.array([0.0, 0.0, 0.0], dtype=float).reshape((3,))})),
        ('Reject repeated time', lambda f: rejects(f,[0,0],[1,2])),
        ('Reject unequal lengths', lambda f: rejects(f,[0,1],[1])),
        ('Reject descending grid', lambda f: rejects(f,[2,1],[3,4])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,1,3],[0,2,2]), {'area':np.array([1.0, 4.0], dtype=float).reshape((2,)),'cumulative':np.array([0.0, 1.0, 5.0], dtype=float).reshape((3,))})),
    ]
    return run_cases(namespace, 'trapezoid_integral', cases, mode)
