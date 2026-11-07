def run_tests(namespace, mode="all"):
    cases = [
        ('Upper outlier', lambda f: assert_close(f([0,1,2,3,20],1.5), {'quartiles':np.array([1.0, 3.0], dtype=float).reshape((2,)),'fences':np.array([-2.0, 6.0], dtype=float).reshape((2,)),'tail':np.array([0, 0, 0, 0, 1], dtype=float).reshape((5,))})),
        ('Both tails', lambda f: assert_close(f([-30,0,1,2,3,4,40],1), {'quartiles':np.array([0.5, 3.5], dtype=float).reshape((2,)),'fences':np.array([-2.5, 6.5], dtype=float).reshape((2,)),'tail':np.array([-1, 0, 0, 0, 0, 0, 1], dtype=float).reshape((7,))})),
        ('Fence equality', lambda f: assert_close(f([0,1,2],.5), {'quartiles':np.array([0.5, 1.5], dtype=float).reshape((2,)),'fences':np.array([0.0, 2.0], dtype=float).reshape((2,)),'tail':np.array([0, 0, 0], dtype=float).reshape((3,))})),
        ('No spread', lambda f: assert_close(f([2,2,2,9],0), {'quartiles':np.array([2.0, 3.75], dtype=float).reshape((2,)),'fences':np.array([2.0, 3.75], dtype=float).reshape((2,)),'tail':np.array([0, 0, 0, 1], dtype=float).reshape((4,))})),
        ('Single value', lambda f: assert_close(f([5],2), {'quartiles':np.array([5.0, 5.0], dtype=float).reshape((2,)),'fences':np.array([5.0, 5.0], dtype=float).reshape((2,)),'tail':np.array([0], dtype=float).reshape((1,))})),
        ('Unsorted values', lambda f: assert_close(f([6,-2,1,4,3],0), {'quartiles':np.array([1.0, 4.0], dtype=float).reshape((2,)),'fences':np.array([1.0, 4.0], dtype=float).reshape((2,)),'tail':np.array([1, -1, 0, 0, 0], dtype=float).reshape((5,))})),
        ('Reject negative multiplier', lambda f: rejects(f,[1,2],-1)),
        ('Reject empty', lambda f: rejects(f,[],1.5)),
        ('Reject matrix', lambda f: rejects(f,[[1,2]],1.5)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,1,2,3,20],1.5), {'quartiles':np.array([1.0, 3.0], dtype=float).reshape((2,)),'fences':np.array([-2.0, 6.0], dtype=float).reshape((2,)),'tail':np.array([0, 0, 0, 0, 1], dtype=float).reshape((5,))})),
    ]
    return run_cases(namespace, 'tukey_fences', cases, mode)
