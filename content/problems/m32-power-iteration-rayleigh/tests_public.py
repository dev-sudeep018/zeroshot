def run_tests(namespace, mode="all"):
    cases = [
        ('One step', lambda f: assert_close(f([[2,0],[0,1]],[1,1],1), {"vector":np.array([2.,1.])/np.sqrt(5),"rayleigh":1.8})),
        ('No multiplication', lambda f: assert_close(f([[2,0],[0,1]],[3,4],0), {"vector":np.array([.6,.8]),"rayleigh":1.36})),
        ('Known eigenvector', lambda f: assert_close(f([[3,0],[0,1]],[1,0],4), {"vector":np.array([1.,0]),"rayleigh":3})),
        ('Negative dominant eigenvalue', lambda f: assert_close(f([[-2,0],[0,1]],[1,0],1), {"vector":np.array([-1.,0]),"rayleigh":-2})),
        ('Identity preserves direction', lambda f: assert_close(f([[1,0],[0,1]],[0,-2],5), {"vector":np.array([0.,-1]),"rayleigh":1})),
        ('Two steps', lambda f: assert_close(f([[2,0],[0,1]],[1,1],2), {"vector":np.array([4.,1.])/np.sqrt(17),"rayleigh":33/17})),
        ('Reject zero start', lambda f: rejects(f,[[1]],[0],1)),
        ('Reject zero intermediate', lambda f: rejects(f,[[0]],[1],1)),
        ('Reject nonsymmetric matrix', lambda f: rejects(f,[[1,1],[0,1]],[1,1],1)),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[2.,0],[0,1.]]),np.array([1.,1]),1),{"vector":np.array([2.,1.])/np.sqrt(5),"rayleigh":1.8})),
    ]
    return run_cases(namespace, 'power_iteration', cases, mode)
