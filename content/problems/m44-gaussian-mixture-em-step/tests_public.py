def run_tests(namespace, mode="all"):
    cases = [
        ('One component fits moments', lambda f: assert_close(f([-1,1],[1],[0],[1]), {"weights":np.array([1.]),"means":np.array([0.]),"variances":np.array([1.]),"log_likelihood":-np.log(2*np.pi)-1})),
        ('Identical components preserve weights', lambda f: assert_close(f([-1,1],[.25,.75],[0,0],[1,1]), {"weights":np.array([.25,.75]),"means":np.array([0.,0]),"variances":np.array([1.,1]),"log_likelihood":-np.log(2*np.pi)-1})),
        ('Variance floor', lambda f: assert_close(f([2,2],[1],[2],[1],.1), {"weights":np.array([1.]),"means":np.array([2.]),"variances":np.array([.1]),"log_likelihood":-np.log(2*np.pi)})),
        ('Separated soft groups', lambda f: assert_close(f([-1,1],[.5,.5],[-1,1],[1,1]), {"weights":np.array([.5,.5]),"means":np.array([-np.tanh(1),np.tanh(1)]),"variances":np.full(2,1-np.tanh(1)**2),"log_likelihood":2*np.log((1+np.exp(-2))/2)-np.log(2*np.pi)})),
        ('New mean before variance', lambda f: assert_close(f([0,2],[1],[8],[4]), {"weights":np.array([1.]),"means":np.array([1.]),"variances":np.array([1.]),"log_likelihood":-np.log(8*np.pi)-12.5})),
        ('Single observation', lambda f: assert_close(f([3],[1],[1],[4],.5), {"weights":np.array([1.]),"means":np.array([3.]),"variances":np.array([.5]),"log_likelihood":-.5*(np.log(8*np.pi)+1)})),
        ('Reject zero weight', lambda f: rejects(f,[0],[0,1],[0,0],[1,1])),
        ('Reject invalid variance', lambda f: rejects(f,[0],[1],[0],[0])),
        ('Reject empty component', lambda f: rejects(f,[0],[.5,.5],[0,1000],[1,1])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([-1.,1]),np.array([1.]),np.array([0.]),np.array([1.])),{"weights":np.array([1.]),"means":np.array([0.]),"variances":np.array([1.]),"log_likelihood":-np.log(2*np.pi)-1})),
    ]
    return run_cases(namespace, 'gaussian_em_step', cases, mode)
