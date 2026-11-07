def run_tests(namespace, mode="all"):
    cases = [
        ('Upper triangular input', lambda f: assert_close(f([[1,1],[0,1]]), {"q":np.eye(2),"r":np.array([[1.,1],[0,1]])})),
        ('Scaled axes', lambda f: assert_close(f([[2,0],[0,3]]), {"q":np.eye(2),"r":np.diag([2.,3.])})),
        ('Negative column orientation', lambda f: assert_close(f([[-2,0],[0,3]]), {"q":np.diag([-1.,1.]),"r":np.diag([2.,3.])})),
        ('One column', lambda f: assert_close(f([[3],[4]]), {"q":np.array([[.6],[.8]]),"r":np.array([[5.]])})),
        ('Tall orthogonal columns', lambda f: assert_close(f([[1,0],[0,1],[0,0]]), {"q":np.array([[1.,0],[0,1],[0,0]]),"r":np.eye(2)})),
        ('Mixed orthogonal directions', lambda f: assert_close(f([[1,1],[1,-1]]), {"q":np.array([[1.,1],[1,-1]])/np.sqrt(2),"r":np.eye(2)*np.sqrt(2)})),
        ('Reject dependent columns', lambda f: rejects(f,[[1,2],[2,4]])),
        ('Reject wide matrix', lambda f: rejects(f,[[1,0]])),
        ('Reject zero column', lambda f: rejects(f,[[0],[0]])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[1.,1],[0,1]])),{"q":np.eye(2),"r":np.array([[1.,1],[0,1]])})),
    ]
    return run_cases(namespace, 'gram_schmidt', cases, mode)
