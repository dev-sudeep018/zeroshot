def run_tests(namespace, mode="all"):
    cases = [
        ('Estimate square root two', lambda f: assert_close(f(2,1,4), np.array([1.0, 1.5, 1.4166666666666665, 1.4142156862745097, 1.4142135623746899], dtype=float).reshape((5,)))),
        ('Already exact', lambda f: assert_close(f(9,3,3), np.array([3.0, 3.0, 3.0, 3.0], dtype=float).reshape((4,)))),
        ('Zero target', lambda f: assert_close(f(0,8,4), np.array([8.0, 4.0, 2.0, 1.0, 0.5], dtype=float).reshape((5,)))),
        ('No updates', lambda f: assert_close(f(4,7,0), np.array([7.0], dtype=float).reshape((1,)))),
        ('Small target', lambda f: assert_close(f(.01,1,5), np.array([1.0, 0.505, 0.2624009900990099, 0.15025530119986813, 0.10840434673026925, 0.10032578510960605], dtype=float).reshape((6,)))),
        ('Large initial guess', lambda f: assert_close(f(16,20,4), np.array([20.0, 10.4, 5.969230769230769, 4.324821570182395, 4.012198081555918], dtype=float).reshape((5,)))),
        ('Reject negative target', lambda f: rejects(f,-1,1,3)),
        ('Reject zero initial', lambda f: rejects(f,2,0,3)),
        ('Reject boolean steps', lambda f: rejects(f,2,1,True)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,2,1,4), np.array([1.0, 1.5, 1.4166666666666665, 1.4142156862745097, 1.4142135623746899], dtype=float).reshape((5,)))),
    ]
    return run_cases(namespace, 'newton_sqrt_trace', cases, mode)
