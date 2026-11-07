def run_tests(namespace, mode="all"):
    cases = [
        ('No signal', lambda f: assert_close(f([[0],[0]],[0],[[1]],[[1]],[0]),np.zeros((2,1)))),
        ('One input', lambda f: assert_close(f([[1]],[0],[[1]],[[0]],[0]),np.array([[np.tanh(1)]]))),
        ('Carry memory', lambda f: assert_close(f([[0],[0]],[1],[[0]],[[1]],[0]),np.array([[np.tanh(1)],[np.tanh(np.tanh(1))]]))),
        ('No recurrence', lambda f: assert_close(f([[1],[-1]],[9],[[2]],[[0]],[0]),np.array([[np.tanh(2)],[-np.tanh(2)]]))),
        ('Bias each step', lambda f: assert_close(f([[0],[0]],[0],[[0]],[[0]],[1]),np.full((2,1),np.tanh(1)))),
        ('Feature projection', lambda f: assert_close(f([[1,2]],[0],[[1],[2]],[[0]],[0]),np.array([[np.tanh(5)]]))),
        ('Hidden width', lambda f: assert_close(f([[1]],[0,0],[[1,-1]],np.zeros((2,2)),[0,0]),np.array([[np.tanh(1),-np.tanh(1)]]))),
        ('Reject recurrent width', lambda f: rejects(f,[[1]],[0],[[1]],[[1,2]],[0])),
        ('Reject empty time', lambda f: rejects(f,np.empty((0,1)),[0],[[1]],[[1]],[0])),
        ('Reject nonfinite state', lambda f: rejects(f,[[0]],[np.nan],[[1]],[[1]],[0])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[0],[0]],[0],[[1]],[[1]],[0]),np.zeros((2,1)))),
    ]
    return run_cases(namespace, 'recurrent_states', cases, mode)
