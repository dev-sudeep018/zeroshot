def run_tests(namespace, mode="all"):
    cases = [
        ('Two means', lambda f: assert_close(f([[0],[2],[10]],[0,0,1],[[9],[9]]), np.array([[1.],[10.]]))),
        ('Empty cluster', lambda f: assert_close(f([[2],[4]],[0,0],[[0],[99]]), np.array([[3.],[99.]]))),
        ('Two features', lambda f: assert_close(f([[0,2],[2,4]],[0,0],[[9,9]]), np.array([[1.,3.]]))),
        ('Label order', lambda f: assert_close(f([[1],[9]],[1,0],[[0],[0]]), np.array([[9.],[1.]]))),
        ('Singleton clusters', lambda f: assert_close(f([[1],[2],[3]],[0,1,2],[[9],[9],[9]]), np.array([[1.],[2.],[3.]]))),
        ('Negative values', lambda f: assert_close(f([[-4],[-2],[3]],[0,0,1],[[0],[0]]), np.array([[-3.],[3.]]))),
        ('Reject fractional ID', lambda f: rejects(f,[[1]],[.5],[[0]])),
        ('Reject missing label', lambda f: rejects(f,[[1],[2]],[0],[[0]])),
        ('Reject features', lambda f: rejects(f,[[1,2]],[0],[[0]])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[0.],[2.],[10.]]),np.array([0,0,1]),np.array([[9.],[9.]])),np.array([[1.],[10.]]))),
    ]
    return run_cases(namespace, 'update_centroids', cases, mode)
