def run_tests(namespace, mode="all"):
    cases = [
        ('Closed branch', lambda f: assert_close(f([[[1,3]]],[[2,2]],[[7,7]],[[0,0]]),np.zeros((1,1,2)))),
        ('Constant token', lambda f: assert_close(f([[[5,5]]],[[9,9]],[[2,3]],[[4,-1]]),np.array([[[8.,-3.]]]))),
        ('Normalize then scale', lambda f: assert_close(f([[[1,3]]],[[2,2]],[[0,0]],[[1,1]],1),np.array([[[-np.sqrt(2),np.sqrt(2)]]]))),
        ('Shift is gated', lambda f: assert_close(f([[[0]]],[[0]],[[3]],[[2]]),np.array([[[6.]]]))),
        ('Sequence statistics stay separate', lambda f: assert_close(f([[[0,2],[8,8]]],[[1,1]],[[0,0]],[[1,1]],1),np.array([[[-1/np.sqrt(2),1/np.sqrt(2)],[0,0]]]))),
        ('Independent batch conditioning', lambda f: assert_close(f([[[1]],[[1]]],[[0],[0]],[[2],[3]],[[1],[2]]),np.array([[[2.]],[[6.]]]))),
        ('No residual addition', lambda f: assert_close(f([[[8]]],[[1]],[[0]],[[1]]),np.zeros((1,1,1)))),
        ('Reject broadcast conditioning', lambda f: rejects(f,[[[1,2]]],[1,1],[[0,0]],[[1,1]])),
        ('Reject invalid epsilon', lambda f: rejects(f,[[[1]]],[[1]],[[0]],[[1]],0)),
        ('Reject nonfinite input', lambda f: rejects(f,[[[np.nan]]],[[1]],[[0]],[[1]])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[[1,3]]],[[2,2]],[[7,7]],[[0,0]]),np.zeros((1,1,2)))),
    ]
    return run_cases(namespace, 'conditional_gate', cases, mode)
