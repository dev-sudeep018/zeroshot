def run_tests(namespace, mode="all"):
    cases = [
        ('One key only', lambda f: assert_close(f([[2]],[[3]],[[4]],[[5]]),{"queries":np.zeros((1,1)),"keys":np.zeros((1,1)),"values":np.array([[5.]])})),
        ('Uniform weights still have score derivative', lambda f: assert_close(f([[0]],[[0],[1]],[[0],[4]],[[1]]),{"queries":np.array([[1.]]),"keys":np.zeros((2,1)),"values":np.array([[.5],[.5]])})),
        ('Equal keys can receive opposite gradients', lambda f: assert_close(f([[1]],[[0],[0]],[[1],[3]],[[2]]),{"queries":np.zeros((1,1)),"keys":np.array([[-1.],[1.]]),"values":np.ones((2,1))})),
        ('Constant values cancel score gradient', lambda f: assert_close(f([[1]],[[0],[1]],[[3],[3]],[[1]]),{"queries":np.zeros((1,1)),"keys":np.zeros((2,1)),"values":np.array([[1/(1+np.e)],[np.e/(1+np.e)]])})),
        ('Feature scaling in backward', lambda f: assert_close(f([[0,0]],[[0,0],[1,1]],[[0],[4]],[[1]]),{"queries":np.array([[1/np.sqrt(2),1/np.sqrt(2)]]),"keys":np.zeros((2,2)),"values":np.array([[.5],[.5]])})),
        ('Queries share value gradients', lambda f: assert_close(f([[0],[0]],[[0],[1]],[[0],[4]],[[1],[3]]),{"queries":np.array([[1.],[3.]]),"keys":np.zeros((2,1)),"values":np.array([[2.],[2.]])})),
        ('No objective gradient', lambda f: assert_close(f([[1]],[[1]],[[1]],[[0]]),{"queries":np.zeros((1,1)),"keys":np.zeros((1,1)),"values":np.zeros((1,1))})),
        ('Reject key width', lambda f: rejects(f,[[1,2]],[[1]],[[1]],[[1]])),
        ('Reject upstream width', lambda f: rejects(f,[[1]],[[1]],[[1,2]],[[1]])),
        ('Reject nonfinite values', lambda f: rejects(f,[[1]],[[1]],[[np.nan]],[[1]])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[2]],[[3]],[[4]],[[5]]),{"queries":np.zeros((1,1)),"keys":np.zeros((1,1)),"values":np.array([[5.]])})),
    ]
    return run_cases(namespace, 'attention_backward', cases, mode)
