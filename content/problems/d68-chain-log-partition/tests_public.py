def run_tests(namespace, mode="all"):
    cases = [
        ('Four equal paths', lambda f: assert_close(f(np.zeros((2,2)),np.zeros((2,2)),[0,0],[0,0]),np.log(4))),
        ('Weighted single-step labels', lambda f: assert_close(f([[0,np.log(3)]],np.zeros((2,2)),[0,0],[0,0]),np.log(4))),
        ('Only one path', lambda f: assert_close(f([[1],[2],[3]],[[4]],[5],[6]),25.)),
        ('Transition direction matters', lambda f: assert_close(f(np.zeros((2,2)),[[0,np.log(2)],[np.log(3),0]],[0,0],[0,0]),np.log(7))),
        ('Start and end both contribute', lambda f: assert_close(f([[0,0]],np.zeros((2,2)),[0,np.log(2)],[0,np.log(3)]),np.log(7))),
        ('Large finite scores', lambda f: assert_close(f(np.full((2,2),1000),np.zeros((2,2)),[0,0],[0,0]),2000+np.log(4))),
        ('Three-time path count', lambda f: assert_close(f(np.zeros((3,2)),np.zeros((2,2)),[0,0],[0,0]),np.log(8))),
        ('Reject transition shape', lambda f: rejects(f,[[0,0]],[[0]],[0,0],[0,0])),
        ('Reject empty sequence', lambda f: rejects(f,np.empty((0,2)),np.zeros((2,2)),[0,0],[0,0])),
        ('Reject nonfinite start', lambda f: rejects(f,[[0]],[[0]],[np.inf],[0])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,np.zeros((2,2)),np.zeros((2,2)),[0,0],[0,0]),np.log(4))),
    ]
    return run_cases(namespace, 'chain_log_partition', cases, mode)
