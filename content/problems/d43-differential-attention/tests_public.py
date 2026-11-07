def run_tests(namespace, mode="all"):
    cases = [
        ('Identical maps cancel', lambda f: assert_close(f([[0]],[[0],[0]],[[0]],[[0],[0]],[[2],[8]],1),np.zeros((1,1)))),
        ('Keep the first map', lambda f: assert_close(f([[0]],[[0],[0]],[[1]],[[0],[1]],[[2],[8]],0),np.array([[5.]]))),
        ('Signed contrast', lambda f: assert_close(f([[np.log(3)]],[[0],[1]],[[0]],[[0],[1]],[[0],[8]],1),np.array([[2.]]))),
        ('Negative output allowed', lambda f: assert_close(f([[0]],[[0],[1]],[[np.log(3)]],[[0],[1]],[[0],[8]],1),np.array([[-2.]]))),
        ('Constant-value row sum', lambda f: assert_close(f([[7]],[[0],[1]],[[3]],[[1],[2]],[[4],[4]],2),np.array([[-4.]]))),
        ('One-key formula', lambda f: assert_close(f([[2]],[[3]],[[4]],[[5]],[[6,8]],.5),np.array([[3.,4.]]))),
        ('Negative coefficient adds maps', lambda f: assert_close(f([[0]],[[0],[0]],[[0]],[[0],[0]],[[2],[8]],-1),np.array([[10.]]))),
        ('Reject query mismatch', lambda f: rejects(f,[[0]],[[0]],[[0],[0]],[[0]],[[1]],1)),
        ('Reject nonfinite coefficient', lambda f: rejects(f,[[0]],[[0]],[[0]],[[0]],[[1]],np.inf)),
        ('Reject value row mismatch', lambda f: rejects(f,[[0]],[[0],[1]],[[0]],[[0],[1]],[[1]],1)),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[0]],[[0],[0]],[[0]],[[0],[0]],[[2],[8]],1),np.zeros((1,1)))),
    ]
    return run_cases(namespace, 'differential_attention', cases, mode)
