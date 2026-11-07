def run_tests(namespace, mode="all"):
    cases = [
        ('Unit scale', lambda f: assert_close(f([[0]],[[0]],[[2]],[[3]]),{"mean":np.array([[3.]]),"log_variance":np.array([[3.]])})),
        ('Zero noise', lambda f: assert_close(f([[9]],[[0]],[[0]],[[3]]),{"mean":np.array([[3.]]),"log_variance":np.array([[0.]])})),
        ('Variance four', lambda f: assert_close(f([[0]],[[np.log(4)]],[[2]],[[3]]),{"mean":np.array([[3.]]),"log_variance":np.array([[6.]])})),
        ('Negative noise', lambda f: assert_close(f([[0]],[[0]],[[-2]],[[3]]),{"mean":np.array([[3.]]),"log_variance":np.array([[-3.]])})),
        ('Zero upstream', lambda f: assert_close(f([[0]],[[0]],[[2]],[[0]]),{"mean":np.array([[0.]]),"log_variance":np.array([[0.]])})),
        ('Mean value does not affect derivative', lambda f: assert_close(f([[100]],[[0]],[[2]],[[3]]),{"mean":np.array([[3.]]),"log_variance":np.array([[3.]])})),
        ('Independent feature signs', lambda f: assert_close(f([[0,0]],[[0,0]],[[1,-1]],[[2,4]]),{"mean":np.array([[2.,4.]]),"log_variance":np.array([[1.,-2.]])})),
        ('Reject broadcast noise', lambda f: rejects(f,[[0,0]],[[0,0]],[[1]],[[1,1]])),
        ('Reject invalid variance', lambda f: rejects(f,[[0]],[[100]],[[1]],[[1]])),
        ('Reject nonfinite noise', lambda f: rejects(f,[[0]],[[0]],[[np.nan]],[[1]])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[0]],[[0]],[[2]],[[3]]),{"mean":np.array([[3.]]),"log_variance":np.array([[3.]])})),
    ]
    return run_cases(namespace, 'reparameterization_backward', cases, mode)
