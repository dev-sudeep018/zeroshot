def run_tests(namespace, mode="all"):
    cases = [
        ('Undo the scale exactly once', lambda f: assert_close(f([8,-16], 8), dict(gradients=np.array([1.,-2.]),skip_step=False))),
        ('Infinity skips whole update', lambda f: assert_close(f([2,np.inf], 2), dict(gradients=np.zeros(2),skip_step=True))),
        ('NaN skips whole update', lambda f: assert_close(f([np.nan], 1), dict(gradients=np.zeros(1),skip_step=True))),
        ('Unit scale', lambda f: assert_close(f([[1,2]], 1), dict(gradients=np.array([[1.,2.]]),skip_step=False))),
        ('Empty gradients', lambda f: assert_close(f([], 10), dict(gradients=np.array([]),skip_step=False))),
        ('Overflow after division', lambda f: assert_close(f([1e30], 1e-300), dict(gradients=np.zeros(1),skip_step=True))),
        ('Reject zero scale', lambda f: rejects(f, [1], 0)),
        ('Reject complex gradient', lambda f: rejects(f, [1j], 1)),
        ('Reject nonfinite scale', lambda f: rejects(f, [1], np.inf)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [8,-16], 8), dict(gradients=np.array([1.,-2.]),skip_step=False)))
    ]
    return run_cases(namespace, 'unscale_gradients', cases, mode)
