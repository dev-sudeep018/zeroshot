def run_tests(namespace, mode="all"):
    cases = [
        ('Two update sources', lambda f: assert_close(f([2,-4],[1,-2],0.1,0.5), {'weights':np.array([1.7999999999999998, -3.5999999999999996], dtype='float64'),'optimizer_delta':np.array([-0.1, 0.2], dtype='float64'),'decay_delta':np.array([-0.1, 0.2], dtype='float64')})),
        ('Decay only', lambda f: assert_close(f([2,-2],[0,0],0.5,0.2), {'weights':np.array([1.8, -1.8], dtype='float64'),'optimizer_delta':np.array([-0.0, -0.0], dtype='float64'),'decay_delta':np.array([-0.2, 0.2], dtype='float64')})),
        ('No decay', lambda f: assert_close(f([1,2],[3,4],0.1,0), {'weights':np.array([0.7, 1.6], dtype='float64'),'optimizer_delta':np.array([-0.30000000000000004, -0.4], dtype='float64'),'decay_delta':np.array([-0.0, -0.0], dtype='float64')})),
        ('Zero rate', lambda f: assert_close(f([1],[2],0,1), {'weights':np.array([1.0], dtype='float64'),'optimizer_delta':np.array([-0.0], dtype='float64'),'decay_delta':np.array([-0.0], dtype='float64')})),
        ('Zero parameters', lambda f: assert_close(f([0],[2],0.5,1), {'weights':np.array([-1.0], dtype='float64'),'optimizer_delta':np.array([-1.0], dtype='float64'),'decay_delta':np.array([-0.0], dtype='float64')})),
        ('Full shrink factor', lambda f: assert_close(f([3],[1],1,1), {'weights':np.array([-1.0], dtype='float64'),'optimizer_delta':np.array([-1.0], dtype='float64'),'decay_delta':np.array([-3.0], dtype='float64')})),
        ('Reject different lengths', lambda f: rejects(f, [1,2],[1],0.1,0.1)),
        ('Reject negative decay', lambda f: rejects(f, [1],[1],0.1,-0.1)),
        ('Reject invalid rate', lambda f: rejects(f, [1],[1],2,0.1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [2,-4],[1,-2],0.1,0.5), {'weights':np.array([1.7999999999999998, -3.5999999999999996], dtype='float64'),'optimizer_delta':np.array([-0.1, 0.2], dtype='float64'),'decay_delta':np.array([-0.1, 0.2], dtype='float64')})),
    ]
    return run_cases(namespace, 'decoupled_decay', cases, mode)
