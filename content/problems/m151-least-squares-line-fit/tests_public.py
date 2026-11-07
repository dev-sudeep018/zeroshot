def run_tests(namespace, mode="all"):
    cases = [
        ('Exact line', lambda f: assert_close(f([0,1,2],[1,3,5]), {'slope':2.0,'intercept':1.0,'residuals':np.array([0.0, 0.0, 0.0], dtype=float).reshape((3,)),'squared_error':0.0})),
        ('Noisy line', lambda f: assert_close(f([1,2,3],[2,3,5]), {'slope':1.5,'intercept':0.3333333333333335,'residuals':np.array([0.16666666666666652, -0.3333333333333335, 0.16666666666666607], dtype=float).reshape((3,)),'squared_error':0.16666666666666652})),
        ('Negative slope', lambda f: assert_close(f([0,2,4],[5,3,1]), {'slope':-1.0,'intercept':5.0,'residuals':np.array([0.0, 0.0, 0.0], dtype=float).reshape((3,)),'squared_error':0.0})),
        ('Constant target', lambda f: assert_close(f([1,2,3],[4,4,4]), {'slope':0.0,'intercept':4.0,'residuals':np.array([0.0, 0.0, 0.0], dtype=float).reshape((3,)),'squared_error':0.0})),
        ('Unsorted inputs', lambda f: assert_close(f([3,0,2],[7,1,5]), {'slope':2.0,'intercept':0.9999999999999996,'residuals':np.array([0.0, 4.440892098500626e-16, 0.0], dtype=float).reshape((3,)),'squared_error':1.9721522630525295e-31})),
        ('Repeated inputs', lambda f: assert_close(f([0,0,1,1],[1,2,3,4]), {'slope':2.0,'intercept':1.5,'residuals':np.array([-0.5, 0.5, -0.5, 0.5], dtype=float).reshape((4,)),'squared_error':1.0})),
        ('Reject constant input', lambda f: rejects(f,[1,1],[2,3])),
        ('Reject length mismatch', lambda f: rejects(f,[1,2],[1,2,3])),
        ('Reject one observation', lambda f: rejects(f,[1],[2])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,1,2],[1,3,5]), {'slope':2.0,'intercept':1.0,'residuals':np.array([0.0, 0.0, 0.0], dtype=float).reshape((3,)),'squared_error':0.0})),
    ]
    return run_cases(namespace, 'fit_least_squares_line', cases, mode)
