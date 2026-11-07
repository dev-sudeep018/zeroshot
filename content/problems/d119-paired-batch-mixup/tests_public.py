def run_tests(namespace, mode="all"):
    cases = [
        ('Halfway pairs', lambda f: assert_close(f([[0,2],[4,6]],[[1,0],[0,1]],[1,0],0.5), {'features':np.array([[2.0, 4.0], [2.0, 4.0]], dtype='float64'),'labels':np.array([[0.5, 0.5], [0.5, 0.5]], dtype='float64')})),
        ('Original endpoint', lambda f: assert_close(f([[1],[3]],[[1,0],[0,1]],[1,0],1), {'features':np.array([[1.0], [3.0]], dtype='float64'),'labels':np.array([[1.0, 0.0], [0.0, 1.0]], dtype='float64')})),
        ('Partner endpoint', lambda f: assert_close(f([[1],[3]],[[1,0],[0,1]],[1,0],0), {'features':np.array([[3.0], [1.0]], dtype='float64'),'labels':np.array([[0.0, 1.0], [1.0, 0.0]], dtype='float64')})),
        ('Identity partners', lambda f: assert_close(f([[2],[4]],[[1],[1]],[0,1],0.3), {'features':np.array([[2.0], [4.0]], dtype='float64'),'labels':np.array([[1.0], [1.0]], dtype='float64')})),
        ('Three-way cycle', lambda f: assert_close(f([[1],[2],[3]],np.eye(3),[1,2,0],0.25), {'features':np.array([[1.75], [2.75], [1.5]], dtype='float64'),'labels':np.array([[0.25, 0.75, 0.0], [0.0, 0.25, 0.75], [0.75, 0.0, 0.25]], dtype='float64')})),
        ('Single example', lambda f: assert_close(f([[2,-1]],[[0.2,0.8]],[0],0.6), {'features':np.array([[2.0, -1.0]], dtype='float64'),'labels':np.array([[0.2, 0.8]], dtype='float64')})),
        ('Reject repeated partner', lambda f: rejects(f, [[1],[2]],[[1],[1]],[0,0],0.5)),
        ('Reject label batch mismatch', lambda f: rejects(f, [[1],[2]],[[1]],[1,0],0.5)),
        ('Reject invalid coefficient', lambda f: rejects(f, [[1]],[[1]],[0],1.1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[0,2],[4,6]],[[1,0],[0,1]],[1,0],0.5), {'features':np.array([[2.0, 4.0], [2.0, 4.0]], dtype='float64'),'labels':np.array([[0.5, 0.5], [0.5, 0.5]], dtype='float64')})),
    ]
    return run_cases(namespace, 'mixup_batch', cases, mode)
