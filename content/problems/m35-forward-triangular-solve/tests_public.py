def run_tests(namespace, mode="all"):
    cases = [
        ('Two-step solve', lambda f: assert_close(f([[2,0],[3,1]],[4,7]), np.array([2.,1]))),
        ('Diagonal solve', lambda f: assert_close(f([[2,0],[0,4]],[6,8]), np.array([3.,2]))),
        ('Negative diagonal', lambda f: assert_close(f([[-2,0],[1,-1]],[4,3]), np.array([-2.,-5]))),
        ('Three rows', lambda f: assert_close(f([[1,0,0],[2,1,0],[3,4,2]],[1,4,17]), np.array([1.,2,3]))),
        ('Zero target', lambda f: assert_close(f([[2,0],[1,3]],[0,0]), np.zeros(2))),
        ('Single equation', lambda f: assert_close(f([[4]],[3]), np.array([.75]))),
        ('Reject upper entry', lambda f: rejects(f,[[1,1],[0,1]],[1,2])),
        ('Reject zero diagonal', lambda f: rejects(f,[[0]],[1])),
        ('Reject target shape', lambda f: rejects(f,[[1,0],[0,1]],[1])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[2.,0],[3,1]]),np.array([4.,7])),np.array([2.,1]))),
        ('Reject nonfinite triangular solution', lambda f: rejects(f,np.eye(24)*2e-12+np.tril(np.full((24,24),1e6),-1),np.ones(24))),
    ]
    return run_cases(namespace, 'forward_substitution', cases, mode)
