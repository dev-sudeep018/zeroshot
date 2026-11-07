def run_tests(namespace, mode="all"):
    cases = [
        ('Isolated outlier', lambda f: assert_close(f([1,2,2,3,20],3), {'center':2.0,'mad':1.0,'outlier':np.array([False, False, False, False, True], dtype=bool).reshape((5,))})),
        ('Zero MAD', lambda f: assert_close(f([4,4,4,9],2), {'center':4.0,'mad':0.0,'outlier':np.array([False, False, False, True], dtype=bool).reshape((4,))})),
        ('Strict boundary', lambda f: assert_close(f([-2,0,2],1), {'center':0.0,'mad':2.0,'outlier':np.array([False, False, False], dtype=bool).reshape((3,))})),
        ('Even sample', lambda f: assert_close(f([1,2,4,8],2), {'center':3.0,'mad':1.5,'outlier':np.array([False, False, False, True], dtype=bool).reshape((4,))})),
        ('Zero threshold', lambda f: assert_close(f([1,2,3],0), {'center':2.0,'mad':1.0,'outlier':np.array([True, False, True], dtype=bool).reshape((3,))})),
        ('Constant sample', lambda f: assert_close(f([7,7,7],4), {'center':7.0,'mad':0.0,'outlier':np.array([False, False, False], dtype=bool).reshape((3,))})),
        ('Reject negative threshold', lambda f: rejects(f,[1,2],-1)),
        ('Reject nonfinite', lambda f: rejects(f,[1,np.nan],2)),
        ('Reject boolean data', lambda f: rejects(f,[True,False],2)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,2,2,3,20],3), {'center':2.0,'mad':1.0,'outlier':np.array([False, False, False, False, True], dtype=bool).reshape((5,))})),
    ]
    return run_cases(namespace, 'median_outliers', cases, mode)
