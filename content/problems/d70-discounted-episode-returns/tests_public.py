def run_tests(namespace, mode="all"):
    cases = [
        ('Three-step return', lambda f: assert_close(f([1,2,3],[0,0,1],0.5), np.array([2.75,3.5,3.]))),
        ('Terminal boundary', lambda f: assert_close(f([1,2,100],[0,1,1],1), np.array([3.,2.,100.]))),
        ('Rollout cutoff', lambda f: assert_close(f([1,2],[0,0],0.5,8), np.array([4.,6.]))),
        ('Immediate rewards only', lambda f: assert_close(f([1,-2,4],[0,0,0],0,99), np.array([1.,-2.,4.]))),
        ('Terminal ignores bootstrap', lambda f: assert_close(f([3],[1],0.9,100), np.array([3.]))),
        ('Negative rewards', lambda f: assert_close(f([-1,-2],[0,1],1), np.array([-3.,-2.]))),
        ('All terminals', lambda f: assert_close(f([1,2,3],[1,1,1],0.5,20), np.array([1.,2.,3.]))),
        ('Reject mismatched flags', lambda f: rejects(f, [1,2],[0],0.9)),
        ('Reject invalid discount', lambda f: rejects(f, [1],[0],1.01)),
        ('Reject nonbinary terminal', lambda f: rejects(f, [1],[2],0.9)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1,2,3],[0,0,1],0.5), np.array([2.75,3.5,3.])))
    ]
    return run_cases(namespace, 'episode_returns', cases, mode)
