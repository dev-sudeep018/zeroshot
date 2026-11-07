def run_tests(namespace, mode="all"):
    cases = [
        ('Inside and outside band', lambda f: assert_close(f([0,2,5],[1,1,2],1), {'loss':0.6666666666666666,'gradient':np.array([0.0, 0.0, 0.3333333333333333], dtype=float).reshape((3,))})),
        ('Boundary gradients', lambda f: assert_close(f([-1,1],[0,0],1), {'loss':0.0,'gradient':np.array([0.0, 0.0], dtype=float).reshape((2,))})),
        ('Zero tolerance', lambda f: assert_close(f([-2,0,3],[0,0,0],0), {'loss':1.6666666666666667,'gradient':np.array([-0.3333333333333333, 0.0, 0.3333333333333333], dtype=float).reshape((3,))})),
        ('All tolerated', lambda f: assert_close(f([1,2],[1.2,2.2],.5), {'loss':0.0,'gradient':np.array([0.0, 0.0], dtype=float).reshape((2,))})),
        ('Negative residual', lambda f: assert_close(f([-3],[1],2), {'loss':2.0,'gradient':np.array([-1.0], dtype=float).reshape((1,))})),
        ('Unequal targets', lambda f: assert_close(f([2,4,1],[0,5,1],.25), {'loss':0.8333333333333334,'gradient':np.array([0.3333333333333333, -0.3333333333333333, 0.0], dtype=float).reshape((3,))})),
        ('Reject negative tolerance', lambda f: rejects(f,[1],[0],-1)),
        ('Reject mismatched lengths', lambda f: rejects(f,[1,2],[0],1)),
        ('Reject boolean tolerance', lambda f: rejects(f,[1],[0],True)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,2,5],[1,1,2],1), {'loss':0.6666666666666666,'gradient':np.array([0.0, 0.0, 0.3333333333333333], dtype=float).reshape((3,))})),
    ]
    return run_cases(namespace, 'epsilon_insensitive_loss', cases, mode)
