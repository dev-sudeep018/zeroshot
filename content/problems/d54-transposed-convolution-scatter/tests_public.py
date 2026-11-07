def run_tests(namespace, mode="all"):
    cases = [
        ('One scatter', lambda f: assert_close(f([2],[1,3],1),np.array([2.,6.]))),
        ('Overlap adds', lambda f: assert_close(f([1,2],[1,1],1),np.array([1.,3.,2.]))),
        ('Separated segments', lambda f: assert_close(f([1,2],[1,3],2),np.array([1.,3.,2.,6.]))),
        ('Uncovered zeros', lambda f: assert_close(f([1,2],[3],2),np.array([3.,0.,6.]))),
        ('Signed cancellation', lambda f: assert_close(f([1,-1],[1,1],1),np.array([1.,0.,-1.]))),
        ('No reversal', lambda f: assert_close(f([1],[2,3,4],1),np.array([2.,3.,4.]))),
        ('Zero input', lambda f: assert_close(f([0,0],[1,2],1),np.zeros(3))),
        ('Reject zero stride', lambda f: rejects(f,[1],[1],0)),
        ('Reject oversized output', lambda f: rejects(f,np.ones(8),[1],10000)),
        ('Reject empty signal', lambda f: rejects(f,[],[1],1)),
        ('Reject boolean kernel', lambda f: rejects(f,[1],[True],1)),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[2],[1,3],1),np.array([2.,6.]))),
    ]
    return run_cases(namespace, 'transposed_convolution', cases, mode)
