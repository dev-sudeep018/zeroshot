def run_tests(namespace, mode="all"):
    cases = [
        ('Both inside margin', lambda f: assert_close(f([[1],[-1]],[1,-1],[0],0), {"loss":1,"weights":np.array([-1.]),"bias":0})),
        ('At the kink', lambda f: assert_close(f([[1]],[1],[1],0), {"loss":0,"weights":np.array([0.]),"bias":0})),
        ('Satisfied margin', lambda f: assert_close(f([[2]],[1],[1],0), {"loss":0,"weights":np.array([0.]),"bias":0})),
        ('Wrong prediction', lambda f: assert_close(f([[2]],[-1],[1],0), {"loss":3,"weights":np.array([2.]),"bias":1})),
        ('Average over all samples', lambda f: assert_close(f([[.5],[2]],[1,1],[1],0), {"loss":.25,"weights":np.array([-.25]),"bias":-.5})),
        ('Multiple columns', lambda f: assert_close(f([[1,2]],[1],[0,0],0), {"loss":1,"weights":np.array([-1.,-2]),"bias":-1})),
        ('Reject zero label', lambda f: rejects(f,[[1]],[0],[0],0)),
        ('Reject wrong feature count', lambda f: rejects(f,[[1,2]],[1],[0],0)),
        ('Reject nonfinite bias', lambda f: rejects(f,[[1]],[1],[0],np.inf)),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[1.],[-1.]]),np.array([1.,-1]),np.array([0.]),0),{"loss":1,"weights":np.array([-1.]),"bias":0})),
    ]
    return run_cases(namespace, 'hinge_gradient', cases, mode)
