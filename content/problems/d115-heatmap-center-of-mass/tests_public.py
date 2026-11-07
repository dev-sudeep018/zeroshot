def run_tests(namespace, mode="all"):
    cases = [
        ('Uniform map', lambda f: assert_close(f(np.ones((1,2,3))), {'mass':np.array([6.0], dtype='float64'),'centers':np.array([[0.5, 1.0]], dtype='float64')})),
        ('Single peak', lambda f: assert_close(f([[[0,0],[0,2]]]), {'mass':np.array([2.0], dtype='float64'),'centers':np.array([[1.0, 1.0]], dtype='float64')})),
        ('Two weighted peaks', lambda f: assert_close(f([[[1,0,3]]]), {'mass':np.array([4.0], dtype='float64'),'centers':np.array([[0.0, 1.5]], dtype='float64')})),
        ('Two examples', lambda f: assert_close(f([[[1,0],[0,0]],[[0,0],[0,4]]]), {'mass':np.array([1.0, 4.0], dtype='float64'),'centers':np.array([[0.0, 0.0], [1.0, 1.0]], dtype='float64')})),
        ('One pixel', lambda f: assert_close(f([[[5]]]), {'mass':np.array([5.0], dtype='float64'),'centers':np.array([[0.0, 0.0]], dtype='float64')})),
        ('Non-normalized map', lambda f: assert_close(f([[[1,2],[3,4]]]), {'mass':np.array([10.0], dtype='float64'),'centers':np.array([[0.7, 0.6]], dtype='float64')})),
        ('Reject zero mass', lambda f: rejects(f, np.zeros((1,2,2)))),
        ('Reject negative mass', lambda f: rejects(f, [[[1,-0.1]]])),
        ('Reject missing batch axis', lambda f: rejects(f, [[1,2]])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, np.ones((1,2,3))), {'mass':np.array([6.0], dtype='float64'),'centers':np.array([[0.5, 1.0]], dtype='float64')})),
    ]
    return run_cases(namespace, 'heatmap_centers', cases, mode)
