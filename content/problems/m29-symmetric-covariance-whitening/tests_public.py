def run_tests(namespace, mode="all"):
    cases = [
        ('Diagonal covariance', lambda f: assert_close(f([[3,0],[0,8]],1), np.diag([.5,1/3]))),
        ('Zero covariance', lambda f: assert_close(f([[0,0],[0,0]],4), np.eye(2)*.5)),
        ('Rotated directions', lambda f: assert_close(f([[1.5,.5],[.5,1.5]],2), np.array([[(.5+1/np.sqrt(3))/2,(.5-1/np.sqrt(3))/2],[(.5-1/np.sqrt(3))/2,(.5+1/np.sqrt(3))/2]]))),
        ('One feature', lambda f: assert_close(f([[8]],1), np.array([[1/3]]))),
        ('Repeated eigenvalues', lambda f: assert_close(f([[2,0],[0,2]],2), np.eye(2)*.5)),
        ('Rank deficient', lambda f: assert_close(f([[1,1],[1,1]],2), np.array([[(.5+1/np.sqrt(2))/2,(.5-1/np.sqrt(2))/2],[(.5-1/np.sqrt(2))/2,(.5+1/np.sqrt(2))/2]]))),
        ('Reject asymmetric matrix', lambda f: rejects(f,[[1,2],[0,1]],1)),
        ('Reject negative eigenvalue', lambda f: rejects(f,[[1,0],[0,-1]],1)),
        ('Reject zero regularizer', lambda f: rejects(f,[[1]],0)),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[3.,0],[0,8.]]),1),np.diag([.5,1/3]))),
    ]
    return run_cases(namespace, 'whiten_covariance', cases, mode)
