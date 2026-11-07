def run_tests(namespace, mode="all"):
    cases = [
        ('Quadratic', lambda f: assert_close(f([2,-3,1],[-1,0,2]), {'value':np.array([6.0, 1.0, 3.0], dtype=float).reshape((3,)),'slope':np.array([-7.0, -3.0, 5.0], dtype=float).reshape((3,))})),
        ('Constant', lambda f: assert_close(f([7],[-3,2]), {'value':np.array([7.0, 7.0], dtype=float).reshape((2,)),'slope':np.array([0.0, 0.0], dtype=float).reshape((2,))})),
        ('Leading zeros', lambda f: assert_close(f([0,0,2,-1],[0,3]), {'value':np.array([-1.0, 5.0], dtype=float).reshape((2,)),'slope':np.array([2.0, 2.0], dtype=float).reshape((2,))})),
        ('Cubic', lambda f: assert_close(f([1,0,-2,3],[-2,1]), {'value':np.array([-1.0, 2.0], dtype=float).reshape((2,)),'slope':np.array([10.0, 1.0], dtype=float).reshape((2,))})),
        ('Zero polynomial', lambda f: assert_close(f([0],[2]), {'value':np.array([0.0], dtype=float).reshape((1,)),'slope':np.array([0.0], dtype=float).reshape((1,))})),
        ('Repeated queries', lambda f: assert_close(f([1,1],[2,2]), {'value':np.array([3.0, 3.0], dtype=float).reshape((2,)),'slope':np.array([1.0, 1.0], dtype=float).reshape((2,))})),
        ('Reject excessive degree', lambda f: rejects(f,[1]*11,[1])),
        ('Reject excessive point', lambda f: rejects(f,[1,2],[11])),
        ('Reject empty coefficients', lambda f: rejects(f,[],[0])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[2,-3,1],[-1,0,2]), {'value':np.array([6.0, 1.0, 3.0], dtype=float).reshape((3,)),'slope':np.array([-7.0, -3.0, 5.0], dtype=float).reshape((3,))})),
    ]
    return run_cases(namespace, 'horner_value_slope', cases, mode)
