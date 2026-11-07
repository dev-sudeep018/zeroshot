def run_tests(namespace, mode="all"):
    cases = [
        ('Two connected nodes', lambda f: assert_close(f([[0,1],[1,0]],[[1],[2]],[[1]],[0],[[1]],[0]),np.array([[3.],[3.]]))),
        ('Increase the self contribution', lambda f: assert_close(f([[0,1],[1,0]],[[1],[2]],[[1]],[0],[[1]],[0],1),np.array([[4.],[5.]]))),
        ('Linear final layer', lambda f: assert_close(f([[0,1],[1,0]],[[1],[2]],[[1]],[0],[[-1]],[0]),np.array([[-3.],[-3.]]))),
        ('Sum retains multiplicity', lambda f: assert_close(f([[0,1,1],[0,0,0],[0,0,0]],[[0],[3],[3]],[[1]],[0],[[1]],[0]),np.array([[6.],[3.],[3.]]))),
        ('Negative hidden activation', lambda f: assert_close(f([[0]],[[-2]],[[1]],[1],[[4]],[3]),np.array([[3.]]))),
        ('Cancel the self term', lambda f: assert_close(f([[0]],[[100]],[[1]],[2],[[3]],[4],-1),np.array([[10.]]))),
        ('Weighted directed messages', lambda f: assert_close(f([[0,2],[0,0]],[[1],[3]],[[1]],[0],[[1]],[0]),np.array([[7.],[3.]]))),
        ('Reject explicit self edge', lambda f: rejects(f,[[1]],[[1]],[[1]],[0],[[1]],[0])),
        ('Reject negative edge', lambda f: rejects(f,[[0,-1],[0,0]],[[1],[2]],[[1]],[0],[[1]],[0])),
        ('Reject broadcast bias', lambda f: rejects(f,[[0]],[[1]],[[1,2]],[0],[[1],[1]],[0])),
        ('Reject invalid epsilon', lambda f: rejects(f,[[0]],[[1]],[[1]],[0],[[1]],[0],2**4096)),
        ('No mutation', lambda f: assert_close(unchanged(f,np.zeros((1,1)),np.ones((1,1)),np.ones((1,1)),np.zeros(1),np.ones((1,1)),np.zeros(1)),np.ones((1,1))))
    ]
    return run_cases(namespace, 'gin_layer', cases, mode)
