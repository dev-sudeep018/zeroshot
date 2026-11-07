def run_tests(namespace, mode="all"):
    cases = [
        ('Nonterminal bootstrap', lambda f: assert_close(f([1],[2],[10],[0],0.5), dict(targets=np.array([6.]),errors=np.array([4.])))),
        ('Terminal reward', lambda f: assert_close(f([1],[2],[10],[1],0.5), dict(targets=np.array([1.]),errors=np.array([-1.])))),
        ('Mixed transition batch', lambda f: assert_close(f([1,2],[0,3],[4,8],[0,1],0.5), dict(targets=np.array([3.,2.]),errors=np.array([3.,-1.])))),
        ('Zero discount', lambda f: assert_close(f([2],[5],[100],[0],0), dict(targets=np.array([2.]),errors=np.array([-3.])))),
        ('Negative future value', lambda f: assert_close(f([-1],[2],[-4],[0],0.5), dict(targets=np.array([-3.]),errors=np.array([-5.])))),
        ('Prediction already matches', lambda f: assert_close(f([2],[5],[3],[0],1), dict(targets=np.array([5.]),errors=np.array([0.])))),
        ('Rows do not form a trajectory', lambda f: assert_close(f([0,100],[0,0],[2,0],[0,1],1), dict(targets=np.array([2.,100.]),errors=np.array([2.,100.])))),
        ('Reject mismatched value', lambda f: rejects(f, [1],[0,0],[0],[0],0.9)),
        ('Reject invalid flag', lambda f: rejects(f, [1],[0],[0],[2],0.9)),
        ('Reject nonfinite next value', lambda f: rejects(f, [1],[0],[np.inf],[0],0.9)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1],[2],[10],[0],0.5), dict(targets=np.array([6.]),errors=np.array([4.]))))
    ]
    return run_cases(namespace, 'td_value_targets', cases, mode)
