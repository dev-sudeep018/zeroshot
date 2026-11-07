def run_tests(namespace, mode="all"):
    cases = [
        ('Constant group', lambda f: assert_close(f([[[2,2],[2,2]]],1),np.zeros((1,2,2)))),
        ('Shared channels', lambda f: assert_close(f([[[0],[2]]],1,1),np.array([[[-1/np.sqrt(2)],[1/np.sqrt(2)]]]))),
        ('Singleton groups', lambda f: assert_close(f([[[0],[2]]],2,1),np.zeros((1,2,1)))),
        ('Spatial statistics', lambda f: assert_close(f([[[1,3]]],1,1),np.array([[[-1/np.sqrt(2),1/np.sqrt(2)]]]))),
        ('Batch isolation', lambda f: assert_close(f([[[1,3]],[[11,13]]],1,1),np.tile(np.array([[[-1/np.sqrt(2),1/np.sqrt(2)]]]),(2,1,1)))),
        ('Different channel groups', lambda f: assert_close(f([[[1,3],[8,8]]],2,1),np.array([[[-1/np.sqrt(2),1/np.sqrt(2)],[0,0]]]))),
        ('Centered groups sum to zero', lambda f: assert_close(f(np.arange(12).reshape(1,4,3),2).reshape(1,2,6).sum(-1),np.zeros((1,2)))),
        ('Reject nondivisor groups', lambda f: rejects(f,np.ones((1,3,2)),2)),
        ('Reject zero epsilon', lambda f: rejects(f,[[[1]]],1,0)),
        ('Reject boolean groups', lambda f: rejects(f,[[[1]]],True)),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[[2,2],[2,2]]],1),np.zeros((1,2,2)))),
    ]
    return run_cases(namespace, 'group_normalize', cases, mode)
