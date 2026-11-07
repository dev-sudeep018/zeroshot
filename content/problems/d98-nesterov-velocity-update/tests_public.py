def run_tests(namespace, mode="all"):
    cases = [
        ('Lookahead correction', lambda f: assert_close(f([2],[1],[3],0.5,0.1), {'lookahead':np.array([2.5], dtype='float64'),'velocity':np.array([0.19999999999999996], dtype='float64'),'weights':np.array([2.2], dtype='float64')})),
        ('No momentum', lambda f: assert_close(f([1,2],[3,4],[2,1],0,0.5), {'lookahead':np.array([1.0, 2.0], dtype='float64'),'velocity':np.array([-1.0, -0.5], dtype='float64'),'weights':np.array([0.0, 1.5], dtype='float64')})),
        ('No previous velocity', lambda f: assert_close(f([2],[0],[1],0.9,0.1), {'lookahead':np.array([2.0], dtype='float64'),'velocity':np.array([-0.1], dtype='float64'),'weights':np.array([1.9], dtype='float64')})),
        ('Zero rate still moves', lambda f: assert_close(f([1],[2],[3],0.5,0), {'lookahead':np.array([2.0], dtype='float64'),'velocity':np.array([1.0], dtype='float64'),'weights':np.array([2.0], dtype='float64')})),
        ('Opposing gradient', lambda f: assert_close(f([1],[1],[-2],1,0.5), {'lookahead':np.array([2.0], dtype='float64'),'velocity':np.array([2.0], dtype='float64'),'weights':np.array([3.0], dtype='float64')})),
        ('Two coordinates', lambda f: assert_close(f([1,-2],[0.5,-1],[2,-3],0.8,0.1), {'lookahead':np.array([1.4, -2.8], dtype='float64'),'velocity':np.array([0.2, -0.5], dtype='float64'),'weights':np.array([1.2, -2.5], dtype='float64')})),
        ('Reject shape mismatch', lambda f: rejects(f, [1,2],[0],[1],0.9,0.1)),
        ('Reject invalid momentum', lambda f: rejects(f, [1],[0],[1],1.1,0.1)),
        ('Reject negative rate', lambda f: rejects(f, [1],[0],[1],0.9,-0.1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [2],[1],[3],0.5,0.1), {'lookahead':np.array([2.5], dtype='float64'),'velocity':np.array([0.19999999999999996], dtype='float64'),'weights':np.array([2.2], dtype='float64')})),
    ]
    return run_cases(namespace, 'nesterov_step', cases, mode)
