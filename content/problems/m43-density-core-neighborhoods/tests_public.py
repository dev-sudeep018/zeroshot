def run_tests(namespace, mode="all"):
    cases = [
        ('Inclusive boundary', lambda f: assert_close(f([[0],[1],[3]],1,2), {"neighbors":np.array([[1,1,0],[1,1,0],[0,0,1]],dtype=bool),"core":np.array([1,1,0],dtype=bool)})),
        ('Self counts', lambda f: assert_close(f([[0],[5]],0,1), {"neighbors":np.eye(2,dtype=bool),"core":np.ones(2,dtype=bool)})),
        ('Duplicate observations', lambda f: assert_close(f([[2],[2],[3]],0,2), {"neighbors":np.array([[1,1,0],[1,1,0],[0,0,1]],dtype=bool),"core":np.array([1,1,0],dtype=bool)})),
        ('Every pair close', lambda f: assert_close(f([[0],[1],[2]],2,3), {"neighbors":np.ones((3,3),dtype=bool),"core":np.ones(3,dtype=bool)})),
        ('Only center core', lambda f: assert_close(f([[0],[1],[2]],1,3), {"neighbors":np.array([[1,1,0],[1,1,1],[0,1,1]],dtype=bool),"core":np.array([0,1,0],dtype=bool)})),
        ('Euclidean geometry', lambda f: assert_close(f([[0,0],[3,4]],4,2), {"neighbors":np.eye(2,dtype=bool),"core":np.zeros(2,dtype=bool)})),
        ('Reject negative radius', lambda f: rejects(f,[[0]],-1,1)),
        ('Reject excessive count', lambda f: rejects(f,[[0]],1,2)),
        ('Reject boolean count', lambda f: rejects(f,[[0]],1,True)),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[0.],[1.],[3.]]),1,2),{"neighbors":np.array([[1,1,0],[1,1,0],[0,0,1]],dtype=bool),"core":np.array([1,1,0],dtype=bool)})),
        ('Tiny distinct points stay outside a zero radius', lambda f: assert_close(f([[0],[1e-300]],0,2), {'neighbors':np.eye(2,dtype=bool),'core':np.zeros(2,dtype=bool)})),
    ]
    return run_cases(namespace, 'density_neighborhoods', cases, mode)
