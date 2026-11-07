def run_tests(namespace, mode="all"):
    cases = [
        ('Split one bin', lambda f: assert_close(f([0,4],[8],[0,1,3,4]), np.array([2.0, 4.0, 2.0], dtype=float).reshape((3,)))),
        ('Merge bins', lambda f: assert_close(f([0,1,3],[2,6],[0,3]), np.array([8.0], dtype=float).reshape((1,)))),
        ('Cross old boundary', lambda f: assert_close(f([0,2,4],[2,6],[0,1,3,4]), np.array([1.0, 4.0, 3.0], dtype=float).reshape((3,)))),
        ('Extended range', lambda f: assert_close(f([1,2],[3],[0,1,2,3]), np.array([0.0, 3.0, 0.0], dtype=float).reshape((3,)))),
        ('Identity grid', lambda f: assert_close(f([0,1,2],[0,4],[0,1,2]), np.array([0.0, 4.0], dtype=float).reshape((2,)))),
        ('Uneven old widths', lambda f: assert_close(f([0,1,4],[3,3],[0,2,4]), np.array([4.0, 2.0], dtype=float).reshape((2,)))),
        ('Reject incomplete cover', lambda f: rejects(f,[0,2],[1],[0,1])),
        ('Reject wrong mass count', lambda f: rejects(f,[0,1,2],[1],[0,2])),
        ('Reject negative mass', lambda f: rejects(f,[0,1,2],[-1,2],[0,2])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,4],[8],[0,1,3,4]), np.array([2.0, 4.0, 2.0], dtype=float).reshape((3,)))),
    ]
    return run_cases(namespace, 'rebin_histogram', cases, mode)
