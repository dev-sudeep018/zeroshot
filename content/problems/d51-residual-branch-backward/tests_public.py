def run_tests(namespace, mode="all"):
    cases = [
        ('Both routes active', lambda f: assert_close(f([[2]],[[3]],[[4]]),{"input":np.array([[16.]]),"weights":np.array([[8.]])})),
        ('Branch inactive', lambda f: assert_close(f([[-2]],[[3]],[[4]]),{"input":np.array([[4.]]),"weights":np.array([[0.]])})),
        ('ReLU boundary', lambda f: assert_close(f([[0]],[[3]],[[4]]),{"input":np.array([[4.]]),"weights":np.array([[0.]])})),
        ('Sum batch', lambda f: assert_close(f([[1],[2]],[[1]],[[3],[4]]),{"input":np.array([[6.],[8.]]),"weights":np.array([[11.]])})),
        ('Zero upstream', lambda f: assert_close(f([[2]],[[3]],[[0]]),{"input":np.array([[0.]]),"weights":np.array([[0.]])})),
        ('Negative weights', lambda f: assert_close(f([[-2]],[[-3]],[[4]]),{"input":np.array([[-8.]]),"weights":np.array([[-8.]])})),
        ('Different feature masks', lambda f: assert_close(f([[2,-1]],np.eye(2),[[3,4]]),{"input":np.array([[6.,4.]]),"weights":np.array([[6.,0.],[-3.,0.]])})),
        ('Reject weight width', lambda f: rejects(f,[[1,2]],[[1]],[[1,2]])),
        ('Reject upstream broadcast', lambda f: rejects(f,[[1],[2]],[[1]],[[1]])),
        ('Reject nonfinite input', lambda f: rejects(f,[[np.inf]],[[1]],[[1]])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[2]],[[3]],[[4]]),{"input":np.array([[16.]]),"weights":np.array([[8.]])})),
    ]
    return run_cases(namespace, 'residual_backward', cases, mode)
