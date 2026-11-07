def run_tests(namespace, mode="all"):
    cases = [
        ('Swap two nodes', lambda f: assert_close(f([[2],[8]],[[0,1],[1,0]],[[1]],[0,0]),np.array([[8.],[2.]]))),
        ('Isolated node is zero', lambda f: assert_close(f([[4]],[[0]],[[2]],[1,1]),np.array([[0.]]))),
        ('Uniform neighborhood', lambda f: assert_close(f([[2],[8]],[[1,1],[1,1]],[[1]],[0,0]),np.array([[5.],[5.]]))),
        ('Sender score selects mixture', lambda f: assert_close(f([[0],[np.log(3)]],[[1,1],[1,1]],[[1]],[0,1]),np.full((2,1),.75*np.log(3)))),
        ('Explicit self edge', lambda f: assert_close(f([[3]],[[1]],[[2]],[1,1]),np.array([[6.]]))),
        ('No final relu', lambda f: assert_close(f([[-3]],[[1]],[[1]],[0,0]),np.array([[-3.]]))),
        ('Multiple output channels', lambda f: assert_close(f([[2]],[[1]],[[1,-1]],[0,0,0,0]),np.array([[2.,-2.]]))),
        ('Reject weighted adjacency', lambda f: rejects(f,[[1]],[[2]],[[1]],[0,0])),
        ('Reject attention width', lambda f: rejects(f,[[1]],[[1]],[[1]],[0])),
        ('Reject invalid slope', lambda f: rejects(f,[[1]],[[1]],[[1]],[0,0],-1)),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[2],[8]],[[0,1],[1,0]],[[1]],[0,0]),np.array([[8.],[2.]]))),
    ]
    return run_cases(namespace, 'graph_attention', cases, mode)
