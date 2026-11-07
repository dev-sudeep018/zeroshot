def run_tests(namespace, mode="all"):
    cases = [
        ('Diagonal trace', lambda f: assert_close(f([[2,0],[0,3]],[[1,1],[1,-1]]),{"estimates":np.array([5.,5.]),"mean":5.})),
        ('One inaccurate probe', lambda f: assert_close(f([[1,2],[2,3]],[[1,1]]),{"estimates":np.array([8.]),"mean":8.})),
        ('Balanced off-diagonal cancellation', lambda f: assert_close(f([[1,2],[2,3]],[[1,1],[1,-1]]),{"estimates":np.array([8.,0.]),"mean":4.})),
        ('Antisymmetric component', lambda f: assert_close(f([[1,3],[-3,2]],[[1,1],[1,-1]]),{"estimates":np.array([3.,3.]),"mean":3.})),
        ('One dimension', lambda f: assert_close(f([[7]],[[1],[-1]]),{"estimates":np.array([7.,7.]),"mean":7.})),
        ('Global sign does not change probe', lambda f: assert_close(f([[1,2],[2,3]],[[1,1],[-1,-1]]),{"estimates":np.array([8.,8.]),"mean":8.})),
        ('Zero matrix', lambda f: assert_close(f(np.zeros((2,2)),[[1,-1]]),{"estimates":np.array([0.]),"mean":0.})),
        ('Reject non-sign entries', lambda f: rejects(f,np.eye(2),[[1,0]])),
        ('Reject nonsquare matrix', lambda f: rejects(f,np.ones((2,3)),[[1,1]])),
        ('Reject empty probes', lambda f: rejects(f,np.eye(2),np.empty((0,2)))),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[2,0],[0,3]],[[1,1],[1,-1]]),{"estimates":np.array([5.,5.]),"mean":5.})),
    ]
    return run_cases(namespace, 'trace_probes', cases, mode)
