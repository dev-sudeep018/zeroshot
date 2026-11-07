def run_tests(namespace, mode="all"):
    cases = [
        ('Two observations', lambda f: assert_close(f([[0],[1]],[[0],[1]],1), np.array([[1.,np.exp(-1)],[np.exp(-1),1]]))),
        ('Zero gamma', lambda f: assert_close(f([[0],[99]],[[2]],0), np.ones((2,1)))),
        ('Squared distance', lambda f: assert_close(f([[0]],[[2]],.5), np.array([[np.exp(-2)]]))),
        ('Two dimensions', lambda f: assert_close(f([[0,0]],[[3,4]],.04), np.array([[np.exp(-1)]]))),
        ('Cross-set shape', lambda f: assert_close(f([[0],[1]],[[0],[1],[2]],1), np.array([[1.,np.exp(-1),np.exp(-4)],[np.exp(-1),1,np.exp(-1)]]))),
        ('Duplicate rows', lambda f: assert_close(f([[2],[2]],[[2]],9), np.ones((2,1)))),
        ('Reject negative gamma', lambda f: rejects(f,[[0]],[[1]],-1)),
        ('Reject mismatched features', lambda f: rejects(f,[[0,1]],[[1]],1)),
        ('Reject boolean gamma', lambda f: rejects(f,[[0]],[[1]],True)),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[0.],[1.]]),np.array([[0.],[1.]]),1),np.array([[1.,np.exp(-1)],[np.exp(-1),1]]))),
    ]
    return run_cases(namespace, 'rbf_kernel', cases, mode)
