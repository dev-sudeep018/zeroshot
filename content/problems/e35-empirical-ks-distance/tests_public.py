def run_tests(namespace, mode="all"):
    cases = [
        ('Disjoint samples', lambda f: assert_close(f([0,1], [2,3]), dict(statistic=1.,location=1.))),
        ('Identical empirical distributions', lambda f: assert_close(f([2,1], [1,2]), dict(statistic=0.,location=1.))),
        ('Ties count together', lambda f: assert_close(f([0,0,1], [0,1,1]), dict(statistic=1/3,location=0.))),
        ('Unequal sample counts', lambda f: assert_close(f([0], [0,1]), dict(statistic=.5,location=0.))),
        ('Earliest maximizer', lambda f: assert_close(f([0,2], [1,3]), dict(statistic=.5,location=0.))),
        ('Negative observations', lambda f: assert_close(f([-3,-2], [-1]), dict(statistic=1.,location=-2.))),
        ('Reject empty sample', lambda f: rejects(f, [], [1])),
        ('Reject nonfinite sample', lambda f: rejects(f, [1], [np.nan])),
        ('Reject matrix sample', lambda f: rejects(f, [[1]], [1])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [0,1], [2,3]), dict(statistic=1.,location=1.)))
        ,('Exact tied CDF gaps choose earliest support', lambda f: assert_close(f([0,0,1], [0,1,1]), dict(statistic=1/3,location=0.)))
    ]
    return run_cases(namespace, 'ks_distance', cases, mode)
