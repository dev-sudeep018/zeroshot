def run_tests(namespace, mode="all"):
    cases = [
        ('Symmetric sample', lambda f: assert_close(f([-2,-1,0,1,2]), {'skewness':0.0,'excess_kurtosis':-1.3000000000000007})),
        ('Right tail', lambda f: assert_close(f([0,0,0,4]), {'skewness':1.1547005383792517,'excess_kurtosis':-0.6666666666666661})),
        ('Constant sample', lambda f: assert_close(f([3,3]), {'skewness':0.0,'excess_kurtosis':0.0})),
        ('Left tail', lambda f: assert_close(f([-4,0,0,0]), {'skewness':-1.154700538379252,'excess_kurtosis':-0.6666666666666665})),
        ('Two observations', lambda f: assert_close(f([1,7]), {'skewness':0.0,'excess_kurtosis':-2.0})),
        ('Unequal sample', lambda f: assert_close(f([1,2,3,8,9]), {'skewness':0.3236269295627415,'excess_kurtosis':-1.7127310758098253})),
        ('Reject empty', lambda f: rejects(f,[])),
        ('Reject matrix', lambda f: rejects(f,[[1,2]])),
        ('Reject nonfinite', lambda f: rejects(f,[np.nan])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[-2,-1,0,1,2]), {'skewness':0.0,'excess_kurtosis':-1.3000000000000007})),
    ]
    return run_cases(namespace, 'shape_moments', cases, mode)
