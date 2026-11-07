def run_tests(namespace, mode="all"):
    cases = [
        ('Prior match', lambda f: assert_close(f([[0,0]],[[0,0]]),np.array([0.]))),
        ('Shifted mean', lambda f: assert_close(f([[2]],[[0]]),np.array([2.]))),
        ('Broader variance', lambda f: assert_close(f([[0]],[[np.log(4)]]),np.array([.5*(3-np.log(4))]))),
        ('Narrower variance', lambda f: assert_close(f([[0]],[[np.log(.25)]]),np.array([.5*(-.75-np.log(.25))]))),
        ('Sum latent coordinates', lambda f: assert_close(f([[1,2]],[[0,0]]),np.array([2.5]))),
        ('Keep batch examples', lambda f: assert_close(f([[1],[2]],[[0],[0]]),np.array([.5,2.]))),
        ('Mean sign symmetry', lambda f: assert_close(f([[-2]],[[0]]),np.array([2.]))),
        ('Reject broadcast variance', lambda f: rejects(f,[[1,2]],[[0]])),
        ('Reject unbounded log variance', lambda f: rejects(f,[[0]],[[61]])),
        ('Reject nonfinite mean', lambda f: rejects(f,[[np.inf]],[[0]])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[0,0]],[[0,0]]),np.array([0.]))),
    ]
    return run_cases(namespace, 'gaussian_kl', cases, mode)
