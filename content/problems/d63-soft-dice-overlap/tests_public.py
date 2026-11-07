def run_tests(namespace, mode="all"):
    cases = [
        ('Exact binary match', lambda f: assert_close(f([[1,0]],[[1,0]],1),np.array([0.]))),
        ('Disjoint masks', lambda f: assert_close(f([[1,0]],[[0,1]],1),np.array([2/3]))),
        ('Both masks empty', lambda f: assert_close(f([[0,0]],[[0,0]],1),np.array([0.]))),
        ('Soft confidence', lambda f: assert_close(f([[.5]],[[1]],1),np.array([.2]))),
        ('False positive mass', lambda f: assert_close(f([[1]],[[0]],1),np.array([.5]))),
        ('Missing positive', lambda f: assert_close(f([[0]],[[1]],1),np.array([.5]))),
        ('Examples remain separate', lambda f: assert_close(f([[1],[0]],[[1],[1]],1),np.array([0.,.5]))),
        ('Reject probability outside bounds', lambda f: rejects(f,[[1.1]],[[1]])),
        ('Reject nonbinary target', lambda f: rejects(f,[[.5]],[[.5]])),
        ('Reject zero smoothing', lambda f: rejects(f,[[0]],[[0]],0)),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[1,0]],[[1,0]],1),np.array([0.]))),
    ]
    return run_cases(namespace, 'soft_dice_loss', cases, mode)
