def run_tests(namespace, mode="all"):
    cases = [
        ('Positive changes', lambda f: assert_close(f([0,0,0],[1,2,3]), {"mean_difference":2,"standard_error":1/np.sqrt(3),"t":2*np.sqrt(3),"degrees_of_freedom":2})),
        ('Zero mean change', lambda f: assert_close(f([5,5,5],[4,5,6]), {"mean_difference":0,"standard_error":1/np.sqrt(3),"t":0,"degrees_of_freedom":2})),
        ('Two pairs', lambda f: assert_close(f([0,0],[1,3]), {"mean_difference":2,"standard_error":1,"t":2,"degrees_of_freedom":1})),
        ('Reverse direction', lambda f: assert_close(f([1,2,3],[0,0,0]), {"mean_difference":-2,"standard_error":1/np.sqrt(3),"t":-2*np.sqrt(3),"degrees_of_freedom":2})),
        ('Different baselines', lambda f: assert_close(f([10,20,30],[11,22,33]), {"mean_difference":2,"standard_error":1/np.sqrt(3),"t":2*np.sqrt(3),"degrees_of_freedom":2})),
        ('Scale changes', lambda f: assert_close(f([0,0],[2,6]), {"mean_difference":4,"standard_error":2,"t":2,"degrees_of_freedom":1})),
        ('Reject constant changes', lambda f: rejects(f,[1,2],[3,4])),
        ('Reject one pair', lambda f: rejects(f,[0],[1])),
        ('Reject lengths', lambda f: rejects(f,[0,1],[1,2,3])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([0.,0]),np.array([1.,3])),{"mean_difference":2,"standard_error":1,"t":2,"degrees_of_freedom":1})),
    ]
    return run_cases(namespace, 'paired_t_statistic', cases, mode)
