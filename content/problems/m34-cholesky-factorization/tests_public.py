def run_tests(namespace, mode="all"):
    cases = [
        ('Correlated pair', lambda f: assert_close(f([[4,2],[2,5]]), np.array([[2.,0],[1,2]]))),
        ('Diagonal covariance', lambda f: assert_close(f([[9,0],[0,16]]), np.diag([3.,4.]))),
        ('Single entry', lambda f: assert_close(f([[25]]), np.array([[5.]]))),
        ('Negative off diagonal', lambda f: assert_close(f([[4,-2],[-2,2]]), np.array([[2.,0],[-1,1]]))),
        ('Three dimensions', lambda f: assert_close(f([[4,2,0],[2,5,2],[0,2,2]]), np.array([[2.,0,0],[1,2,0],[0,1,1]]))),
        ('Identity', lambda f: assert_close(f(np.eye(3)), np.eye(3))),
        ('Reject semidefinite', lambda f: rejects(f,[[1,1],[1,1]])),
        ('Reject negative pivot', lambda f: rejects(f,[[1,2],[2,1]])),
        ('Reject asymmetry', lambda f: rejects(f,[[1,1],[0,1]])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[4.,2],[2,5]])),np.array([[2.,0],[1,2]]))),
    ]
    return run_cases(namespace, 'cholesky_lower', cases, mode)
