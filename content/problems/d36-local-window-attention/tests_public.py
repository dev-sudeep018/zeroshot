def run_tests(namespace, mode="all"):
    cases = [
        ('Self-only attention', lambda f: assert_close(f(np.zeros((3,1)),np.zeros((3,1)),[[2],[4],[8]],0),np.array([[2.],[4.],[8.]]))),
        ('One neighbor on each side', lambda f: assert_close(f(np.zeros((3,1)),np.zeros((3,1)),[[2],[4],[8]],1),np.array([[3.],[14/3],[6.]]))),
        ('Full window', lambda f: assert_close(f(np.zeros((3,1)),np.zeros((3,1)),[[2],[4],[8]],2),np.full((3,1),14/3))),
        ('Distant value excluded', lambda f: assert_close(f(np.zeros((4,1)),np.zeros((4,1)),[[2],[4],[1000],[-1000]],1)[0],np.array([3.]))),
        ('Scale by key dimension', lambda f: assert_close(f([[1,1],[0,0]],[[1,1],[0,0]],[[1],[0]],1),np.array([[1/(1+np.exp(-np.sqrt(2)))],[.5]]))),
        ('Multiple value features', lambda f: assert_close(f([[0]],[[0]],[[2,3]],0),np.array([[2.,3.]]))),
        ('Stable extreme scores', lambda f: assert_close(f([[1000],[1000]],[[1000],[-1000]],[[3],[9]],1),np.full((2,1),3.))),
        ('Reject invalid radius', lambda f: [rejects(f,[[0],[0]],[[0],[0]],[[1],[2]],v) for v in (-1,2,True,1.5,2**4096)]),
        ('Reject missing value row', lambda f: rejects(f,[[0],[0]],[[0],[0]],[[1]],1)),
        ('Reject key width', lambda f: rejects(f,[[0,0]],[[0]],[[1]],0)),
        ('Reject empty sequence', lambda f: rejects(f,np.empty((0,1)),np.empty((0,1)),np.empty((0,1)),0)),
        ('No mutation', lambda f: assert_close(unchanged(f,np.zeros((2,1)),np.zeros((2,1)),np.array([[2.],[4.]]),1),np.full((2,1),3.)))
    ]
    return run_cases(namespace, 'window_attention', cases, mode)
