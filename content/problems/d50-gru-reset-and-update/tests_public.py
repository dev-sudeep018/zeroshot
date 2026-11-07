def run_tests(namespace, mode="all"):
    cases = [
        ('Empty state', lambda f: assert_close(f([[0]],[[0]],[[0]],[[0]],[[0]]),np.array([[0.]]))),
        ('Half retention', lambda f: assert_close(f([[2]],[[0]],[[0]],[[0]],[[0]]),np.array([[1.]]))),
        ('Reset scales drive', lambda f: assert_close(f([[0]],[[0]],[[0]],[[0]],[[2]]),np.array([[.5*np.tanh(1)]]))),
        ('Retain state', lambda f: assert_close(f([[3]],[[1000]],[[0]],[[9]],[[9]]),np.array([[3.]]))),
        ('Replace state', lambda f: assert_close(f([[3]],[[-1000]],[[0]],[[1]],[[0]]),np.array([[np.tanh(1)]]))),
        ('Reset removes recurrence', lambda f: assert_close(f([[0]],[[0]],[[-1000]],[[1]],[[999]]),np.array([[.5*np.tanh(1)]]))),
        ('Feature independence', lambda f: assert_close(f([[2,-2]],[[0,0]],[[0,0]],[[0,0]],[[0,0]]),np.array([[1.,-1.]]))),
        ('Reject broadcast candidate', lambda f: rejects(f,[[1,2]],[[0,0]],[[0,0]],[[0]],[[0,0]])),
        ('Reject nonfinite state', lambda f: rejects(f,[[np.nan]],[[0]],[[0]],[[0]],[[0]])),
        ('Reject missing batch', lambda f: rejects(f,[0],[0],[0],[0],[0])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[0]],[[0]],[[0]],[[0]],[[0]]),np.array([[0.]]))),
    ]
    return run_cases(namespace, 'gru_step', cases, mode)
