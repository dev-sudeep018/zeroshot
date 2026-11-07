def run_tests(namespace, mode="all"):
    cases = [
        ('Separated groups', lambda f: assert_close(f([1,3,6,8],[0,0,1,1],2), {'grand_mean':4.5,'group_mean':np.array([2.0, 7.0], dtype=float).reshape((2,)),'between':25.0,'within':4.0,'total':29.0})),
        ('One group', lambda f: assert_close(f([1,2,4],[0,0,0],1), {'grand_mean':2.3333333333333335,'group_mean':np.array([2.3333333333333335], dtype=float).reshape((1,)),'between':0.0,'within':4.666666666666666,'total':4.666666666666666})),
        ('Each value a group', lambda f: assert_close(f([1,3,8],[0,1,2],3), {'grand_mean':4.0,'group_mean':np.array([1.0, 3.0, 8.0], dtype=float).reshape((3,)),'between':26.0,'within':0.0,'total':26.0})),
        ('Unequal sizes', lambda f: assert_close(f([0,2,4,10],[0,0,0,1],2), {'grand_mean':4.0,'group_mean':np.array([2.0, 10.0], dtype=float).reshape((2,)),'between':48.0,'within':8.0,'total':56.0})),
        ('Interleaved labels', lambda f: assert_close(f([1,8,3,6],[0,1,0,1],2), {'grand_mean':4.5,'group_mean':np.array([2.0, 7.0], dtype=float).reshape((2,)),'between':25.0,'within':4.0,'total':29.0})),
        ('Constant data', lambda f: assert_close(f([5,5,5],[0,1,1],2), {'grand_mean':5.0,'group_mean':np.array([5.0, 5.0], dtype=float).reshape((2,)),'between':0.0,'within':0.0,'total':0.0})),
        ('Reject absent group', lambda f: rejects(f,[1,2],[0,0],2)),
        ('Reject outside label', lambda f: rejects(f,[1,2],[0,2],2)),
        ('Reject length mismatch', lambda f: rejects(f,[1,2],[0],1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,3,6,8],[0,0,1,1],2), {'grand_mean':4.5,'group_mean':np.array([2.0, 7.0], dtype=float).reshape((2,)),'between':25.0,'within':4.0,'total':29.0})),
    ]
    return run_cases(namespace, 'anova_partition', cases, mode)
