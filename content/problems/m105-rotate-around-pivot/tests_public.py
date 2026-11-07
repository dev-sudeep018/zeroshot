def run_tests(namespace, mode="all"):
    cases = [
        ('Quarter turn', lambda f: assert_close(f([[1,0],[0,1]],[0,0],np.pi/2), np.array([[6.123233995736766e-17, 1.0], [-1.0, 6.123233995736766e-17]], dtype=float).reshape((2, 2)))),
        ('Around shifted pivot', lambda f: assert_close(f([[3,1],[2,2]],[2,1],np.pi), np.array([[1.0, 1.0000000000000002], [1.9999999999999998, 0.0]], dtype=float).reshape((2, 2)))),
        ('No rotation', lambda f: assert_close(f([[2,-1],[-3,4]],[1,1],0), np.array([[2.0, -1.0], [-3.0, 4.0]], dtype=float).reshape((2, 2)))),
        ('Clockwise rotation', lambda f: assert_close(f([[1,0]],[0,0],-np.pi/2), np.array([[6.123233995736766e-17, -1.0]], dtype=float).reshape((1, 2)))),
        ('Pivot stays fixed', lambda f: assert_close(f([[3,4]],[3,4],.7), np.array([[3.0, 4.0]], dtype=float).reshape((1, 2)))),
        ('Oblique turn', lambda f: assert_close(f([[2,1],[0,-1]],[1,0],np.pi/4), np.array([[1.0, 1.4142135623730951], [1.0, -1.4142135623730951]], dtype=float).reshape((2, 2)))),
        ('Reject nonplanar', lambda f: rejects(f,[[1,2,3]],[0,0],1)),
        ('Reject bad pivot', lambda f: rejects(f,[[1,2]],[0],1)),
        ('Reject nonfinite angle', lambda f: rejects(f,[[1,2]],[0,0],np.inf)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[1,0],[0,1]],[0,0],np.pi/2), np.array([[6.123233995736766e-17, 1.0], [-1.0, 6.123233995736766e-17]], dtype=float).reshape((2, 2)))),
    ]
    return run_cases(namespace, 'rotate_points', cases, mode)
