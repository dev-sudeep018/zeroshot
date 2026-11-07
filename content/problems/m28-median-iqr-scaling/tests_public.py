def run_tests(namespace, mode="all"):
    cases = [
        ('Fit and transform', lambda f: assert_close(f([[0],[2],[4]],[[2],[6]]), {"center":np.array([2.]),"scale":np.array([2.]),"values":np.array([[0.],[2.]])})),
        ('Constant column', lambda f: assert_close(f([[5],[5]],[[5],[7]]), {"center":np.array([5.]),"scale":np.array([1.]),"values":np.array([[0.],[2.]])})),
        ('Separate columns', lambda f: assert_close(f([[0,10],[2,14],[4,18]],[[4,10]]), {"center":np.array([2.,14.]),"scale":np.array([2.,4.]),"values":np.array([[1.,-1.]])})),
        ('Do not refit', lambda f: assert_close(f([[0],[2],[4]],[[100]]), {"center":np.array([2.]),"scale":np.array([2.]),"values":np.array([[49.]])})),
        ('Single training row', lambda f: assert_close(f([[2,3]],[[4,2]]), {"center":np.array([2.,3.]),"scale":np.array([1.,1.]),"values":np.array([[2.,-1.]])})),
        ('Even sample interpolation', lambda f: assert_close(f([[0],[2],[4],[6]],[[3]]), {"center":np.array([3.]),"scale":np.array([3.]),"values":np.array([[0.]])})),
        ('Reject features mismatch', lambda f: rejects(f,[[1,2]],[[1]])),
        ('Reject vector training', lambda f: rejects(f,[1,2],[[1]])),
        ('Reject empty rows', lambda f: rejects(f,[],[[1]])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[0.],[2.],[4.]]),np.array([[2.]])),{"center":np.array([2.]),"scale":np.array([2.]),"values":np.array([[0.]])})),
    ]
    return run_cases(namespace, 'robust_scale', cases, mode)
