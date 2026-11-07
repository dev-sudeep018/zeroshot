def run_tests(namespace, mode="all"):
    cases = [
        ('Identity geometry', lambda f: assert_close(f([[3,4],[0,0]],[0,0],[[1,0],[0,1]]), np.array([25.,0]))),
        ('Anisotropic geometry', lambda f: assert_close(f([[2,2]],[0,0],[[.25,0],[0,1]]), np.array([5.]))),
        ('Correlated precision', lambda f: assert_close(f([[1,1],[1,-1]],[0,0],[[2,1],[1,2]]), np.array([6.,2]))),
        ('Shifted center', lambda f: assert_close(f([[4,5]],[1,1],[[1,0],[0,1]]), np.array([25.]))),
        ('Single dimension', lambda f: assert_close(f([[2],[-2]],[0],[[.5]]), np.array([2.,2]))),
        ('At center', lambda f: assert_close(f([[2,3]],[2,3],[[2,1],[1,2]]), np.array([0.]))),
        ('Reject indefinite precision', lambda f: rejects(f,[[1,1]],[0,0],[[1,2],[2,1]])),
        ('Reject asymmetric precision', lambda f: rejects(f,[[1,1]],[0,0],[[1,1],[0,1]])),
        ('Reject dimension mismatch', lambda f: rejects(f,[[1,2]],[0],[[1]])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[3.,4]]),np.array([0.,0]),np.eye(2)),np.array([25.]))),
    ]
    return run_cases(namespace, 'mahalanobis_squared', cases, mode)
