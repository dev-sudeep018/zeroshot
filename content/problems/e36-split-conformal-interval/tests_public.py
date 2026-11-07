def run_tests(namespace, mode="all"):
    cases = [
        ('Finite sample correction', lambda f: assert_close(f([1,2,3,4], [10,20], .4), dict(radius=3.,lower=np.array([7.,17.]),upper=np.array([13.,23.])))),
        ('Tied residuals', lambda f: assert_close(f([2,2,2], [0], .5), dict(radius=2.,lower=np.array([-2.]),upper=np.array([2.])))),
        ('Zero residuals', lambda f: assert_close(f([0,0], [5], .5), dict(radius=0.,lower=np.array([5.]),upper=np.array([5.])))),
        ('Unsorted residuals', lambda f: assert_close(f([4,1,3,2], [-2], .4), dict(radius=3.,lower=np.array([-5.]),upper=np.array([1.])))),
        ('Empty prediction batch', lambda f: assert_close(f([1,2], [], .5), dict(radius=2.,lower=np.array([]),upper=np.array([])))),
        ('One calibration point', lambda f: assert_close(f([3], [1], .5), dict(radius=3.,lower=np.array([-2.]),upper=np.array([4.])))),
        ('Reject unsupported finite rank', lambda f: rejects(f, [1,2], [0], .1)),
        ('Reject negative residual', lambda f: rejects(f, [-1,2], [0], .5)),
        ('Reject invalid alpha', lambda f: rejects(f, [1,2], [0], 0)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1,2,3,4], [10,20], .4), dict(radius=3.,lower=np.array([7.,17.]),upper=np.array([13.,23.]))))
    ]
    return run_cases(namespace, 'conformal_interval', cases, mode)
