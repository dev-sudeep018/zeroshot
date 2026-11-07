def run_tests(namespace, mode="all"):
    cases = [
        ('Two document classes', lambda f: assert_close(f([[2,0],[0,2]],[0,1],2), {"class_log_prior":np.log(np.array([.5,.5])),"feature_log_probability":np.log(np.array([[.75,.25],[.25,.75]]))})),
        ('Empty document', lambda f: assert_close(f([[0,0]],[0],1), {"class_log_prior":np.array([0.]),"feature_log_probability":np.log(np.array([[.5,.5]]))})),
        ('Unequal class prior', lambda f: assert_close(f([[1,0],[1,0],[0,1]],[0,0,1],2), {"class_log_prior":np.log(np.array([2/3,1/3])),"feature_log_probability":np.log(np.array([[.75,.25],[1/3,2/3]]))})),
        ('Different smoothing', lambda f: assert_close(f([[2,0]],[0],1,2), {"class_log_prior":np.array([0.]),"feature_log_probability":np.log(np.array([[2/3,1/3]]))})),
        ('Single vocabulary entry', lambda f: assert_close(f([[4],[0]],[0,1],2), {"class_log_prior":np.log(np.array([.5,.5])),"feature_log_probability":np.zeros((2,1))})),
        ('Aggregate within class', lambda f: assert_close(f([[1,2],[3,0]],[0,0],1), {"class_log_prior":np.array([0.]),"feature_log_probability":np.log(np.array([[5/8,3/8]]))})),
        ('Reject missing class', lambda f: rejects(f,[[1,0]],[0],2)),
        ('Reject fractional count', lambda f: rejects(f,[[.5,1]],[0],1)),
        ('Reject zero smoothing', lambda f: rejects(f,[[1]],[0],1,0)),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[2.,0],[0,2]]),np.array([0,1]),2),{"class_log_prior":np.log(np.array([.5,.5])),"feature_log_probability":np.log(np.array([[.75,.25],[.25,.75]]))})),
    ]
    return run_cases(namespace, 'fit_multinomial_nb', cases, mode)
