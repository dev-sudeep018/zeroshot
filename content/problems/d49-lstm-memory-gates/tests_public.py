def run_tests(namespace, mode="all"):
    cases = [
        ('Empty memory', lambda f: assert_close(f([[0]],[[0]],[[0]],[[0]],[[0]]),{"cell":np.array([[0.]]),"hidden":np.array([[0.]])})),
        ('Half retention', lambda f: assert_close(f([[2]],[[0]],[[0]],[[0]],[[0]]),{"cell":np.array([[1.]]),"hidden":np.array([[.5*np.tanh(1)]])})),
        ('Candidate write', lambda f: assert_close(f([[0]],[[0]],[[0]],[[0]],[[1]]),{"cell":np.array([[.5*np.tanh(1)]]),"hidden":np.array([[.5*np.tanh(.5*np.tanh(1))]])})),
        ('Closed output gate', lambda f: assert_close(f([[2]],[[0]],[[0]],[[-1000]],[[0]]),{"cell":np.array([[1.]]),"hidden":np.array([[0.]])})),
        ('Closed forget gate', lambda f: assert_close(f([[8]],[[0]],[[-1000]],[[0]],[[0]]),{"cell":np.array([[0.]]),"hidden":np.array([[0.]])})),
        ('Negative memory', lambda f: assert_close(f([[-2]],[[0]],[[0]],[[0]],[[0]]),{"cell":np.array([[-1.]]),"hidden":np.array([[-.5*np.tanh(1)]])})),
        ('Batch memory', lambda f: assert_close(f([[2],[4]],[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]]),{"cell":np.array([[1.],[2.]]),"hidden":.5*np.tanh(np.array([[1.],[2.]]))})),
        ('Reject broadcast gate', lambda f: rejects(f,[[1,2]],[[0]],[[0,0]],[[0,0]],[[0,0]])),
        ('Reject vector cell', lambda f: rejects(f,[1],[0],[0],[0],[0])),
        ('Reject nonfinite gate', lambda f: rejects(f,[[0]],[[np.inf]],[[0]],[[0]],[[0]])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[0]],[[0]],[[0]],[[0]],[[0]]),{"cell":np.array([[0.]]),"hidden":np.array([[0.]])})),
    ]
    return run_cases(namespace, 'lstm_step', cases, mode)
