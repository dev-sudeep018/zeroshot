def run_tests(namespace, mode="all"):
    cases = [
        ('Partial overlap', lambda f: assert_close(f([[0,0,2,2]], [[1,1,3,3]]), np.array([[1/7]]))),
        ('Identical boxes', lambda f: assert_close(f([[0,0,1,1]], [[0,0,1,1]]), np.array([[1.]]))),
        ('Touching edges', lambda f: assert_close(f([[0,0,1,1]], [[1,0,2,1]]), np.array([[0.]]))),
        ('Contained box', lambda f: assert_close(f([[0,0,4,4]], [[1,1,2,2]]), np.array([[1/16]]))),
        ('Degenerate union', lambda f: assert_close(f([[0,0,0,0]], [[0,0,0,0]]), np.array([[0.]]))),
        ('Pairwise matrix', lambda f: assert_close(f([[0,0,1,1],[2,2,3,3]], [[0,0,1,1]]), np.array([[1.],[0.]]))),
        ('Reject reversed corners', lambda f: rejects(f, [[1,0,0,1]], [[0,0,1,1]])),
        ('Reject wrong columns', lambda f: rejects(f, [[0,0,1]], [[0,0,1,1]])),
        ('Reject nonfinite coordinate', lambda f: rejects(f, [[0,0,np.inf,1]], [[0,0,1,1]])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[0,0,2,2]], [[1,1,3,3]]), np.array([[1/7]])))
    ]
    return run_cases(namespace, 'box_iou', cases, mode)
