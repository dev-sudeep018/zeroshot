def run_tests(namespace, mode="all"):
    cases = [
        ('Across box', lambda f: assert_close(f([-1,1],[3,1],[0,0],[2,2]), {'visible':True,'parameters':np.array([0.25, 0.75], dtype=float).reshape((2,)),'points':np.array([[0.0, 1.0], [2.0, 1.0]], dtype=float).reshape((2, 2))})),
        ('Outside parallel', lambda f: assert_close(f([-1,3],[3,3],[0,0],[2,2]), {'visible':False,'parameters':np.array([0.0, 0.0], dtype=float).reshape((2,)),'points':np.array([[0.0, 0.0], [0.0, 0.0]], dtype=float).reshape((2, 2))})),
        ('Inside point', lambda f: assert_close(f([1,1],[1,1],[0,0],[2,2]), {'visible':True,'parameters':np.array([0.0, 1.0], dtype=float).reshape((2,)),'points':np.array([[1.0, 1.0], [1.0, 1.0]], dtype=float).reshape((2, 2))})),
        ('Corner contact', lambda f: assert_close(f([-1,1],[1,-1],[0,0],[2,2]), {'visible':True,'parameters':np.array([0.5, 0.5], dtype=float).reshape((2,)),'points':np.array([[0.0, 0.0], [0.0, 0.0]], dtype=float).reshape((2, 2))})),
        ('Entirely inside', lambda f: assert_close(f([.5,.5],[1,1],[0,0],[2,2]), {'visible':True,'parameters':np.array([0.0, 1.0], dtype=float).reshape((2,)),'points':np.array([[0.5, 0.5], [1.0, 1.0]], dtype=float).reshape((2, 2))})),
        ('Zero-width box', lambda f: assert_close(f([-1,1],[1,1],[0,0],[0,2]), {'visible':True,'parameters':np.array([0.5, 0.5], dtype=float).reshape((2,)),'points':np.array([[0.0, 1.0], [0.0, 1.0]], dtype=float).reshape((2, 2))})),
        ('Reject reversed bounds', lambda f: rejects(f,[0,0],[1,1],[2,0],[1,2])),
        ('Reject bad endpoint', lambda f: rejects(f,[0],[1,1],[0,0],[2,2])),
        ('Reject nonfinite', lambda f: rejects(f,[0,0],[np.inf,1],[0,0],[2,2])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[-1,1],[3,1],[0,0],[2,2]), {'visible':True,'parameters':np.array([0.25, 0.75], dtype=float).reshape((2,)),'points':np.array([[0.0, 1.0], [2.0, 1.0]], dtype=float).reshape((2, 2))})),
    ]
    return run_cases(namespace, 'clip_segment_box', cases, mode)
