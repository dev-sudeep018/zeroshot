def run_tests(namespace, mode="all"):
    cases = [
        ('Full residual trace', lambda f: assert_close(f([1,2],[0,0,0],[0,1],0.5,1), dict(advantages=np.array([2.,2.]),targets=np.array([2.,2.])))),
        ('One-step residuals', lambda f: assert_close(f([1,2],[2,4,8],[0,0],0.5,0), dict(advantages=np.array([1.,2.]),targets=np.array([3.,6.])))),
        ('Half trace decay', lambda f: assert_close(f([1,2],[2,4,8],[0,0],0.5,0.5), dict(advantages=np.array([1.5,2.]),targets=np.array([3.5,6.])))),
        ('Terminal cuts both terms', lambda f: assert_close(f([1,2],[2,4,8],[1,0],0.5,1), dict(advantages=np.array([-1.,2.]),targets=np.array([1.,6.])))),
        ('Undiscounted terminal return', lambda f: assert_close(f([1,2],[5,6,7],[0,1],1,1), dict(advantages=np.array([-2.,-4.]),targets=np.array([3.,2.])))),
        ('Zero discount', lambda f: assert_close(f([2],[9,7],[0],0,1), dict(advantages=np.array([-7.]),targets=np.array([2.])))),
        ('Perfect value estimate', lambda f: assert_close(f([1,2],[3,2,0],[0,1],1,0.7), dict(advantages=np.zeros(2),targets=np.array([3.,2.])))),
        ('Reject missing bootstrap value', lambda f: rejects(f, [1],[0],[0],0.9,0.9)),
        ('Reject invalid decay', lambda f: rejects(f, [1],[0,0],[0],0.9,-0.1)),
        ('Reject invalid flags', lambda f: rejects(f, [1],[0,0],[0.5],0.9,0.9)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1,2],[0,0,0],[0,1],0.5,1), dict(advantages=np.array([2.,2.]),targets=np.array([2.,2.])))),
        ('Huge current value retains terminal reward', lambda f: assert_close(f([1],[1e30,0],[1],.9,1)["targets"], np.array([1.]))),
        ('Residual retains a small reward', lambda f: assert_close(f([1],[1e30,1e30],[0],1,0)["advantages"], np.array([1.])))
    ]
    return run_cases(namespace, 'generalized_advantages', cases, mode)
