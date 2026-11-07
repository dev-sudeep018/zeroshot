def run_tests(namespace, mode="all"):
    cases = [
        ('Center and tails', lambda f: assert_close(f([-3,-1,0,1,3],1), {'per_item':np.array([2.5, 0.5, 0.0, 0.5, 2.5], dtype='float64'),'derivative':np.array([-1.0, -1.0, 0.0, 1.0, 1.0], dtype='float64'),'mean_loss':1.2,'mean_gradient':np.array([-0.2, -0.2, 0.0, 0.2, 0.2], dtype='float64')})),
        ('All quadratic', lambda f: assert_close(f([-0.5,0.5],1), {'per_item':np.array([0.125, 0.125], dtype='float64'),'derivative':np.array([-0.5, 0.5], dtype='float64'),'mean_loss':0.125,'mean_gradient':np.array([-0.25, 0.25], dtype='float64')})),
        ('Exact thresholds', lambda f: assert_close(f([-2,2],2), {'per_item':np.array([2.0, 2.0], dtype='float64'),'derivative':np.array([-2.0, 2.0], dtype='float64'),'mean_loss':2.0,'mean_gradient':np.array([-1.0, 1.0], dtype='float64')})),
        ('Asymmetric errors', lambda f: assert_close(f([-4,0,1],2), {'per_item':np.array([6.0, 0.0, 0.5], dtype='float64'),'derivative':np.array([-2.0, 0.0, 1.0], dtype='float64'),'mean_loss':2.1666666666666665,'mean_gradient':np.array([-0.6666666666666666, 0.0, 0.3333333333333333], dtype='float64')})),
        ('Zero residual', lambda f: assert_close(f([0],0.1), {'per_item':np.array([0.0], dtype='float64'),'derivative':np.array([0.0], dtype='float64'),'mean_loss':0.0,'mean_gradient':np.array([0.0], dtype='float64')})),
        ('Small threshold', lambda f: assert_close(f([-1,1],0.25), {'per_item':np.array([0.21875, 0.21875], dtype='float64'),'derivative':np.array([-0.25, 0.25], dtype='float64'),'mean_loss':0.21875,'mean_gradient':np.array([-0.125, 0.125], dtype='float64')})),
        ('Reject zero threshold', lambda f: rejects(f, [1],0)),
        ('Reject matrix residuals', lambda f: rejects(f, [[1]],1)),
        ('Reject boolean residual', lambda f: rejects(f, [True],1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [-3,-1,0,1,3],1), {'per_item':np.array([2.5, 0.5, 0.0, 0.5, 2.5], dtype='float64'),'derivative':np.array([-1.0, -1.0, 0.0, 1.0, 1.0], dtype='float64'),'mean_loss':1.2,'mean_gradient':np.array([-0.2, -0.2, 0.0, 0.2, 0.2], dtype='float64')})),
    ]
    return run_cases(namespace, 'huber_residuals', cases, mode)
