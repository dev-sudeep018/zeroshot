def run_tests(namespace, mode="all"):
    cases = [
        ('Positive advantage', lambda f: assert_close(f([[0,0]],[0],[2]), dict(loss=2*np.log(2),gradient=np.array([[-1.,1.]])))),
        ('Negative advantage', lambda f: assert_close(f([[0,0]],[1],[-2]), dict(loss=-2*np.log(2),gradient=np.array([[-1.,1.]])))),
        ('Known action probability', lambda f: assert_close(f([[0,np.log(3)]],[1],[1]), dict(loss=-np.log(0.75),gradient=np.array([[0.25,-0.25]])))),
        ('Batch averaging', lambda f: assert_close(f([[0,0],[0,0]],[0,1],[2,4]), dict(loss=3*np.log(2),gradient=np.array([[-0.5,0.5],[1.,-1.]])))),
        ('Zero advantage', lambda f: assert_close(f([[4,-2]],[0],[0]), dict(loss=0.,gradient=np.zeros((1,2))))),
        ('Single action has no choice', lambda f: assert_close(f([[10]],[0],[4]), dict(loss=0.,gradient=np.zeros((1,1))))),
        ('Stable unlikely action', lambda f: assert_close(f([[1000,-1000]],[1],[1]), dict(loss=2000.,gradient=np.array([[1.,-1.]])))),
        ('Reject fractional action', lambda f: rejects(f, [[0,0]],[0.5],[1])),
        ('Reject out-of-range action', lambda f: rejects(f, [[0,0]],[2],[1])),
        ('Reject advantage batch mismatch', lambda f: rejects(f, [[0,0]],[0],[1,2])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[0,0]],[0],[2]), dict(loss=2*np.log(2),gradient=np.array([[-1.,1.]]))))
    ]
    return run_cases(namespace, 'policy_score_gradient', cases, mode)
