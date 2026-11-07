def run_tests(namespace, mode="all"):
    cases = [
        ('One shared key', lambda f: assert_close(f(np.zeros((2,1,1)),[[[0]]],[[[7]]]),np.full((2,1,1),7.))),
        ('Contiguous groups', lambda f: assert_close(f(np.zeros((4,1,1)),np.zeros((2,1,1)),[[[2]],[[9]]]),np.array([[[2.]],[[2.]],[[9.]],[[9.]]]))),
        ('Uniform two-key mixture', lambda f: assert_close(f([[[0]]],[[[1],[3]]],[[[2],[8]]]),np.array([[[5.]]]))),
        ('Query content still matters', lambda f: assert_close(f([[[np.log(3)]]],[[[0],[1]]],[[[0],[8]]]),np.array([[[6.]]]))),
        ('Feature scaling', lambda f: assert_close(f([[[1,1]]],[[[0,0],[1,1]]],[[[0],[1]]]),np.array([[[1/(1+np.exp(-np.sqrt(2)))]]]))),
        ('Independent query positions', lambda f: assert_close(f([[[0],[np.log(3)]]],[[[0],[1]]],[[[0],[8]]]),np.array([[[4.],[6.]]]))),
        ('Multiple value channels', lambda f: assert_close(f([[[0]]],[[[0]]],[[[2,5]]]),np.array([[[2.,5.]]]))),
        ('Reject nondivisible head count', lambda f: rejects(f,np.zeros((3,1,1)),np.zeros((2,1,1)),np.zeros((2,1,1)))),
        ('Reject key width mismatch', lambda f: rejects(f,[[[1,2]]],[[[1]]],[[[1]]])),
        ('Reject empty keys', lambda f: rejects(f,[[[1]]],np.empty((1,0,1)),np.empty((1,0,1)))),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,np.zeros((2,1,1)),[[[0]]],[[[7]]]),np.full((2,1,1),7.))),
    ]
    return run_cases(namespace, 'grouped_attention', cases, mode)
