def run_tests(namespace, mode="all"):
    cases = [
        ('Two orthogonal features', lambda f: assert_close(f([[1,0],[0,1]]), np.array([[.5,-.5],[-.5,.5]]))),
        ('Constant kernel', lambda f: assert_close(f([[3,3],[3,3]]), np.zeros((2,2)))),
        ('One observation', lambda f: assert_close(f([[7]]), np.zeros((1,1)))),
        ('Scalar feature Gram matrix', lambda f: assert_close(f([[1,3],[3,9]]), np.array([[1.,-1],[-1,1]]))),
        ('Already centered', lambda f: assert_close(f([[1,-1],[-1,1]]), np.array([[1.,-1],[-1,1]]))),
        ('Three observations', lambda f: assert_close(f(np.eye(3)), np.eye(3)-np.ones((3,3))/3)),
        ('Reject rectangle', lambda f: rejects(f,[[1,2]])),
        ('Reject asymmetry', lambda f: rejects(f,[[1,2],[0,1]])),
        ('Reject nonfinite kernel', lambda f: rejects(f,[[np.nan]])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[1.,0],[0,1]])),np.array([[.5,-.5],[-.5,.5]]))),
    ]
    return run_cases(namespace, 'center_kernel', cases, mode)
