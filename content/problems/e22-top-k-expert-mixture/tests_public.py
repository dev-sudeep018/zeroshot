def run_tests(namespace, mode="all"):
    cases = [
        ('Choose one expert', lambda f: assert_close(f([[1,3,2]],[[[10],[20],[30]]],1),{"output":np.array([[20.]]),"indices":np.array([[1]]),"weights":np.array([[1.]])})),
        ('Mix two selected experts', lambda f: assert_close(f([[0,np.log(3),-10]],[[[4],[8],[100]]],2),{"output":np.array([[7.]]),"indices":np.array([[1,0]]),"weights":np.array([[.75,.25]])})),
        ('Resolve tied gates', lambda f: assert_close(f([[0,0,0]],[[[2],[6],[100]]],2),{"output":np.array([[4.]]),"indices":np.array([[0,1]]),"weights":np.array([[.5,.5]])})),
        ('Independent token routes', lambda f: assert_close(f([[2,1],[0,1]],[[[2,4],[10,20]],[[3,6],[7,9]]],1)["output"],np.array([[2.,4.],[7.,9.]]))),
        ('All experts', lambda f: assert_close(f([[0,0,0]],[[[2],[4],[9]]],3)["output"],np.array([[5.]]))),
        ('Stable extreme gates', lambda f: assert_close(f([[1000,-1000]],[[[2],[9]]],2)["weights"],np.array([[1.,0.]]))),
        ('Integer route indices', lambda f: assert_close(f([[0,0]],[[[1],[2]]],1)["indices"].dtype.kind in "iu",True)),
        ('Reject invalid k', lambda f: [rejects(f,[[0,0]],[[[1],[2]]],v) for v in (0,3,True,1.5,2**4096)]),
        ('Reject token mismatch', lambda f: rejects(f,[[0,0]],np.ones((2,2,1)),1)),
        ('Reject expert mismatch', lambda f: rejects(f,[[0,0]],np.ones((1,3,1)),1)),
        ('Reject nonfinite expert output', lambda f: rejects(f,[[0]],[[[np.nan]]],1)),
        ('No mutation', lambda f: assert_close(unchanged(f,np.zeros((1,2)),np.array([[[2.],[6.]]]),2)["output"],np.array([[4.]])))
    ]
    return run_cases(namespace, 'mix_experts', cases, mode)
