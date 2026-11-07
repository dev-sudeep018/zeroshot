def run_tests(namespace, mode="all"):
    cases = [
        ('Exact velocity at the midpoint', lambda f: assert_close(f([[0,0]],[[2,4]],[.5],[[2,4]]),{"point":np.array([[1.,2.]]),"velocity":np.array([[2.,4.]]),"loss":0})),
        ('Wrong velocity at the start', lambda f: assert_close(f([[0,0]],[[2,4]],[0],[[0,0]]),{"point":np.array([[0.,0.]]),"velocity":np.array([[2.,4.]]),"loss":10})),
        ('Different times per example', lambda f: assert_close(f([[1],[2]],[[3],[6]],[0,1],[[0],[0]]),{"point":np.array([[1.],[6.]]),"velocity":np.array([[2.],[4.]]),"loss":10})),
        ('Constant endpoints', lambda f: assert_close(f([[3]],[[3]],[.7],[[0]])["velocity"],np.zeros((1,1)))),
        ('Direction is data minus noise', lambda f: assert_close(f([[4]],[[1]],[.5],[[-3]])["loss"],0)),
        ('Average features too', lambda f: assert_close(f([[0,0]],[[0,0]],[.5],[[2,0]])["loss"],2)),
        ('Quarter interpolation', lambda f: assert_close(f([[2]],[[10]],[.25],[[8]])["point"],np.array([[4.]]))),
        ('Reject scalar time', lambda f: rejects(f,[[0]],[[1]],.5,[[1]])),
        ('Reject invalid time', lambda f: [rejects(f,[[0]],[[1]],[v],[[1]]) for v in (-.1,1.1,np.nan)]),
        ('Reject prediction broadcast', lambda f: rejects(f,[[0,0]],[[1,1]],[.5],[[1]])),
        ('Reject empty features', lambda f: rejects(f,np.empty((1,0)),np.empty((1,0)),[0],np.empty((1,0)))),
        ('No mutation', lambda f: assert_close(unchanged(f,np.array([[0.]]),np.array([[2.]]),np.array([.5]),np.array([[2.]]))["point"],np.array([[1.]])))
    ]
    return run_cases(namespace, 'flow_matching', cases, mode)
