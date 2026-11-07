def run_tests(namespace, mode="all"):
    cases = [
        ('One unit kernel weight', lambda f: assert_close(f([[0]],[[0]],[[2]]),np.array([[2/(1+1e-6)]]))),
        ('Two equal keys', lambda f: assert_close(f([[0]],[[0],[0]],[[2],[6]]),np.array([[8/(2+1e-6)]]))),
        ('Small positive feature maps', lambda f: assert_close(f([[np.log(.5)]],[[np.log(.5)]],[[4]]),np.array([[1/(.25+1e-6)]]))),
        ('Positive feature weighting', lambda f: assert_close(f([[2]],[[0],[1]],[[2],[8]]),np.array([[54/(9+1e-6)]]))),
        ('Unequal query and key counts', lambda f: assert_close(f([[0],[1]],[[0]],[[3,6]]),np.array([[3/(1+1e-6),6/(1+1e-6)],[6/(2+1e-6),12/(2+1e-6)]]))),
        ('Tiny kernel mass is attenuated', lambda f: assert_close(f([[-20]],[[-20]],[[1]]),np.array([[np.exp(-40)/(np.exp(-40)+1e-6)]]),atol=1e-15)),
        ('Positive inputs do not overflow exp', lambda f: assert_close(f([[1000]],[[1000]],[[2]]),np.array([[2*1001**2/(1001**2+1e-6)]]))),
        ('Zero underflow mass', lambda f: assert_close(f([[-1000]],[[-1000]],[[2]]),np.zeros((1,1)))),
        ('Reject incompatible feature widths', lambda f: rejects(f,[[0,0]],[[0]],[[1]])),
        ('Reject empty key set', lambda f: rejects(f,[[0]],np.empty((0,1)),np.empty((0,1)))),
        ('Reject nonfinite input', lambda f: rejects(f,[[np.inf]],[[0]],[[1]])),
        ('No mutation', lambda f: assert_close(unchanged(f,np.zeros((1,1)),np.zeros((1,1)),np.array([[2.]])),np.array([[2/(1+1e-6)]])))
    ]
    return run_cases(namespace, 'linear_attention', cases, mode)
