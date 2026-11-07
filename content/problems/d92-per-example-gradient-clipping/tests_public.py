def run_tests(namespace, mode="all"):
    cases = [
        ('Large and small rows', lambda f: assert_close(f([[3,4],[0,1]],2), {'clipped':np.array([[1.2000000000000002, 1.6], [0.0, 1.0]], dtype='float64'),'scale':np.array([0.4, 1.0], dtype='float64'),'mean':np.array([0.6000000000000001, 1.3], dtype='float64')})),
        ('Zero row', lambda f: assert_close(f([[0,0],[3,4]],1), {'clipped':np.array([[0.0, 0.0], [0.6000000000000001, 0.8]], dtype='float64'),'scale':np.array([1.0, 0.2], dtype='float64'),'mean':np.array([0.30000000000000004, 0.4], dtype='float64')})),
        ('Already bounded', lambda f: assert_close(f([[1,0],[0,1]],2), {'clipped':np.array([[1.0, 0.0], [0.0, 1.0]], dtype='float64'),'scale':np.array([1.0, 1.0], dtype='float64'),'mean':np.array([0.5, 0.5], dtype='float64')})),
        ('Opposing rows', lambda f: assert_close(f([[10,0],[-2,0]],1), {'clipped':np.array([[1.0, 0.0], [-1.0, 0.0]], dtype='float64'),'scale':np.array([0.1, 0.5], dtype='float64'),'mean':np.array([0.0, 0.0], dtype='float64')})),
        ('Exact boundary', lambda f: assert_close(f([[3,4]],5), {'clipped':np.array([[3.0, 4.0]], dtype='float64'),'scale':np.array([1.0], dtype='float64'),'mean':np.array([3.0, 4.0], dtype='float64')})),
        ('One parameter', lambda f: assert_close(f([[2],[-4],[0]],2), {'clipped':np.array([[2.0], [-2.0], [0.0]], dtype='float64'),'scale':np.array([1.0, 0.5, 1.0], dtype='float64'),'mean':np.array([0.0], dtype='float64')})),
        ('Reject zero norm cap', lambda f: rejects(f, [[1]],0)),
        ('Reject negative cap', lambda f: rejects(f, [[1]],-1)),
        ('Reject vector gradient', lambda f: rejects(f, [1,2],1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[3,4],[0,1]],2), {'clipped':np.array([[1.2000000000000002, 1.6], [0.0, 1.0]], dtype='float64'),'scale':np.array([0.4, 1.0], dtype='float64'),'mean':np.array([0.6000000000000001, 1.3], dtype='float64')})),
    ]
    return run_cases(namespace, 'clip_example_gradients', cases, mode)
