def run_tests(namespace, mode="all"):
    cases = [
        ('Rectangular map', lambda f: assert_close(f([[[1,2,3],[6,4,5]]]), {'coordinates':np.array([[1, 0]], dtype='int64'),'score':np.array([6.0], dtype='float64')})),
        ('Tied maxima', lambda f: assert_close(f([[[0,3],[3,0]]]), {'coordinates':np.array([[0, 1]], dtype='int64'),'score':np.array([3.0], dtype='float64')})),
        ('All negative', lambda f: assert_close(f([[[-5,-2],[-3,-4]]]), {'coordinates':np.array([[0, 1]], dtype='int64'),'score':np.array([-2.0], dtype='float64')})),
        ('Two examples', lambda f: assert_close(f([[[1,0]],[[0,2]]]), {'coordinates':np.array([[0, 0], [0, 1]], dtype='int64'),'score':np.array([1.0, 2.0], dtype='float64')})),
        ('Single pixel', lambda f: assert_close(f([[[7]]]), {'coordinates':np.array([[0, 0]], dtype='int64'),'score':np.array([7.0], dtype='float64')})),
        ('Uniform map', lambda f: assert_close(f(np.ones((1,3,2))), {'coordinates':np.array([[0, 0]], dtype='int64'),'score':np.array([1.0], dtype='float64')})),
        ('Reject missing batch axis', lambda f: rejects(f, [[1,2]])),
        ('Reject empty image', lambda f: rejects(f, np.empty((1,0,2)))),
        ('Reject nonfinite score', lambda f: rejects(f, [[[np.nan]]])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[[1,2,3],[6,4,5]]]), {'coordinates':np.array([[1, 0]], dtype='int64'),'score':np.array([6.0], dtype='float64')})),
    ]
    return run_cases(namespace, 'heatmap_peaks', cases, mode)
