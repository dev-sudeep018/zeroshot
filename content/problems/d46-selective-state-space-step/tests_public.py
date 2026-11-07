def run_tests(namespace, mode="all"):
    cases = [
        ('Write into empty memory', lambda f: assert_close(f([[2]],[[[0]]],[[0]],[[3]],[[4]],[[.5]]),{"state":np.array([[[3.]]]),"output":np.array([[12.]])})),
        ('No elapsed time', lambda f: assert_close(f([[99]],[[[2]]],[[-1]],[[3]],[[4]],[[0]]),{"state":np.array([[[2.]]]),"output":np.array([[8.]])})),
        ('Half the old memory', lambda f: assert_close(f([[0]],[[[8]]],[[-np.log(2)]],[[1]],[[1]],[[1]]),{"state":np.array([[[4.]]]),"output":np.array([[4.]])})),
        ('Read sums state coordinates', lambda f: assert_close(f([[1]],[[[0,0]]],[[0,0]],[[2,3]],[[4,5]],[[1]]),{"state":np.array([[[2.,3.]]]),"output":np.array([[23.]])})),
        ('Zero readout', lambda f: assert_close(f([[1]],[[[0]]],[[0]],[[2]],[[0]],[[1]]),{"state":np.array([[[2.]]]),"output":np.array([[0.]])})),
        ('Channels have distinct time', lambda f: assert_close(f([[2,2]],[[[0],[0]]],[[0],[0]],[[1]],[[1]],[[1,2]]),{"state":np.array([[[2.],[4.]]]),"output":np.array([[2.,4.]])})),
        ('Negative input write', lambda f: assert_close(f([[-2]],[[[1]]],[[0]],[[3]],[[1]],[[1]]),{"state":np.array([[[-5.]]]),"output":np.array([[-5.]])})),
        ('Reject positive decay', lambda f: rejects(f,[[1]],[[[0]]],[[1]],[[1]],[[1]],[[1]])),
        ('Reject negative time', lambda f: rejects(f,[[1]],[[[0]]],[[0]],[[1]],[[1]],[[-1]])),
        ('Reject missing state axis', lambda f: rejects(f,[[1]],[[0]],[[0]],[[1]],[[1]],[[1]])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[2]],[[[0]]],[[0]],[[3]],[[4]],[[.5]]),{"state":np.array([[[3.]]]),"output":np.array([[12.]])})),
    ]
    return run_cases(namespace, 'state_space_step', cases, mode)
