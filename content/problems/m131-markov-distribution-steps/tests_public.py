def run_tests(namespace, mode="all"):
    cases = [
        ('Switching states', lambda f: assert_close(f([1,0],[[.8,.2],[.3,.7]],2), np.array([[1.0, 0.0], [0.8, 0.2], [0.7000000000000002, 0.30000000000000004]], dtype=float).reshape((3, 2)))),
        ('No transitions', lambda f: assert_close(f([.2,.8],[[1,0],[0,1]],0), np.array([[0.2, 0.8]], dtype=float).reshape((1, 2)))),
        ('Deterministic cycle', lambda f: assert_close(f([1,0,0],[[0,1,0],[0,0,1],[1,0,0]],3), np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0], [1.0, 0.0, 0.0]], dtype=float).reshape((4, 3)))),
        ('Absorbing state', lambda f: assert_close(f([1,0],[[.5,.5],[0,1]],3), np.array([[1.0, 0.0], [0.5, 0.5], [0.25, 0.75], [0.125, 0.875]], dtype=float).reshape((4, 2)))),
        ('One state', lambda f: assert_close(f([1],[[1]],4), np.array([[1.0], [1.0], [1.0], [1.0], [1.0]], dtype=float).reshape((5, 1)))),
        ('Stationary start', lambda f: assert_close(f([.6,.4],[[.8,.2],[.3,.7]],5), np.array([[0.6, 0.4], [0.6, 0.39999999999999997], [0.6, 0.39999999999999997], [0.6, 0.39999999999999997], [0.6, 0.39999999999999997], [0.6, 0.39999999999999997]], dtype=float).reshape((6, 2)))),
        ('Reject column-only stochastic', lambda f: rejects(f,[1,0],[[.5,.2],[.5,.8]],1)),
        ('Reject shape', lambda f: rejects(f,[1],[[1,0],[0,1]],1)),
        ('Reject negative steps', lambda f: rejects(f,[1],[[1]],-1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,0],[[.8,.2],[.3,.7]],2), np.array([[1.0, 0.0], [0.8, 0.2], [0.7000000000000002, 0.30000000000000004]], dtype=float).reshape((3, 2)))),
    ]
    return run_cases(namespace, 'markov_steps', cases, mode)
