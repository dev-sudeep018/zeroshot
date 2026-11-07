def run_tests(namespace, mode="all"):
    cases = [
        ('Two resamples', lambda f: assert_close(f([0,2],[[0,0],[1,1]]), {"means":np.array([0.,2]),"standard_error":np.sqrt(2)})),
        ('Repeated index draws', lambda f: assert_close(f([1,4,7],[[0,0,2],[1,1,1],[2,2,2]]), {"means":np.array([3.,4,7]),"standard_error":np.sqrt(13/3)})),
        ('Same means', lambda f: assert_close(f([0,2],[[0,1],[1,0]]), {"means":np.array([1.,1]),"standard_error":0})),
        ('Constant values', lambda f: assert_close(f([3,3],[[0,0],[1,1],[0,1]]), {"means":np.array([3.,3,3]),"standard_error":0})),
        ('Single observation', lambda f: assert_close(f([9],[[0],[0]]), {"means":np.array([9.,9]),"standard_error":0})),
        ('Negative observations', lambda f: assert_close(f([-2,2],[[0,0],[0,1],[1,1]]), {"means":np.array([-2.,0,2]),"standard_error":2})),
        ('Reject one resample', lambda f: rejects(f,[0,2],[[0,1]])),
        ('Reject width', lambda f: rejects(f,[0,2],[[0],[1]])),
        ('Reject invalid index', lambda f: rejects(f,[0,2],[[0,2],[0,1]])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([0.,2]),np.array([[0,0],[1,1]])),{"means":np.array([0.,2]),"standard_error":np.sqrt(2)})),
    ]
    return run_cases(namespace, 'bootstrap_means', cases, mode)
