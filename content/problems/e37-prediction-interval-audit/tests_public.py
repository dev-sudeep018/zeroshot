def run_tests(namespace, mode="all"):
    cases = [
        ('Coverage and width differ', lambda f: assert_close(f([0,5], [-1,0], [1,4]), dict(covered=np.array([True,False]),coverage=.5,widths=np.array([2.,4.]),mean_width=3.))),
        ('Inclusive boundaries', lambda f: assert_close(f([0,2], [0,1], [1,2]), dict(covered=np.array([True,True]),coverage=1.,widths=np.array([1.,1.]),mean_width=1.))),
        ('Exact zero width', lambda f: assert_close(f([2], [2], [2]), dict(covered=np.array([True]),coverage=1.,widths=np.array([0.]),mean_width=0.))),
        ('Missed zero width', lambda f: assert_close(f([3], [2], [2]), dict(covered=np.array([False]),coverage=0.,widths=np.array([0.]),mean_width=0.))),
        ('Negative range', lambda f: assert_close(f([-2], [-3], [-1]), dict(covered=np.array([True]),coverage=1.,widths=np.array([2.]),mean_width=2.))),
        ('All missed', lambda f: assert_close(f([0,5], [1,1], [2,2]), dict(covered=np.array([False,False]),coverage=0.,widths=np.array([1.,1.]),mean_width=1.))),
        ('Reject reversed interval', lambda f: rejects(f, [0], [2], [1])),
        ('Reject shape mismatch', lambda f: rejects(f, [0,1], [0], [1])),
        ('Reject empty arrays', lambda f: rejects(f, [], [], [])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [0,5], [-1,0], [1,4]), dict(covered=np.array([True,False]),coverage=.5,widths=np.array([2.,4.]),mean_width=3.)))
    ]
    return run_cases(namespace, 'interval_audit', cases, mode)
