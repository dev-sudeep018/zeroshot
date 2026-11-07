def run_tests(namespace, mode="all"):
    cases = [
        ('Zero margin updates', lambda f: assert_close(f([[2]],[1],[0],0), {"weights":np.array([2.]),"bias":1,"updates":1})),
        ('Already correct', lambda f: assert_close(f([[2]],[-1],[-1],0), {"weights":np.array([-1.]),"bias":0,"updates":0})),
        ('Sequential updates', lambda f: assert_close(f([[1],[-1]],[1,-1],[0],0), {"weights":np.array([2.]),"bias":0,"updates":2})),
        ('Fractional learning rate', lambda f: assert_close(f([[2]],[-1],[0],0,.5), {"weights":np.array([-1.]),"bias":-.5,"updates":1})),
        ('Bias can learn alone', lambda f: assert_close(f([[0]],[1],[0],0), {"weights":np.array([0.]),"bias":1,"updates":1})),
        ('Two dimensions', lambda f: assert_close(f([[1,2]],[1],[0,0],0), {"weights":np.array([1.,2]),"bias":1,"updates":1})),
        ('Reject zero label', lambda f: rejects(f,[[1]],[0],[0],0)),
        ('Reject zero rate', lambda f: rejects(f,[[1]],[1],[0],0,0)),
        ('Reject dimensions', lambda f: rejects(f,[[1,2]],[1],[0],0)),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[2.]]),np.array([1.]),np.array([0.]),0),{"weights":np.array([2.]),"bias":1,"updates":1})),
    ]
    return run_cases(namespace, 'perceptron_pass', cases, mode)
