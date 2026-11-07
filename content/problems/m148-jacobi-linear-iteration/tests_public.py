def run_tests(namespace, mode="all"):
    cases = [
        ('Two coupled equations', lambda f: assert_close(f([[4,1],[2,3]],[1,2],[0,0],3), {'solution':np.array([0.125, 0.611111111111111], dtype=float).reshape((2,)),'residual':np.array([0.11111111111111116, 0.08333333333333304], dtype=float).reshape((2,))})),
        ('Diagonal system', lambda f: assert_close(f([[2,0],[0,-4]],[6,8],[0,0],1), {'solution':np.array([3.0, -2.0], dtype=float).reshape((2,)),'residual':np.array([0.0, 0.0], dtype=float).reshape((2,))})),
        ('No iteration', lambda f: assert_close(f([[3,1],[1,3]],[1,1],[2,3],0), {'solution':np.array([2.0, 3.0], dtype=float).reshape((2,)),'residual':np.array([8.0, 10.0], dtype=float).reshape((2,))})),
        ('Already solved', lambda f: assert_close(f([[3,1],[1,3]],[4,4],[1,1],4), {'solution':np.array([1.0, 1.0], dtype=float).reshape((2,)),'residual':np.array([0.0, 0.0], dtype=float).reshape((2,))})),
        ('Single equation', lambda f: assert_close(f([[2]],[8],[1],5), {'solution':np.array([4.0], dtype=float).reshape((1,)),'residual':np.array([0.0], dtype=float).reshape((1,))})),
        ('Asymmetric system', lambda f: assert_close(f([[5,-1,1],[1,4,0],[0,1,3]],[2,4,6],[0,0,0],12), {'solution':np.array([0.2499998834876543, 0.9374999386574074, 1.687500150462963], dtype=float).reshape((3,)),'residual':np.array([-3.70756172873854e-07, -3.6188271579362663e-07, 3.9004629659444845e-07], dtype=float).reshape((3,))})),
        ('Reject zero diagonal', lambda f: rejects(f,[[0]],[1],[0],1)),
        ('Reject nondominant matrix', lambda f: rejects(f,[[1,2],[2,1]],[1,1],[0,0],1)),
        ('Reject mismatched vectors', lambda f: rejects(f,[[2]],[1],[0,1],1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[4,1],[2,3]],[1,2],[0,0],3), {'solution':np.array([0.125, 0.611111111111111], dtype=float).reshape((2,)),'residual':np.array([0.11111111111111116, 0.08333333333333304], dtype=float).reshape((2,))})),
    ]
    return run_cases(namespace, 'jacobi_iterations', cases, mode)
