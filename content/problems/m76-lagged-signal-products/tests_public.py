def run_tests(namespace, mode="all"):
    cases = [
        ('Overlap normalization', lambda f: assert_close(f([1,2,3],2,"overlap"), {'value':np.array([4.666666666666667, 4.0, 3.0], dtype=float).reshape((3,)),'count':np.array([3, 2, 1], dtype=float).reshape((3,))})),
        ('Biased normalization', lambda f: assert_close(f([1,2,3],2,"biased"), {'value':np.array([4.666666666666667, 2.6666666666666665, 1.0], dtype=float).reshape((3,)),'count':np.array([3, 2, 1], dtype=float).reshape((3,))})),
        ('Constant signal', lambda f: assert_close(f([2,2,2],2,"overlap"), {'value':np.array([4.0, 4.0, 4.0], dtype=float).reshape((3,)),'count':np.array([3, 2, 1], dtype=float).reshape((3,))})),
        ('Alternating signs', lambda f: assert_close(f([1,-1,1,-1],3,"overlap"), {'value':np.array([1.0, -1.0, 1.0, -1.0], dtype=float).reshape((4,)),'count':np.array([4, 3, 2, 1], dtype=float).reshape((4,))})),
        ('Lag zero only', lambda f: assert_close(f([3,4],0,"biased"), {'value':np.array([12.5], dtype=float).reshape((1,)),'count':np.array([2], dtype=float).reshape((1,))})),
        ('Singleton', lambda f: assert_close(f([5],0,"overlap"), {'value':np.array([25.0], dtype=float).reshape((1,)),'count':np.array([1], dtype=float).reshape((1,))})),
        ('Reject lag too large', lambda f: rejects(f,[1,2],2,"overlap")),
        ('Reject unknown convention', lambda f: rejects(f,[1,2],1,"centered")),
        ('Reject negative lag', lambda f: rejects(f,[1,2],-1,"biased")),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,2,3],2,"overlap"), {'value':np.array([4.666666666666667, 4.0, 3.0], dtype=float).reshape((3,)),'count':np.array([3, 2, 1], dtype=float).reshape((3,))})),
    ]
    return run_cases(namespace, 'lag_products', cases, mode)
