def run_tests(namespace, mode="all"):
    cases = [
        ('Select first column', lambda f: assert_close(f([[.1,.2],[.3,.4]],[True,False]), {'event':0.4,'rows':np.array([0.25, 0.7499999999999999], dtype=float).reshape((2,))})),
        ('Select all columns', lambda f: assert_close(f([[.1,.2],[.3,.4]],[True,True]), {'event':1.0,'rows':np.array([0.30000000000000004, 0.7], dtype=float).reshape((2,))})),
        ('Several selected columns', lambda f: assert_close(f([[.1,.1,.2],[.2,.3,.1]],[True,False,True]), {'event':0.5999999999999999,'rows':np.array([0.5, 0.5], dtype=float).reshape((2,))})),
        ('Single cell', lambda f: assert_close(f([[1]],[True]), {'event':1.0,'rows':np.array([1.0], dtype=float).reshape((1,))})),
        ('Zero row', lambda f: assert_close(f([[0,0],[.4,.6]],[False,True]), {'event':0.6,'rows':np.array([0.0, 1.0], dtype=float).reshape((2,))})),
        ('Sparse support', lambda f: assert_close(f([[.5,0],[0,.5]],[False,True]), {'event':0.5,'rows':np.array([0.0, 1.0], dtype=float).reshape((2,))})),
        ('Reject zero event', lambda f: rejects(f,[[1,0]],[False,True])),
        ('Reject mask shape', lambda f: rejects(f,[[.5,.5]],[True])),
        ('Reject invalid total', lambda f: rejects(f,[[.2]],[True])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[.1,.2],[.3,.4]],[True,False]), {'event':0.4,'rows':np.array([0.25, 0.7499999999999999], dtype=float).reshape((2,))})),
    ]
    return run_cases(namespace, 'condition_joint_columns', cases, mode)
