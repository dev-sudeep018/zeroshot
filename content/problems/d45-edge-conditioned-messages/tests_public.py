def run_tests(namespace, mode="all"):
    cases = [
        ('Edge feature becomes message', lambda f: assert_close(f([[0]],[[1]],[[[3]]],[[0],[0],[2]],[[0],[1]]),np.array([[6.]]))),
        ('Receiver survives isolation', lambda f: assert_close(f([[4]],[[0]],[[[9]]],[[1],[1],[1]],[[2],[1]]),np.array([[8.]]))),
        ('Weighted message', lambda f: assert_close(f([[2]],[[3]],[[[0]]],[[0],[1],[0]],[[0],[1]]),np.array([[6.]]))),
        ('Negative message is clipped', lambda f: assert_close(f([[0]],[[1]],[[[-3]]],[[0],[0],[1]],[[0],[1]]),np.array([[0.]]))),
        ('Sender orientation', lambda f: assert_close(f([[2],[8]],[[0,1],[0,0]],np.zeros((2,2,1)),[[0],[1],[0]],[[0],[1]]),np.array([[8.],[0.]]))),
        ('Recipient orientation', lambda f: assert_close(f([[2],[8]],[[0,1],[0,0]],np.zeros((2,2,1)),[[1],[0],[0]],[[0],[1]]),np.array([[2.],[0.]]))),
        ('Final activation', lambda f: assert_close(f([[-2]],[[0]],[[[0]]],[[0],[0],[1]],[[1],[0]]),np.array([[0.]]))),
        ('Reject negative edge weight', lambda f: rejects(f,[[1]],[[-1]],[[[0]]],[[0],[1],[0]],[[0],[1]])),
        ('Reject message width', lambda f: rejects(f,[[1]],[[1]],[[[0]]],[[1]],[[0],[1]])),
        ('Reject nonfinite edges', lambda f: rejects(f,[[1]],[[1]],[[[np.nan]]],[[0],[1],[0]],[[0],[1]])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[0]],[[1]],[[[3]]],[[0],[0],[2]],[[0],[1]]),np.array([[6.]]))),
    ]
    return run_cases(namespace, 'edge_messages', cases, mode)
