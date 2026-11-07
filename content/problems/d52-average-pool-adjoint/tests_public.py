def run_tests(namespace, mode="all"):
    cases = [
        ('One window', lambda f: assert_close(f([[4]],(2,2),2,1),np.ones((2,2)))),
        ('Overlap counts', lambda f: assert_close(f(np.ones((2,2))*4,(3,3),2,1),np.array([[1.,2.,1.],[2.,4.,2.],[1.,2.,1.]]))),
        ('Uncovered tail', lambda f: assert_close(f([[4]],(3,3),2,2),np.array([[1.,1.,0.],[1.,1.,0.],[0.,0.,0.]]))),
        ('Unit kernel', lambda f: assert_close(f([[1,2],[3,4]],(2,2),1,1),np.array([[1.,2.],[3.,4.]]))),
        ('Signed gradients', lambda f: assert_close(f([[4,-4]],(2,3),2,1),np.array([[1.,0.,-1.],[1.,0.,-1.]]))),
        ('Sparse stride', lambda f: assert_close(f([[2,3]],(1,3),1,2),np.array([[2.,0.,3.]]))),
        ('Zero upstream', lambda f: assert_close(f(np.zeros((2,2)),(3,3),2,1),np.zeros((3,3)))),
        ('Reject shape mismatch', lambda f: rejects(f,[[1]],(3,3),2,1)),
        ('Reject oversized allocation', lambda f: rejects(f,[[1]],(100000,100000),100000,1)),
        ('Reject boolean stride', lambda f: rejects(f,[[1]],(1,1),1,True)),
        ('Reject oversized kernel', lambda f: rejects(f,[[1]],(1,1),2,1)),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[4]],(2,2),2,1),np.ones((2,2)))),
    ]
    return run_cases(namespace, 'average_pool_backward', cases, mode)
