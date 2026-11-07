def run_tests(namespace, mode="all"):
    cases = [
        ('Presence and absence', lambda f: assert_close(f([[1,0],[0,1]],[.6,.4],[[.8,.3],[.2,.7]]), np.array([[-1.0906441190189329, -3.729701448634191], [-3.3242363405260273, -1.4961092271270973]], dtype=float).reshape((2, 2)))),
        ('All absent', lambda f: assert_close(f([[0,0]],[.5,.5],[[.2,.4],[.6,.8]]), np.array([[-1.4271163556401456, -3.218875824868201]], dtype=float).reshape((1, 2)))),
        ('Single class', lambda f: assert_close(f([[1],[0]],[1],[[.25]]), np.array([[-1.3862943611198906], [-0.2876820724517809]], dtype=float).reshape((2, 1)))),
        ('Equal classes', lambda f: assert_close(f([[1,1]],[.5,.5],[[.3,.7],[.3,.7]]), np.array([[-2.2537949288246137, -2.2537949288246137]], dtype=float).reshape((1, 2)))),
        ('Unequal priors', lambda f: assert_close(f([[0]],[.2,.8],[[.5],[.5]]), np.array([[-2.3025850929940455, -0.916290731874155]], dtype=float).reshape((1, 2)))),
        ('Several samples', lambda f: assert_close(f([[1,0,1],[0,0,0]],[.3,.7],[[.2,.4,.6],[.7,.5,.3]]), np.array([[-3.8350619642920174, -2.610469872763346], [-2.854232711280291, -2.610469872763346]], dtype=float).reshape((2, 2)))),
        ('Reject nonbinary feature', lambda f: rejects(f,[[.5]],[1],[[.4]])),
        ('Reject endpoint likelihood', lambda f: rejects(f,[[1]],[1],[[1]])),
        ('Reject zero prior', lambda f: rejects(f,[[1]],[0,1],[[.3],[.4]])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[1,0],[0,1]],[.6,.4],[[.8,.3],[.2,.7]]), np.array([[-1.0906441190189329, -3.729701448634191], [-3.3242363405260273, -1.4961092271270973]], dtype=float).reshape((2, 2)))),
    ]
    return run_cases(namespace, 'bernoulli_log_scores', cases, mode)
