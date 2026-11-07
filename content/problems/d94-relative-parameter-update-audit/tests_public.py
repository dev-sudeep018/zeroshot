def run_tests(namespace, mode="all"):
    cases = [
        ('Two scales', lambda f: assert_close(f([[3,4],[0,2]],[[0.3,0.4],[0,1]],0.01), {'weight_norm':np.array([5.0, 2.0], dtype='float64'),'update_norm':np.array([0.5, 1.0], dtype='float64'),'ratio':np.array([0.1, 0.5], dtype='float64')})),
        ('Zero weights', lambda f: assert_close(f([[0,0]],[[1,0]],0.5), {'weight_norm':np.array([0.0], dtype='float64'),'update_norm':np.array([1.0], dtype='float64'),'ratio':np.array([2.0], dtype='float64')})),
        ('Zero update', lambda f: assert_close(f([[2,3]],[[0,0]],0.1), {'weight_norm':np.array([3.605551275463989], dtype='float64'),'update_norm':np.array([0.0], dtype='float64'),'ratio':np.array([0.0], dtype='float64')})),
        ('Both zero', lambda f: assert_close(f([[0]],[[0]],1e-6), {'weight_norm':np.array([0.0], dtype='float64'),'update_norm':np.array([0.0], dtype='float64'),'ratio':np.array([0.0], dtype='float64')})),
        ('Denominator floor', lambda f: assert_close(f([[0.01]],[[0.02]],0.1), {'weight_norm':np.array([0.01], dtype='float64'),'update_norm':np.array([0.02], dtype='float64'),'ratio':np.array([0.19999999999999998], dtype='float64')})),
        ('Negative changes', lambda f: assert_close(f([[-3,-4]],[[-0.3,-0.4]],0.01), {'weight_norm':np.array([5.0], dtype='float64'),'update_norm':np.array([0.5], dtype='float64'),'ratio':np.array([0.1], dtype='float64')})),
        ('Reject mismatch', lambda f: rejects(f, [[1,2]],[[1]],0.1)),
        ('Reject zero epsilon', lambda f: rejects(f, [[1]],[[1]],0)),
        ('Reject large epsilon', lambda f: rejects(f, [[1]],[[1]],2)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[3,4],[0,2]],[[0.3,0.4],[0,1]],0.01), {'weight_norm':np.array([5.0, 2.0], dtype='float64'),'update_norm':np.array([0.5, 1.0], dtype='float64'),'ratio':np.array([0.1, 0.5], dtype='float64')})),
    ]
    return run_cases(namespace, 'update_ratios', cases, mode)
