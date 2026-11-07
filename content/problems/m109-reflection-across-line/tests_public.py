def run_tests(namespace, mode="all"):
    cases = [
        ('Reflect across x axis', lambda f: assert_close(f([[1,2],[-3,-4]],[0,1],0), np.array([[1.0, -2.0], [-3.0, 4.0]], dtype=float).reshape((2, 2)))),
        ('Reflect across shifted line', lambda f: assert_close(f([[0,0],[3,1]],[1,0],-1), np.array([[2.0, 0.0], [-1.0, 1.0]], dtype=float).reshape((2, 2)))),
        ('Diagonal mirror', lambda f: assert_close(f([[2,0],[1,3]],[1,-1],0), np.array([[0.0, 2.0], [3.0, 1.0]], dtype=float).reshape((2, 2)))),
        ('Points on mirror', lambda f: assert_close(f([[1,2],[1,7]],[1,0],-1), np.array([[1.0, 2.0], [1.0, 7.0]], dtype=float).reshape((2, 2)))),
        ('Normal rescaled', lambda f: assert_close(f([[2,0]],[2,-2],0), np.array([[0.0, 2.0]], dtype=float).reshape((1, 2)))),
        ('Oblique line', lambda f: assert_close(f([[0,0],[1,2]],[3,4],-5), np.array([[1.2000000000000002, 1.6], [-0.43999999999999995, 0.08000000000000007]], dtype=float).reshape((2, 2)))),
        ('Reject zero normal', lambda f: rejects(f,[[1,2]],[0,0],1)),
        ('Reject bad point rank', lambda f: rejects(f,[1,2],[1,0],0)),
        ('Reject wrong coordinates', lambda f: rejects(f,[[1,2,3]],[1,0],0)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[1,2],[-3,-4]],[0,1],0), np.array([[1.0, -2.0], [-3.0, 4.0]], dtype=float).reshape((2, 2)))),
    ]
    return run_cases(namespace, 'reflect_points', cases, mode)
