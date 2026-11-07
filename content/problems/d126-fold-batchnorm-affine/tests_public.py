def run_tests(namespace, mode="all"):
    cases = [
        ('Two output scales', lambda f: assert_close(f([[1,2],[3,4]],[1,2],[0,1],[3,8],[2,3],[0,1],1), {'weights':np.array([[1.0, 2.0], [3.0, 4.0]], dtype='float64'),'bias':np.array([1.0, 2.0], dtype='float64')})),
        ('Zero gamma', lambda f: assert_close(f([[2]],[3],[4],[0],[0],[7],0.1), {'weights':np.array([[0.0]], dtype='float64'),'bias':np.array([7.0], dtype='float64')})),
        ('Negative gamma', lambda f: assert_close(f([[1]],[0],[1],[3],[-2],[0],1), {'weights':np.array([[-1.0]], dtype='float64'),'bias':np.array([1.0], dtype='float64')})),
        ('Zero variance', lambda f: assert_close(f([[2]],[1],[1],[0],[1],[3],1), {'weights':np.array([[2.0]], dtype='float64'),'bias':np.array([3.0], dtype='float64')})),
        ('Rectangular affine', lambda f: assert_close(f([[1,2,3]],[0,0,0],[1,2,3],[3,3,3],[2,2,2],[0,0,0],1), {'weights':np.array([[1.0, 2.0, 3.0]], dtype='float64'),'bias':np.array([-1.0, -2.0, -3.0], dtype='float64')})),
        ('One feature', lambda f: assert_close(f([[3]],[2],[1],[8],[3],[4],1), {'weights':np.array([[3.0]], dtype='float64'),'bias':np.array([5.0], dtype='float64')})),
        ('Reject negative variance', lambda f: rejects(f, [[1]],[0],[0],[-1],[1],[0],0.1)),
        ('Reject wrong output width', lambda f: rejects(f, [[1,2]],[0],[0],[1],[1],[0],0.1)),
        ('Reject zero epsilon', lambda f: rejects(f, [[1]],[0],[0],[1],[1],[0],0)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[1,2],[3,4]],[1,2],[0,1],[3,8],[2,3],[0,1],1), {'weights':np.array([[1.0, 2.0], [3.0, 4.0]], dtype='float64'),'bias':np.array([1.0, 2.0], dtype='float64')})),
    ]
    return run_cases(namespace, 'fold_batchnorm', cases, mode)
