def run_tests(namespace, mode="all"):
    cases = [
        ('Burst followed by refill', lambda f: assert_close(f([0,0,2], [2,2,2], 3, 1), dict(allowed=np.array([True,False,True]),remaining=np.array([1.,1.,1.])))),
        ('Refill is capped', lambda f: assert_close(f([10], [2], 3, 10), dict(allowed=np.array([True]),remaining=np.array([1.])))),
        ('Exact balance is accepted', lambda f: assert_close(f([0], [3], 3, 0), dict(allowed=np.array([True]),remaining=np.array([0.])))),
        ('Rejected request does not spend', lambda f: assert_close(f([0,0], [4,2], 3, 0), dict(allowed=np.array([False,True]),remaining=np.array([3.,1.])))),
        ('Zero-cost request', lambda f: assert_close(f([0], [0], 0, 0), dict(allowed=np.array([True]),remaining=np.array([0.])))),
        ('Fractional time refill', lambda f: assert_close(f([0,.5], [1,.5], 1, 1), dict(allowed=np.array([True,True]),remaining=np.array([0.,0.])))),
        ('Reject time moves backward', lambda f: rejects(f, [2,1], [1,1], 2, 1)),
        ('Reject negative cost', lambda f: rejects(f, [0], [-1], 2, 1)),
        ('Reject negative refill', lambda f: rejects(f, [0], [1], 2, -1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [0,0,2], [2,2,2], 3, 1), dict(allowed=np.array([True,False,True]),remaining=np.array([1.,1.,1.]))))
    ]
    return run_cases(namespace, 'token_bucket', cases, mode)
