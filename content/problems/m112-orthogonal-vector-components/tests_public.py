def run_tests(namespace, mode="all"):
    cases = [
        ('Horizontal direction', lambda f: assert_close(f([3,4],[1,0]), {'parallel':np.array([3.0, 0.0], dtype=float).reshape((2,)),'perpendicular':np.array([0.0, 4.0], dtype=float).reshape((2,)),'squared_lengths':np.array([9.0, 16.0], dtype=float).reshape((2,))})),
        ('Diagonal direction', lambda f: assert_close(f([2,0],[1,1]), {'parallel':np.array([1.0, 1.0], dtype=float).reshape((2,)),'perpendicular':np.array([1.0, -1.0], dtype=float).reshape((2,)),'squared_lengths':np.array([2.0, 2.0], dtype=float).reshape((2,))})),
        ('Already parallel', lambda f: assert_close(f([2,4],[1,2]), {'parallel':np.array([2.0, 4.0], dtype=float).reshape((2,)),'perpendicular':np.array([0.0, 0.0], dtype=float).reshape((2,)),'squared_lengths':np.array([20.0, 0.0], dtype=float).reshape((2,))})),
        ('Orthogonal vector', lambda f: assert_close(f([1,-1],[1,1]), {'parallel':np.array([0.0, 0.0], dtype=float).reshape((2,)),'perpendicular':np.array([1.0, -1.0], dtype=float).reshape((2,)),'squared_lengths':np.array([0.0, 2.0], dtype=float).reshape((2,))})),
        ('Three dimensions', lambda f: assert_close(f([1,2,3],[0,0,2]), {'parallel':np.array([0.0, 0.0, 3.0], dtype=float).reshape((3,)),'perpendicular':np.array([1.0, 2.0, 0.0], dtype=float).reshape((3,)),'squared_lengths':np.array([9.0, 5.0], dtype=float).reshape((2,))})),
        ('Zero vector', lambda f: assert_close(f([0,0],[1,2]), {'parallel':np.array([0.0, 0.0], dtype=float).reshape((2,)),'perpendicular':np.array([0.0, 0.0], dtype=float).reshape((2,)),'squared_lengths':np.array([0.0, 0.0], dtype=float).reshape((2,))})),
        ('Reject zero direction', lambda f: rejects(f,[1,2],[0,0])),
        ('Reject different lengths', lambda f: rejects(f,[1,2],[1])),
        ('Reject tiny direction', lambda f: rejects(f,[1,2],[1e-9,0])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[3,4],[1,0]), {'parallel':np.array([3.0, 0.0], dtype=float).reshape((2,)),'perpendicular':np.array([0.0, 4.0], dtype=float).reshape((2,)),'squared_lengths':np.array([9.0, 16.0], dtype=float).reshape((2,))})),
    ]
    return run_cases(namespace, 'orthogonal_components', cases, mode)
