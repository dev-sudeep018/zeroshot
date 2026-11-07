def run_tests(namespace, mode="all"):
    cases = [
        ('Swap two observations', lambda f: assert_close(f([0,2],1,[[0,1],[1,0]]), {"observed":-2,"null":np.array([-2.,2]),"p_value":1})),
        ('No null as extreme', lambda f: assert_close(f([0,0,2,2],2,[[0,2,1,3],[3,1,2,0]]), {"observed":-2,"null":np.array([0.,0]),"p_value":1/3})),
        ('One extreme null', lambda f: assert_close(f([0,0,2,2],2,[[0,1,2,3],[0,2,1,3]]), {"observed":-2,"null":np.array([-2.,0]),"p_value":2/3})),
        ('Zero observed difference', lambda f: assert_close(f([0,2,1,1],2,[[0,2,1,3]]), {"observed":0,"null":np.array([-1.]),"p_value":1})),
        ('Unequal sizes', lambda f: assert_close(f([0,2,4],1,[[2,1,0]]), {"observed":-3,"null":np.array([3.]),"p_value":1})),
        ('Repeated null draws', lambda f: assert_close(f([0,0,2,2],2,[[0,2,1,3],[0,2,1,3]]), {"observed":-2,"null":np.array([0.,0]),"p_value":1/3})),
        ('Reject repeated index', lambda f: rejects(f,[0,2],1,[[0,0]])),
        ('Reject empty group', lambda f: rejects(f,[0,2],0,[[0,1]])),
        ('Reject width', lambda f: rejects(f,[0,2],1,[[0]])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([0.,2]),1,np.array([[0,1],[1,0]])),{"observed":-2,"null":np.array([-2.,2]),"p_value":1})),
    ]
    return run_cases(namespace, 'permutation_mean_test', cases, mode)
