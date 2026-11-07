def run_tests(namespace, mode="all"):
    cases = [
        ('Interior projection', lambda f: assert_close(f([1,3],[0,0],[4,0]), {'parameter':0.25,'point':np.array([1.0, 0.0], dtype=float).reshape((2,)),'squared_distance':9.0})),
        ('Beyond end', lambda f: assert_close(f([5,2],[0,0],[3,0]), {'parameter':1.0,'point':np.array([3.0, 0.0], dtype=float).reshape((2,)),'squared_distance':8.0})),
        ('Degenerate segment', lambda f: assert_close(f([3,4],[1,1],[1,1]), {'parameter':0.0,'point':np.array([1.0, 1.0], dtype=float).reshape((2,)),'squared_distance':13.0})),
        ('Before start', lambda f: assert_close(f([-2,1],[0,0],[4,0]), {'parameter':0.0,'point':np.array([0.0, 0.0], dtype=float).reshape((2,)),'squared_distance':5.0})),
        ('Diagonal segment', lambda f: assert_close(f([2,0],[0,0],[2,2]), {'parameter':0.5,'point':np.array([1.0, 1.0], dtype=float).reshape((2,)),'squared_distance':2.0})),
        ('Point on segment', lambda f: assert_close(f([1,1],[0,0],[3,3]), {'parameter':0.3333333333333333,'point':np.array([1.0, 1.0], dtype=float).reshape((2,)),'squared_distance':0.0})),
        ('Reject wrong dimension', lambda f: rejects(f,[1,2,3],[0,0],[1,1])),
        ('Reject nonfinite', lambda f: rejects(f,[np.nan,0],[0,0],[1,1])),
        ('Reject booleans', lambda f: rejects(f,[True,0],[0,0],[1,1])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,3],[0,0],[4,0]), {'parameter':0.25,'point':np.array([1.0, 0.0], dtype=float).reshape((2,)),'squared_distance':9.0})),
    ]
    return run_cases(namespace, 'nearest_on_segment', cases, mode)
