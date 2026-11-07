def run_tests(namespace, mode="all"):
    cases = [
        ('Shrink and remove', lambda f: assert_close(f([-3,-1,0,1,3],1), np.array([-2.,0,0,0,2]))),
        ('Zero threshold', lambda f: assert_close(f([-2,0,4],0), np.array([-2.,0,4]))),
        ('All removed', lambda f: assert_close(f([-1,2],3), np.zeros(2))),
        ('Fractional shrinkage', lambda f: assert_close(f([-.75,.25,1],.5), np.array([-.25,0,.5]))),
        ('Threshold equality', lambda f: assert_close(f([-2,2],2), np.zeros(2))),
        ('One coefficient', lambda f: assert_close(f([7],2), np.array([5.]))),
        ('Reject negative threshold', lambda f: rejects(f,[1],-1)),
        ('Reject matrix', lambda f: rejects(f,[[1]],1)),
        ('Reject boolean threshold', lambda f: rejects(f,[1],True)),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([-3.,0,3]),1),np.array([-2.,0,2]))),
    ]
    return run_cases(namespace, 'soft_threshold', cases, mode)
