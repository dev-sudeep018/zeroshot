def run_tests(namespace, mode="all"):
    cases = [
        ('Integrate quadratic', lambda f: assert_close(f([3,2,1],[0,1],[1,2]), {'antiderivative':np.array([1.0, 1.0, 1.0, 0.0], dtype=float).reshape((4,)),'areas':np.array([3.0, 11.0], dtype=float).reshape((2,))})),
        ('Reversed bounds', lambda f: assert_close(f([2],[3],[1]), {'antiderivative':np.array([2.0, 0.0], dtype=float).reshape((2,)),'areas':np.array([-4.0], dtype=float).reshape((1,))})),
        ('Equal bounds', lambda f: assert_close(f([1,-2],[2],[2]), {'antiderivative':np.array([0.5, -2.0, 0.0], dtype=float).reshape((3,)),'areas':np.array([0.0], dtype=float).reshape((1,))})),
        ('Odd symmetric polynomial', lambda f: assert_close(f([1,0,0,0],[-2],[2]), {'antiderivative':np.array([0.25, 0.0, 0.0, 0.0, 0.0], dtype=float).reshape((5,)),'areas':np.array([0.0], dtype=float).reshape((1,))})),
        ('Zero polynomial', lambda f: assert_close(f([0],[-1,0],[2,4]), {'antiderivative':np.array([0.0, 0.0], dtype=float).reshape((2,)),'areas':np.array([0.0, 0.0], dtype=float).reshape((2,))})),
        ('Linear areas', lambda f: assert_close(f([2,0],[-1,0],[0,3]), {'antiderivative':np.array([1.0, 0.0, 0.0], dtype=float).reshape((3,)),'areas':np.array([-1.0, 9.0], dtype=float).reshape((2,))})),
        ('Reject shape mismatch', lambda f: rejects(f,[1],[0,1],[2])),
        ('Reject excess bounds', lambda f: rejects(f,[1],[0],[11])),
        ('Reject empty coefficients', lambda f: rejects(f,[],[0],[1])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[3,2,1],[0,1],[1,2]), {'antiderivative':np.array([1.0, 1.0, 1.0, 0.0], dtype=float).reshape((4,)),'areas':np.array([3.0, 11.0], dtype=float).reshape((2,))})),
    ]
    return run_cases(namespace, 'polynomial_integrals', cases, mode)
