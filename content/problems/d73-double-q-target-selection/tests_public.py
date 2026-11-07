def run_tests(namespace, mode="all"):
    cases = [
        ('Estimators disagree', lambda f: assert_close(f([1],[[5,2]],[[3,9]],[0],0.5), dict(actions=np.array([0]),targets=np.array([2.5])))),
        ('Lowest-index tie', lambda f: assert_close(f([0],[[4,4]],[[2,8]],[0],1), dict(actions=np.array([0]),targets=np.array([2.])))),
        ('Terminal has no bootstrap', lambda f: assert_close(f([7],[[1,3]],[[8,20]],[1],0.9), dict(actions=np.array([1]),targets=np.array([7.])))),
        ('Independent batch rows', lambda f: assert_close(f([1,2],[[1,4],[5,0]],[[10,6],[3,9]],[0,0],0.5), dict(actions=np.array([1,0]),targets=np.array([4.,3.5])))),
        ('Negative action values', lambda f: assert_close(f([0],[[-4,-2]],[[-1,-7]],[0],1), dict(actions=np.array([1]),targets=np.array([-7.])))),
        ('Single action', lambda f: assert_close(f([2],[[99]],[[8]],[0],0.25), dict(actions=np.array([0]),targets=np.array([4.])))),
        ('Zero discount retains selected action', lambda f: assert_close(f([3],[[0,5]],[[2,8]],[0],0), dict(actions=np.array([1]),targets=np.array([3.])))),
        ('Reject estimator mismatch', lambda f: rejects(f, [1],[[1,2]],[[1]],[0],0.9)),
        ('Reject reward batch mismatch', lambda f: rejects(f, [1,2],[[1]],[[1]],[0,0],0.9)),
        ('Reject invalid discount', lambda f: rejects(f, [1],[[1]],[[1]],[0],True)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1],[[5,2]],[[3,9]],[0],0.5), dict(actions=np.array([0]),targets=np.array([2.5]))))
    ]
    return run_cases(namespace, 'double_q_targets', cases, mode)
