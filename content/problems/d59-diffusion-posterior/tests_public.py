def run_tests(namespace, mode="all"):
    cases = [
        ('First step returns endpoint', lambda f: assert_close(f([2],[99],.25,1),{"mean":np.array([2.]),"variance":0.})),
        ('Zero endpoint and noisy state', lambda f: assert_close(f([0],[0],.5,.5),{"mean":np.array([0.]),"variance":1/3})),
        ('Symmetric coefficient example', lambda f: assert_close(f([3],[6],.5,.5),{"mean":np.array([3*np.sqrt(2)]),"variance":1/3})),
        ('Only clean contribution', lambda f: assert_close(f([3],[0],.5,.5),{"mean":np.array([np.sqrt(2)]),"variance":1/3})),
        ('Only noisy contribution', lambda f: assert_close(f([0],[3],.5,.5),{"mean":np.array([np.sqrt(2)]),"variance":1/3})),
        ('Preserve shape', lambda f: assert_close(f(np.ones((2,3)),np.zeros((2,3)),.5,1),{"mean":np.ones((2,3)),"variance":0.})),
        ('Opposite signals cancel', lambda f: assert_close(f([3],[-3],.5,.5),{"mean":np.array([0.]),"variance":1/3})),
        ('Reject zero beta', lambda f: rejects(f,[1],[1],0,1)),
        ('Reject invalid cumulative retention', lambda f: rejects(f,[1],[1],.5,1.1)),
        ('Reject broadcast noisy input', lambda f: rejects(f,[[1,2]],[[1]],.5,.5)),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[2],[99],.25,1),{"mean":np.array([2.]),"variance":0.})),
    ]
    return run_cases(namespace, 'diffusion_posterior', cases, mode)
