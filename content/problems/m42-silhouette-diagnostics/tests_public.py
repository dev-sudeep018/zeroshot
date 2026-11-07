def run_tests(namespace, mode="all"):
    cases = [
        ('Separated pairs', lambda f: assert_close(f([[0],[1],[4],[5]],[0,0,1,1]), {"scores":np.array([7/9,5/7,5/7,7/9]),"mean":47/63})),
        ('Singleton convention', lambda f: assert_close(f([[0],[2],[5]],[0,0,1]), {"scores":np.array([.6,1/3,0]),"mean":14/45})),
        ('Coincident points', lambda f: assert_close(f([[0],[0],[0]],[0,0,1]), {"scores":np.zeros(3),"mean":0})),
        ('Badly mixed groups', lambda f: assert_close(f([[0],[4],[1],[5]],[0,0,1,1]), {"scores":np.array([-.25,-.5,-.5,-.25]),"mean":-.375})),
        ('Noncontiguous labels', lambda f: assert_close(f([[0],[0],[2],[2]],[0,0,3,3]), {"scores":np.ones(4),"mean":1})),
        ('Two-dimensional geometry', lambda f: assert_close(f([[0,0],[0,0],[3,4],[3,4]],[0,0,1,1]), {"scores":np.ones(4),"mean":1})),
        ('Reject one cluster', lambda f: rejects(f,[[0],[1],[2]],[0,0,0])),
        ('Reject all singletons', lambda f: rejects(f,[[0],[1],[2]],[0,1,2])),
        ('Reject label mismatch', lambda f: rejects(f,[[0],[1],[2]],[0,1])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[0.],[0.],[2.],[2.]]),np.array([0,0,1,1])),{"scores":np.ones(4),"mean":1})),
    ]
    return run_cases(namespace, 'silhouette_scores', cases, mode)
