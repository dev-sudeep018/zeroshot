def run_tests(namespace, mode="all"):
    cases = [
        ('Swap hidden neurons', lambda f: assert_close(f([[1,2],[3,4]],[5,6],[[7],[8]],[1,0]), {'input_weights':np.array([[2.0, 1.0], [4.0, 3.0]], dtype='float64'),'hidden_bias':np.array([6.0, 5.0], dtype='float64'),'output_weights':np.array([[8.0], [7.0]], dtype='float64')})),
        ('Identity order', lambda f: assert_close(f([[1,2]],[3,4],[[5],[6]],[0,1]), {'input_weights':np.array([[1.0, 2.0]], dtype='float64'),'hidden_bias':np.array([3.0, 4.0], dtype='float64'),'output_weights':np.array([[5.0], [6.0]], dtype='float64')})),
        ('Three-neuron cycle', lambda f: assert_close(f([[1,2,3]],[4,5,6],[[7],[8],[9]],[2,0,1]), {'input_weights':np.array([[3.0, 1.0, 2.0]], dtype='float64'),'hidden_bias':np.array([6.0, 4.0, 5.0], dtype='float64'),'output_weights':np.array([[9.0], [7.0], [8.0]], dtype='float64')})),
        ('Multiple outputs', lambda f: assert_close(f([[1,2]],[0,1],[[2,3],[4,5]],[1,0]), {'input_weights':np.array([[2.0, 1.0]], dtype='float64'),'hidden_bias':np.array([1.0, 0.0], dtype='float64'),'output_weights':np.array([[4.0, 5.0], [2.0, 3.0]], dtype='float64')})),
        ('Single neuron', lambda f: assert_close(f([[2]],[3],[[4,5]],[0]), {'input_weights':np.array([[2.0]], dtype='float64'),'hidden_bias':np.array([3.0], dtype='float64'),'output_weights':np.array([[4.0, 5.0]], dtype='float64')})),
        ('Negative weights', lambda f: assert_close(f([[-1,2]],[3,-4],[[-5],[6]],[1,0]), {'input_weights':np.array([[2.0, -1.0]], dtype='float64'),'hidden_bias':np.array([-4.0, 3.0], dtype='float64'),'output_weights':np.array([[6.0], [-5.0]], dtype='float64')})),
        ('Reject repeated index', lambda f: rejects(f, [[1,2]],[0,0],[[1],[2]],[0,0])),
        ('Reject bad outgoing width', lambda f: rejects(f, [[1,2]],[0,0],[[1]],[1,0])),
        ('Reject fractional order', lambda f: rejects(f, [[1,2]],[0,0],[[1],[2]],[0,0.5])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[1,2],[3,4]],[5,6],[[7],[8]],[1,0]), {'input_weights':np.array([[2.0, 1.0], [4.0, 3.0]], dtype='float64'),'hidden_bias':np.array([6.0, 5.0], dtype='float64'),'output_weights':np.array([[8.0], [7.0]], dtype='float64')})),
    ]
    return run_cases(namespace, 'permute_hidden', cases, mode)
