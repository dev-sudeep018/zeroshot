def run_tests(namespace, mode="all"):
    cases = [
        ('Good predictions', lambda f: assert_close(f([1,2,3],[1,2,2.5]), {'residual_ss':0.25,'total_ss':2.0,'r_squared':0.875})),
        ('Mean baseline', lambda f: assert_close(f([1,2,3],[2,2,2]), {'residual_ss':2.0,'total_ss':2.0,'r_squared':0.0})),
        ('Worse than baseline', lambda f: assert_close(f([0,1],[5,5]), {'residual_ss':41.0,'total_ss':0.5,'r_squared':-81.0})),
        ('Constant perfect', lambda f: assert_close(f([2,2],[2,2]), {'residual_ss':0.0,'total_ss':0.0,'r_squared':1.0})),
        ('Constant imperfect', lambda f: assert_close(f([2,2],[2,3]), {'residual_ss':1.0,'total_ss':0.0,'r_squared':0.0})),
        ('Exact nonconstant', lambda f: assert_close(f([-1,0,3],[-1,0,3]), {'residual_ss':0.0,'total_ss':8.666666666666668,'r_squared':1.0})),
        ('Reject one target', lambda f: rejects(f,[1],[1])),
        ('Reject mismatch', lambda f: rejects(f,[1,2],[1])),
        ('Reject nonfinite prediction', lambda f: rejects(f,[1,2],[1,np.inf])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,2,3],[1,2,2.5]), {'residual_ss':0.25,'total_ss':2.0,'r_squared':0.875})),
        ('Tiny scale preserves perfect fit', lambda f: assert_close(f([1e-200,2e-200],[1e-200,2e-200])["r_squared"], 1.)),
    ]
    return run_cases(namespace, 'regression_fit_score', cases, mode)
