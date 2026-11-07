def run_tests(namespace, mode="all"):
    cases = [
        ('Two channels', lambda f: assert_close(f([[1,3],[5,-2]],[2,-1],[1,0],[0,-2],[8,2]), {'values':np.array([[3.0, -2.0], [8.0, 2.0]], dtype=float).reshape((2, 2)),'clipped':np.array([[False, True], [True, False]], dtype=bool).reshape((2, 2))})),
        ('Bounds are inclusive', lambda f: assert_close(f([[0,1]],[1,1],[0,0],[0,0],[1,1]), {'values':np.array([[0.0, 1.0]], dtype=float).reshape((1, 2)),'clipped':np.array([[False, False]], dtype=bool).reshape((1, 2))})),
        ('Negative gain', lambda f: assert_close(f([[1],[3]],[-2],[5],[0],[4]), {'values':np.array([[3.0], [0.0]], dtype=float).reshape((2, 1)),'clipped':np.array([[False], [True]], dtype=bool).reshape((2, 1))})),
        ('Constant channel', lambda f: assert_close(f([[8],[-3]],[0],[2],[0],[1]), {'values':np.array([[1.0], [1.0]], dtype=float).reshape((2, 1)),'clipped':np.array([[True], [True]], dtype=bool).reshape((2, 1))})),
        ('Single reading', lambda f: assert_close(f([[2]],[3],[-1],[-10],[10]), {'values':np.array([[5.0]], dtype=float).reshape((1, 1)),'clipped':np.array([[False]], dtype=bool).reshape((1, 1))})),
        ('Equal bounds', lambda f: assert_close(f([[2],[4]],[1],[0],[3],[3]), {'values':np.array([[3.0], [3.0]], dtype=float).reshape((2, 1)),'clipped':np.array([[True], [True]], dtype=bool).reshape((2, 1))})),
        ('Reject reversed bounds', lambda f: rejects(f,[[1]],[1],[0],[2],[1])),
        ('Reject channel mismatch', lambda f: rejects(f,[[1,2]],[1],[0],[0],[1])),
        ('Reject boolean data', lambda f: rejects(f,[[True]],[1],[0],[0],[2])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[1,3],[5,-2]],[2,-1],[1,0],[0,-2],[8,2]), {'values':np.array([[3.0, -2.0], [8.0, 2.0]], dtype=float).reshape((2, 2)),'clipped':np.array([[False, True], [True, False]], dtype=bool).reshape((2, 2))})),
    ]
    return run_cases(namespace, 'calibrate_channels', cases, mode)
