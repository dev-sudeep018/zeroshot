def run_tests(namespace, mode="all"):
    cases = [
        ('Quarter turn around z', lambda f: assert_close(f([1,0,0],[0,0,1],np.pi/2), np.array([6.123233995736766e-17, 1.0, 0.0], dtype=float).reshape((3,)))),
        ('Along the axis', lambda f: assert_close(f([0,0,3],[0,0,2],1.2), np.array([0.0, 0.0, 3.0], dtype=float).reshape((3,)))),
        ('Half turn around x', lambda f: assert_close(f([1,2,3],[1,0,0],np.pi), np.array([1.0, -2.0000000000000004, -2.9999999999999996], dtype=float).reshape((3,)))),
        ('Zero angle', lambda f: assert_close(f([1,2,3],[1,1,1],0), np.array([1.0, 2.0, 3.0], dtype=float).reshape((3,)))),
        ('Reverse angle', lambda f: assert_close(f([1,0,0],[0,0,1],-np.pi/2), np.array([6.123233995736766e-17, -1.0, 0.0], dtype=float).reshape((3,)))),
        ('Oblique axis', lambda f: assert_close(f([1,0,0],[1,1,1],2*np.pi/3), np.array([2.220446049250313e-16, 1.0, -1.1102230246251565e-16], dtype=float).reshape((3,)))),
        ('Reject zero axis', lambda f: rejects(f,[1,2,3],[0,0,0],1)),
        ('Reject planar vector', lambda f: rejects(f,[1,2],[0,0,1],1)),
        ('Reject nonfinite angle', lambda f: rejects(f,[1,2,3],[1,0,0],np.nan)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,0,0],[0,0,1],np.pi/2), np.array([6.123233995736766e-17, 1.0, 0.0], dtype=float).reshape((3,)))),
    ]
    return run_cases(namespace, 'rotate_about_axis', cases, mode)
