def run_tests(namespace, mode="all"):
    cases = [
        ('Potential increase', lambda f: assert_close(f([1],[2],[6],[0],0.5), np.array([2.]))),
        ('Terminal potential is zero', lambda f: assert_close(f([1],[2],[100],[1],0.5), np.array([-1.]))),
        ('Two-step telescoping', lambda f: assert_close(f([0,0],[2,4],[4,9],[0,1],0.5), np.array([0.,-4.]))),
        ('Zero potentials', lambda f: assert_close(f([1,-2],[0,0],[0,0],[0,1],0.9), np.array([1.,-2.]))),
        ('Zero discount', lambda f: assert_close(f([3],[2],[99],[0],0), np.array([1.]))),
        ('Undiscounted difference', lambda f: assert_close(f([0],[4],[7],[0],1), np.array([3.]))),
        ('Negative potentials', lambda f: assert_close(f([-1],[-3],[-2],[0],0.5), np.array([1.]))),
        ('Reject mismatched potential', lambda f: rejects(f, [1],[0,0],[0],[0],0.9)),
        ('Reject invalid terminal', lambda f: rejects(f, [1],[0],[0],[2],0.9)),
        ('Reject nonfinite potential', lambda f: rejects(f, [1],[np.nan],[0],[0],0.9)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1],[2],[6],[0],0.5), np.array([2.])))
    ]
    return run_cases(namespace, 'shape_rewards', cases, mode)
