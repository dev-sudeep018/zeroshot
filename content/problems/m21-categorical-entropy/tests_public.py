def run_tests(namespace, mode="all"):
    cases = [
        ('Fair binary choice', lambda f: assert_close(f([.5,.5]), np.log(2))),
        ('Certain outcome', lambda f: assert_close(f([1,0]), 0)),
        ('Four equal outcomes', lambda f: assert_close(f([.25]*4), np.log(4))),
        ('Skewed choice', lambda f: assert_close(f([.25,.75]), -.25*np.log(.25)-.75*np.log(.75))),
        ('Zero padding', lambda f: assert_close(f([0,.5,0,.5]), np.log(2))),
        ('Singleton', lambda f: assert_close(f([1]), 0)),
        ('Reject negative probability', lambda f: rejects(f,[-.1,1.1])),
        ('Reject wrong total', lambda f: rejects(f,[.2,.3])),
        ('Reject empty vector', lambda f: rejects(f,[])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([.5,.5])),np.log(2))),
    ]
    return run_cases(namespace, 'categorical_entropy', cases, mode)
