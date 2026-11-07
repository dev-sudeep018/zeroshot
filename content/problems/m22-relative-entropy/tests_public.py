def run_tests(namespace, mode="all"):
    cases = [
        ('Equal distributions', lambda f: assert_close(f([.2,.8],[.2,.8]), 0)),
        ('Certain versus uniform', lambda f: assert_close(f([1,0],[.5,.5]), np.log(2))),
        ('Directed mismatch', lambda f: assert_close(f([.5,.5],[.25,.75]), .5*np.log(4/3))),
        ('Reverse direction', lambda f: assert_close(f([.25,.75],[.5,.5]), .25*np.log(.5)+.75*np.log(1.5))),
        ('Zero support term', lambda f: assert_close(f([0,.5,.5],[.5,.25,.25]), np.log(2))),
        ('Singleton', lambda f: assert_close(f([1],[1]), 0)),
        ('Reject unsupported q', lambda f: rejects(f,[1,0],[0,1])),
        ('Reject unequal shape', lambda f: rejects(f,[1],[.5,.5])),
        ('Reject unnormalized p', lambda f: rejects(f,[.2,.2],[.5,.5])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([1.,0]),np.array([.5,.5])),np.log(2))),
    ]
    return run_cases(namespace, 'relative_entropy', cases, mode)
