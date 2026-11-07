def run_tests(namespace, mode="all"):
    cases = [
        ('Scalar product', lambda f: assert_close(f([[2]],[[3]],[[4]]),{"image":np.array([[12.]]),"kernel":np.array([[8.]])})),
        ('Shared scalar filter', lambda f: assert_close(f([[1,2]],[[3]],[[4,5]]),{"image":np.array([[12.,15.]]),"kernel":np.array([[14.]])})),
        ('Overlapping filter', lambda f: assert_close(f([[1,2,3]],[[2,1]],[[1,1]]),{"image":np.array([[2.,3.,1.]]),"kernel":np.array([[3.,5.]])})),
        ('Signed upstream', lambda f: assert_close(f([[1,2,3]],[[2,1]],[[1,-1]]),{"image":np.array([[2.,-1.,-1.]]),"kernel":np.array([[-1.,-1.]])})),
        ('Full image window', lambda f: assert_close(f([[1,2],[3,4]],[[1,0],[0,-1]],[[2]]),{"image":np.array([[2.,0.],[0.,-2.]]),"kernel":np.array([[2.,4.],[6.,8.]])})),
        ('Zero kernel', lambda f: assert_close(f([[2]],[[0]],[[3]]),{"image":np.array([[0.]]),"kernel":np.array([[6.]])})),
        ('Zero image', lambda f: assert_close(f([[0]],[[2]],[[3]]),{"image":np.array([[6.]]),"kernel":np.array([[0.]])})),
        ('Reject oversized kernel', lambda f: rejects(f,[[1]],[[1,2]],[[1]])),
        ('Reject upstream mismatch', lambda f: rejects(f,[[1,2]],[[1]],[[1]])),
        ('Reject nonfinite image', lambda f: rejects(f,[[np.nan]],[[1]],[[1]])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[2]],[[3]],[[4]]),{"image":np.array([[12.]]),"kernel":np.array([[8.]])})),
    ]
    return run_cases(namespace, 'convolution_backward', cases, mode)
