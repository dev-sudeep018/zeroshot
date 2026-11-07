def run_tests(namespace, mode="all"):
    cases = [
        ('First coordinate update', lambda f: assert_close(f([[1,0],[1,1],[1,2]],[1,2,3],[0,0],0,1), np.array([1.5, 0.0], dtype=float).reshape((2,)))),
        ('Second coordinate update', lambda f: assert_close(f([[1,0],[1,1],[1,2]],[1,2,3],[1,0],1,0), np.array([1.0, 1.0], dtype=float).reshape((2,)))),
        ('Shrink one feature', lambda f: assert_close(f([[1],[2]],[2,4],[7],0,5), np.array([1.0], dtype=float).reshape((1,)))),
        ('Zero feature with penalty', lambda f: assert_close(f([[0],[0]],[1,2],[4],0,1), np.array([0.0], dtype=float).reshape((1,)))),
        ('Correlated columns', lambda f: assert_close(f([[1,2],[2,1],[3,2]],[1,4,5],[2,-1],1,.5), np.array([2.0, -0.42105263157894735], dtype=float).reshape((2,)))),
        ('Already optimum', lambda f: assert_close(f([[1],[2]],[2,4],[2],0,0), np.array([2.0], dtype=float).reshape((1,)))),
        ('Reject negative penalty', lambda f: rejects(f,[[1]],[1],[0],0,-1)),
        ('Reject zero denominator', lambda f: rejects(f,[[0]],[1],[0],0,0)),
        ('Reject coordinate range', lambda f: rejects(f,[[1]],[1],[0],1,0)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[1,0],[1,1],[1,2]],[1,2,3],[0,0],0,1), np.array([1.5, 0.0], dtype=float).reshape((2,)))),
    ]
    return run_cases(namespace, 'ridge_coordinate', cases, mode)
