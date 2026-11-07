def run_tests(namespace, mode="all"):
    cases = [
        ('Signed features', lambda f: assert_close(f([[2,-3],[0,4]],[1,-2],0.5), {'contributions':np.array([[2.0, 6.0], [0.0, -8.0]], dtype='float64'),'score':np.array([8.5, -7.5], dtype='float64')})),
        ('Bias alone', lambda f: assert_close(f([[0,0]],[4,-2],3), {'contributions':np.array([[0.0, -0.0]], dtype='float64'),'score':np.array([3.0], dtype='float64')})),
        ('Single feature', lambda f: assert_close(f([[2],[-1]],[3],-1), {'contributions':np.array([[6.0], [-3.0]], dtype='float64'),'score':np.array([5.0, -4.0], dtype='float64')})),
        ('Cancellation', lambda f: assert_close(f([[2,2]],[1,-1],0), {'contributions':np.array([[2.0, -2.0]], dtype='float64'),'score':np.array([0.0], dtype='float64')})),
        ('Fractional contributions', lambda f: assert_close(f([[0.5,2]],[-2,0.25],1), {'contributions':np.array([[-1.0, 0.5]], dtype='float64'),'score':np.array([0.5], dtype='float64')})),
        ('Two examples', lambda f: assert_close(f([[1,2,3],[3,2,1]],[1,0,-1],2), {'contributions':np.array([[1.0, 0.0, -3.0], [3.0, 0.0, -1.0]], dtype='float64'),'score':np.array([0.0, 4.0], dtype='float64')})),
        ('Reject width mismatch', lambda f: rejects(f, [[1,2]],[1],0)),
        ('Reject matrix weights', lambda f: rejects(f, [[1]],[[1]],0)),
        ('Reject boolean input', lambda f: rejects(f, [[True]],[1],0)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[2,-3],[0,4]],[1,-2],0.5), {'contributions':np.array([[2.0, 6.0], [0.0, -8.0]], dtype='float64'),'score':np.array([8.5, -7.5], dtype='float64')})),
    ]
    return run_cases(namespace, 'neuron_contributions', cases, mode)
