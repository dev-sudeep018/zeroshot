def run_tests(namespace, mode="all"):
    cases = [
        ('Partial move', lambda f: assert_close(f([0,10],[8,2],0.25), np.array([2.,8.]))),
        ('Frozen target', lambda f: assert_close(f([1,2],[9,8],0), np.array([1.,2.]))),
        ('Hard copy', lambda f: assert_close(f([1,2],[9,8],1), np.array([9.,8.]))),
        ('Matrix parameters', lambda f: assert_close(f([[0,2],[4,6]],[[2,4],[6,8]],0.5), np.array([[1.,3.],[5.,7.]]))),
        ('Already synchronized', lambda f: assert_close(f([3,-2],[3,-2],0.2), np.array([3.,-2.]))),
        ('Negative parameters', lambda f: assert_close(f([-4],[-2],0.5), np.array([-3.]))),
        ('Small online weight', lambda f: assert_close(f([0],[10],0.1), np.array([1.]))),
        ('Reject mismatched shape', lambda f: rejects(f, [1],[[1]],0.5)),
        ('Reject invalid rate', lambda f: rejects(f, [1],[2],-0.1)),
        ('Reject scalar parameters', lambda f: rejects(f, 1,2,0.5)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [0,10],[8,2],0.25), np.array([2.,8.])))
    ]
    return run_cases(namespace, 'polyak_update', cases, mode)
