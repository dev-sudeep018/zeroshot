def run_tests(namespace, mode="all"):
    cases = [
        ('Cooling toward room temperature', lambda f: assert_close(f(100,20,.5,1,3), np.array([100.0, 60.0, 40.0, 30.0], dtype=float).reshape((4,)))),
        ('Warming from below', lambda f: assert_close(f(0,20,.25,1,4), np.array([0.0, 5.0, 8.75, 11.5625, 13.671875], dtype=float).reshape((5,)))),
        ('No cooling', lambda f: assert_close(f(30,20,0,1,3), np.array([30.0, 30.0, 30.0, 30.0], dtype=float).reshape((4,)))),
        ('Full relaxation step', lambda f: assert_close(f(100,20,1,1,2), np.array([100.0, 20.0, 20.0], dtype=float).reshape((3,)))),
        ('Already ambient', lambda f: assert_close(f(20,20,.5,1,4), np.array([20.0, 20.0, 20.0, 20.0, 20.0], dtype=float).reshape((5,)))),
        ('No time steps', lambda f: assert_close(f(30,10,.1,.5,0), np.array([30.0], dtype=float).reshape((1,)))),
        ('Reject negative rate', lambda f: rejects(f,30,20,-1,1,2)),
        ('Reject unstable step', lambda f: rejects(f,30,20,2,1,2)),
        ('Reject zero step size', lambda f: rejects(f,30,20,1,0,2)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,100,20,.5,1,3), np.array([100.0, 60.0, 40.0, 30.0], dtype=float).reshape((4,)))),
    ]
    return run_cases(namespace, 'cooling_euler', cases, mode)
