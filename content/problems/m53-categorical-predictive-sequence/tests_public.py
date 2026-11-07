def run_tests(namespace, mode="all"):
    cases = [
        ('Repeated category reinforces itself', lambda f: assert_close(f([1,1],[0,0]), {"probabilities":np.array([.5,2/3]),"log_probability":np.log(1/3),"posterior":np.array([3.,1])})),
        ('Switch categories', lambda f: assert_close(f([1,1],[0,1]), {"probabilities":np.array([.5,1/3]),"log_probability":np.log(1/6),"posterior":np.array([2.,2])})),
        ('Unequal prior', lambda f: assert_close(f([2,1],[1]), {"probabilities":np.array([1/3]),"log_probability":np.log(1/3),"posterior":np.array([2.,2])})),
        ('One category', lambda f: assert_close(f([.5],[0,0,0]), {"probabilities":np.ones(3),"log_probability":0,"posterior":np.array([3.5])})),
        ('Three categories', lambda f: assert_close(f([1,1,1],[0,1,2]), {"probabilities":np.array([1/3,1/4,1/5]),"log_probability":np.log(1/60),"posterior":np.array([2.,2,2])})),
        ('Reverse sequence same joint probability', lambda f: assert_close(f([1,1],[1,0]), {"probabilities":np.array([.5,1/3]),"log_probability":np.log(1/6),"posterior":np.array([2.,2])})),
        ('Reject zero concentration', lambda f: rejects(f,[1,0],[0])),
        ('Reject category outside vocabulary', lambda f: rejects(f,[1,1],[2])),
        ('Reject fractional category', lambda f: rejects(f,[1,1],[.5])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([1.,1]),np.array([0,0])),{"probabilities":np.array([.5,2/3]),"log_probability":np.log(1/3),"posterior":np.array([3.,1])})),
    ]
    return run_cases(namespace, 'categorical_predictive_sequence', cases, mode)
