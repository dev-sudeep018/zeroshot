def run_tests(namespace, mode="all"):
    cases = [
        ('Three measurements', lambda f: assert_close(f([1,2,6]), {'estimates':np.array([4.0, 3.5, 1.5], dtype=float).reshape((3,)),'mean_estimate':3.0,'jackknife_se':1.5275252316519465})),
        ('Two measurements', lambda f: assert_close(f([2,8]), {'estimates':np.array([8.0, 2.0], dtype=float).reshape((2,)),'mean_estimate':5.0,'jackknife_se':3.0})),
        ('Constant data', lambda f: assert_close(f([4,4,4]), {'estimates':np.array([4.0, 4.0, 4.0], dtype=float).reshape((3,)),'mean_estimate':4.0,'jackknife_se':0.0})),
        ('Symmetric data', lambda f: assert_close(f([-2,0,2]), {'estimates':np.array([1.0, 0.0, -1.0], dtype=float).reshape((3,)),'mean_estimate':0.0,'jackknife_se':1.1547005383792515})),
        ('Outlier', lambda f: assert_close(f([0,0,0,12]), {'estimates':np.array([4.0, 4.0, 4.0, 0.0], dtype=float).reshape((4,)),'mean_estimate':3.0,'jackknife_se':3.0})),
        ('Fractional data', lambda f: assert_close(f([.1,.4,.7,1]), {'estimates':np.array([0.7000000000000001, 0.6000000000000001, 0.5000000000000001, 0.4000000000000001], dtype=float).reshape((4,)),'mean_estimate':0.55,'jackknife_se':0.19364916731037082})),
        ('Reject singleton', lambda f: rejects(f,[1])),
        ('Reject empty', lambda f: rejects(f,[])),
        ('Reject matrix', lambda f: rejects(f,[[1,2]])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,2,6]), {'estimates':np.array([4.0, 3.5, 1.5], dtype=float).reshape((3,)),'mean_estimate':3.0,'jackknife_se':1.5275252316519465})),
    ]
    return run_cases(namespace, 'leave_one_out_mean', cases, mode)
