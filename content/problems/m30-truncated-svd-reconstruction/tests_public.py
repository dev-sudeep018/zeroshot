def run_tests(namespace, mode="all"):
    cases = [
        ('Keep largest direction', lambda f: assert_close(f([[3,0],[0,1]],1), {"matrix":np.array([[3.,0],[0,0]]),"squared_error":1})),
        ('Zero rank', lambda f: assert_close(f([[1,2],[3,4]],0), {"matrix":np.zeros((2,2)),"squared_error":30})),
        ('Full rank', lambda f: assert_close(f([[1,2],[0,1]],2), {"matrix":np.array([[1.,2],[0,1]]),"squared_error":0})),
        ('Already rank one', lambda f: assert_close(f([[1,2],[2,4]],1), {"matrix":np.array([[1.,2],[2,4]]),"squared_error":0})),
        ('Rectangular matrix', lambda f: assert_close(f([[4,0,0],[0,2,0]],1), {"matrix":np.array([[4.,0,0],[0,0,0]]),"squared_error":4})),
        ('Zero matrix', lambda f: assert_close(f([[0,0],[0,0]],1), {"matrix":np.zeros((2,2)),"squared_error":0})),
        ('Reject tied truncation', lambda f: rejects(f,[[1,0],[0,1]],1)),
        ('Reject excess rank', lambda f: rejects(f,[[1,2]],2)),
        ('Reject boolean rank', lambda f: rejects(f,[[1]],True)),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[3.,0],[0,1.]]),1),{"matrix":np.array([[3.,0],[0,0]]),"squared_error":1})),
    ]
    return run_cases(namespace, 'low_rank_approximation', cases, mode)
