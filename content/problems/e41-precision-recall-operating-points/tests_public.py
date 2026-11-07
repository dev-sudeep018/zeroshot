def run_tests(namespace, mode="all"):
    cases = [
        ('Tied scores enter together', lambda f: assert_close(f([1,0,1], [.9,.9,.2]), dict(thresholds=np.array([.9,.2]),precision=np.array([.5,2/3]),recall=np.array([.5,1.])))),
        ('Perfect ordering', lambda f: assert_close(f([1,0], [2,1]), dict(thresholds=np.array([2.,1.]),precision=np.array([1.,.5]),recall=np.array([1.,1.])))),
        ('Worst ordering', lambda f: assert_close(f([0,1], [2,1]), dict(thresholds=np.array([2.,1.]),precision=np.array([0.,.5]),recall=np.array([0.,1.])))),
        ('All scores equal', lambda f: assert_close(f([1,0,1], [0,0,0]), dict(thresholds=np.array([0.]),precision=np.array([2/3]),recall=np.array([1.])))),
        ('Single positive', lambda f: assert_close(f([1], [-3]), dict(thresholds=np.array([-3.]),precision=np.array([1.]),recall=np.array([1.])))),
        ('All positive labels', lambda f: assert_close(f([1,1], [1,2]), dict(thresholds=np.array([2.,1.]),precision=np.array([1.,1.]),recall=np.array([.5,1.])))),
        ('Reject no positive labels', lambda f: rejects(f, [0,0], [1,2])),
        ('Reject mismatched shapes', lambda f: rejects(f, [1], [1,2])),
        ('Reject nonbinary label', lambda f: rejects(f, [2], [1])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1,0,1], [.9,.9,.2]), dict(thresholds=np.array([.9,.2]),precision=np.array([.5,2/3]),recall=np.array([.5,1.]))))
    ]
    return run_cases(namespace, 'precision_recall_points', cases, mode)
