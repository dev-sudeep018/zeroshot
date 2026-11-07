def run_tests(namespace, mode="all"):
    cases = [
        ('Merge first pair', lambda f: assert_close(f([[0,1,5],[1,0,3],[5,3,0]]), {"pair":np.array([0,1]),"distance":1,"distances":np.array([[0.,3],[3,0]])})),
        ('Only two clusters', lambda f: assert_close(f([[0,4],[4,0]]), {"pair":np.array([0,1]),"distance":4,"distances":np.zeros((1,1))})),
        ('Tie order', lambda f: assert_close(f([[0,2,2],[2,0,2],[2,2,0]]), {"pair":np.array([0,1]),"distance":2,"distances":np.array([[0.,2],[2,0]])})),
        ('Later pair', lambda f: assert_close(f([[0,8,6],[8,0,1],[6,1,0]]), {"pair":np.array([1,2]),"distance":1,"distances":np.array([[0.,6],[6,0]])})),
        ('Zero separation', lambda f: assert_close(f([[0,0,3],[0,0,4],[3,4,0]]), {"pair":np.array([0,1]),"distance":0,"distances":np.array([[0.,3],[3,0]])})),
        ('Untouched pair distance', lambda f: assert_close(f([[0,1,8,9],[1,0,6,7],[8,6,0,4],[9,7,4,0]]), {"pair":np.array([0,1]),"distance":1,"distances":np.array([[0.,6,7],[6,0,4],[7,4,0]])})),
        ('Reject asymmetric matrix', lambda f: rejects(f,[[0,1],[2,0]])),
        ('Reject nonzero diagonal', lambda f: rejects(f,[[1,2],[2,0]])),
        ('Reject one cluster', lambda f: rejects(f,[[0]])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[0.,1,5],[1,0,3],[5,3,0]])),{"pair":np.array([0,1]),"distance":1,"distances":np.array([[0.,3],[3,0]])})),
    ]
    return run_cases(namespace, 'single_linkage_merge', cases, mode)
