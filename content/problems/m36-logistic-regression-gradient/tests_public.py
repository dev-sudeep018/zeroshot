def run_tests(namespace, mode="all"):
    cases = [
        ('Zero logits', lambda f: assert_close(f([[1],[3]],[0,1],[0],0), {"loss":np.log(2),"weights":np.array([-.5]),"bias":0})),
        ('Bias-only residual', lambda f: assert_close(f([[0],[0]],[1,1],[3],0), {"loss":np.log(2),"weights":np.array([0.]),"bias":-.5})),
        ('Confident correct predictions', lambda f: assert_close(f([[1],[-1]],[1,0],[1000],0), {"loss":0,"weights":np.array([0.]),"bias":0})),
        ('Confident wrong predictions', lambda f: assert_close(f([[1],[-1]],[0,1],[1000],0), {"loss":1000,"weights":np.array([1.]),"bias":0})),
        ('Two feature columns', lambda f: assert_close(f([[1,2]],[1],[0,0],0), {"loss":np.log(2),"weights":np.array([-.5,-1]),"bias":-.5})),
        ('Nonzero bias', lambda f: assert_close(f([[0]],[1],[0],np.log(3)), {"loss":np.log(4/3),"weights":np.array([0.]),"bias":-.25})),
        ('Reject fractional label', lambda f: rejects(f,[[1]],[.5],[0],0)),
        ('Reject dimension mismatch', lambda f: rejects(f,[[1,2]],[1],[0],0)),
        ('Reject boolean bias', lambda f: rejects(f,[[1]],[1],[0],True)),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[1.],[3.]]),np.array([0.,1]),np.array([0.]),0),{"loss":np.log(2),"weights":np.array([-.5]),"bias":0})),
    ]
    return run_cases(namespace, 'logistic_gradient', cases, mode)
