def run_tests(namespace, mode="all"):
    cases = [
        ('Mask padding', lambda f: assert_close(f([[[0,0],[0,2],[3,0]]],[[0,1,0]],[[1,1,0]]), {'per_token':np.array([[0.6931471805599453, 0.1269280110429726, 0.0]], dtype='float64'),'loss':0.41003759580145893,'count':2})),
        ('Uniform distribution', lambda f: assert_close(f([[[0,0,0]]],[[2]],[[1]]), {'per_token':np.array([[1.0986122886681098]], dtype='float64'),'loss':1.0986122886681098,'count':1})),
        ('Extreme wrong class', lambda f: assert_close(f([[[1000,-1000]]],[[1]],[[1]]), {'per_token':np.array([[2000.0]], dtype='float64'),'loss':2000.0,'count':1})),
        ('Unequal valid lengths', lambda f: assert_close(f(np.zeros((2,2,2)),[[0,1],[1,0]],[[1,1],[1,0]]), {'per_token':np.array([[0.6931471805599453, 0.6931471805599453], [0.6931471805599453, 0.0]], dtype='float64'),'loss':0.6931471805599453,'count':3})),
        ('Single vocabulary token', lambda f: assert_close(f([[[5],[8]]],[[0,0]],[[1,0]]), {'per_token':np.array([[0.0, 0.0]], dtype='float64'),'loss':0.0,'count':1})),
        ('Ignore huge masked loss', lambda f: assert_close(f([[[0,0],[1000000,-1000000]]],[[0,1]],[[1,0]]), {'per_token':np.array([[0.6931471805599453, 0.0]], dtype='float64'),'loss':0.6931471805599453,'count':1})),
        ('Reject all padding', lambda f: rejects(f, [[[0,0]]],[[0]],[[0]])),
        ('Reject target outside vocabulary', lambda f: rejects(f, [[[0,0]]],[[2]],[[1]])),
        ('Reject nonbinary mask', lambda f: rejects(f, [[[0,0]]],[[0]],[[0.5]])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[[0,0],[0,2],[3,0]]],[[0,1,0]],[[1,1,0]]), {'per_token':np.array([[0.6931471805599453, 0.1269280110429726, 0.0]], dtype='float64'),'loss':0.41003759580145893,'count':2})),
    ]
    return run_cases(namespace, 'masked_token_nll', cases, mode)
