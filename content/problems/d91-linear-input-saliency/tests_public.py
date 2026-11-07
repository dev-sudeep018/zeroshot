def run_tests(namespace, mode="all"):
    cases = [
        ('Different classes', lambda f: assert_close(f([[1,2],[3,4]],[[1,-1],[2,3]],[0,1]), {'scores':np.array([5.0, 9.0], dtype='float64'),'gradient':np.array([[1.0, 2.0], [-1.0, 3.0]], dtype='float64'),'input_times_gradient':np.array([[1.0, 4.0], [-3.0, 12.0]], dtype='float64')})),
        ('Zero input', lambda f: assert_close(f([[0,0]],[[2],[-3]],[0]), {'scores':np.array([0.0], dtype='float64'),'gradient':np.array([[2.0, -3.0]], dtype='float64'),'input_times_gradient':np.array([[0.0, -0.0]], dtype='float64')})),
        ('One feature', lambda f: assert_close(f([[2],[-2]],[[3,4]],[1,0]), {'scores':np.array([8.0, -6.0], dtype='float64'),'gradient':np.array([[4.0], [3.0]], dtype='float64'),'input_times_gradient':np.array([[8.0], [-6.0]], dtype='float64')})),
        ('Negative weights', lambda f: assert_close(f([[1,-2]],[[-1],[2]],[0]), {'scores':np.array([-5.0], dtype='float64'),'gradient':np.array([[-1.0, 2.0]], dtype='float64'),'input_times_gradient':np.array([[-1.0, -4.0]], dtype='float64')})),
        ('Same class', lambda f: assert_close(f([[1],[2],[3]],[[2]],[0,0,0]), {'scores':np.array([2.0, 4.0, 6.0], dtype='float64'),'gradient':np.array([[2.0], [2.0], [2.0]], dtype='float64'),'input_times_gradient':np.array([[2.0], [4.0], [6.0]], dtype='float64')})),
        ('Zero weight', lambda f: assert_close(f([[3,4]],[[0,1],[0,2]],[0]), {'scores':np.array([0.0], dtype='float64'),'gradient':np.array([[0.0, 0.0]], dtype='float64'),'input_times_gradient':np.array([[0.0, 0.0]], dtype='float64')})),
        ('Reject class outside range', lambda f: rejects(f, [[1]],[[1]],[1])),
        ('Reject class batch mismatch', lambda f: rejects(f, [[1],[2]],[[1]],[0])),
        ('Reject feature mismatch', lambda f: rejects(f, [[1,2]],[[1]],[0])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[1,2],[3,4]],[[1,-1],[2,3]],[0,1]), {'scores':np.array([5.0, 9.0], dtype='float64'),'gradient':np.array([[1.0, 2.0], [-1.0, 3.0]], dtype='float64'),'input_times_gradient':np.array([[1.0, 4.0], [-3.0, 12.0]], dtype='float64')})),
    ]
    return run_cases(namespace, 'linear_saliency', cases, mode)
