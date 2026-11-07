def run_tests(namespace, mode="all"):
    cases = [
        ('Filter then scale', lambda f: assert_close(f([[[[1,2],[3,4]]]],[[[1]]],[[2]]),np.array([[[[2.,4.],[6.,8.]]]]))),
        ('Do not flip the spatial kernel', lambda f: assert_close(f([[[[1,2],[3,4]]]],[[[1,0],[0,-1]]],[[1]]),np.array([[[[-3.]]]]))),
        ('Mix two independent channels', lambda f: assert_close(f([[[[1]],[[10]]]],[[[2]],[[3]]],[[1,1],[1,-1]]),np.array([[[[32.]],[[-28.]]]]))),
        ('Rectangular valid kernel', lambda f: assert_close(f([[[[1,2,3],[4,5,6]]]],[[[1,2]]],[[1]]),np.array([[[[5.,8.],[14.,17.]]]]))),
        ('Identity channel mixing', lambda f: assert_close(f([[[[2]],[[7]]]],[[[3]],[[2]]],np.eye(2)),np.array([[[[6.]],[[14.]]]]))),
        ('Batch isolation', lambda f: assert_close(f(np.array([[[[2]]],[[[4]]]]),[[[3]]],[[1]]),np.array([[[[6.]]],[[[12.]]]]))),
        ('Zero pointwise weights', lambda f: assert_close(f(np.ones((1,2,3,3)),np.ones((2,2,2)),np.zeros((3,2))),np.zeros((1,3,2,2)))),
        ('Reject oversized kernel', lambda f: rejects(f,np.ones((1,1,2,2)),np.ones((1,3,1)),[[1]])),
        ('Reject depthwise channel mismatch', lambda f: rejects(f,np.ones((1,2,2,2)),np.ones((1,1,1)),[[1,1]])),
        ('Reject pointwise channel mismatch', lambda f: rejects(f,np.ones((1,2,2,2)),np.ones((2,1,1)),[[1]])),
        ('Reject missing batch axis', lambda f: rejects(f,np.ones((1,2,2)),np.ones((1,1,1)),[[1]])),
        ('No mutation', lambda f: assert_close(unchanged(f,np.ones((1,1,2,2)),np.ones((1,2,2)),np.ones((1,1))),np.full((1,1,1,1),4.)))
    ]
    return run_cases(namespace, 'depthwise_separable', cases, mode)
