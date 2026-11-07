def run_tests(namespace, mode="all"):
    cases = [
        ('Two observed rewards', lambda f: assert_close(f([1,2,3],[0,10,20,30],[0,0,0],0.5,2), np.array([7.,11.,18.]))),
        ('Terminal cuts lookahead', lambda f: assert_close(f([1,2,100],[0,10,20,30],[0,1,0],0.5,3), np.array([2.,2.,115.]))),
        ('One-step horizon', lambda f: assert_close(f([1,2],[0,4,8],[0,0],0.5,1), np.array([3.,6.]))),
        ('Short rollout retains bootstrap', lambda f: assert_close(f([1],[0,8],[0],0.5,10), np.array([5.]))),
        ('Terminal drops bootstrap', lambda f: assert_close(f([1],[0,8],[1],0.5,10), np.array([1.]))),
        ('Zero discount', lambda f: assert_close(f([1,2],[4,8,16],[0,0],0,2), np.array([1.,2.]))),
        ('Undiscounted full return', lambda f: assert_close(f([1,2,3],[0,0,0,0],[0,0,1],1,3), np.array([6.,5.,3.]))),
        ('Reject missing bootstrap', lambda f: rejects(f, [1],[0],[0],0.9,1)),
        ('Reject zero horizon', lambda f: rejects(f, [1],[0,0],[0],0.9,0)),
        ('Reject fractional horizon', lambda f: rejects(f, [1],[0,0],[0],0.9,1.5)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1,2,3],[0,10,20,30],[0,0,0],0.5,2), np.array([7.,11.,18.])))
    ]
    return run_cases(namespace, 'n_step_targets', cases, mode)
