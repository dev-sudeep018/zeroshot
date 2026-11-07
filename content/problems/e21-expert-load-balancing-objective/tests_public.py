def run_tests(namespace, mode="all"):
    cases = [
        ('Uniform tied logits', lambda f: assert_close(f([[0,0]]),{"fractions":np.array([1.,0.]),"probabilities":np.array([.5,.5]),"loss":1})),
        ('Balanced preferences', lambda f: assert_close(f([[np.log(3),0],[0,np.log(3)]]),{"fractions":np.array([.5,.5]),"probabilities":np.array([.5,.5]),"loss":1})),
        ('Confident shared preference', lambda f: assert_close(f([[np.log(3),0],[np.log(3),0]]),{"fractions":np.array([1.,0.]),"probabilities":np.array([.75,.25]),"loss":1.5})),
        ('One expert', lambda f: assert_close(f([[2],[-3]]),{"fractions":np.array([1.]),"probabilities":np.array([1.]),"loss":1})),
        ('Extreme collapse', lambda f: assert_close(f([[1000,-1000,-1000]])["loss"],3)),
        ('Loss can be below one', lambda f: assert_close(f([[np.log(1.5),0],[np.log(1.5),0],[-1000,0]])["loss"],14/15)),
        ('Index-order ties', lambda f: assert_close(f([[0,2,2],[0,2,2]])["fractions"],np.array([0.,1.,0.]))),
        ('Row shift invariance', lambda f: assert_close(f([[1000,1000],[-1000,-1000]])["probabilities"],np.array([.5,.5]))),
        ('Reject empty tokens', lambda f: rejects(f,np.empty((0,2)))),
        ('Reject vector input', lambda f: rejects(f,[1,2])),
        ('Reject nonfinite logits', lambda f: rejects(f,[[np.inf,0]])),
        ('No mutation', lambda f: assert_close(unchanged(f,np.zeros((2,2)))["fractions"],np.array([1.,0.])))
    ]
    return run_cases(namespace, 'load_balance', cases, mode)
