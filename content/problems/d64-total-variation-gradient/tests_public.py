def run_tests(namespace, mode="all"):
    cases = [
        ('One horizontal edge', lambda f: assert_close(f([[1,4]]),{"loss":3.,"gradient":np.array([[-1.,1.]])})),
        ('Flat region', lambda f: assert_close(f([[2,2],[2,2]]),{"loss":0.,"gradient":np.zeros((2,2))})),
        ('Peak in a row', lambda f: assert_close(f([[0,2,0]]),{"loss":4.,"gradient":np.array([[-1.,2.,-1.]])})),
        ('One vertical edge', lambda f: assert_close(f([[1],[4]]),{"loss":3.,"gradient":np.array([[-1.],[1.]])})),
        ('Two-dimensional edges', lambda f: assert_close(f([[0,1],[2,3]]),{"loss":6.,"gradient":np.array([[-2.,0.],[0.,2.]])})),
        ('Single pixel', lambda f: assert_close(f([[8]]),{"loss":0.,"gradient":np.zeros((1,1))})),
        ('Reversed edge', lambda f: assert_close(f([[4,1]]),{"loss":3.,"gradient":np.array([[1.,-1.]])})),
        ('Reject vector image', lambda f: rejects(f,[1,2])),
        ('Reject empty image', lambda f: rejects(f,np.empty((0,2)))),
        ('Reject nonfinite image', lambda f: rejects(f,[[np.nan]])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[1,4]]),{"loss":3.,"gradient":np.array([[-1.,1.]])})),
    ]
    return run_cases(namespace, 'total_variation', cases, mode)
