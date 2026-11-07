def run_tests(namespace, mode="all"):
    cases = [
        ('Split votes', lambda f: assert_close(f([[[0.9,0.1]],[[0.2,0.8]]]), dict(mean_probability=np.array([[0.55,0.45]]),prediction=np.array([0]),vote_disagreement=np.array([0.5])))),
        ('Unanimous models', lambda f: assert_close(f([[[0.8,0.2]],[[0.6,0.4]]]), dict(mean_probability=np.array([[0.7,0.3]]),prediction=np.array([0]),vote_disagreement=np.array([0])))),
        ('Single model', lambda f: assert_close(f([[[0.1,0.9]]]), dict(mean_probability=np.array([[0.1,0.9]]),prediction=np.array([1]),vote_disagreement=np.array([0])))),
        ('Tied probabilities', lambda f: assert_close(f([[[0.5,0.5]],[[0.5,0.5]]]), dict(mean_probability=np.array([[0.5,0.5]]),prediction=np.array([0]),vote_disagreement=np.array([0])))),
        ('Three distinct votes', lambda f: assert_close(f(np.eye(3)[:,None,:]), dict(mean_probability=np.full((1,3),1/3),prediction=np.array([0]),vote_disagreement=np.array([2/3])))),
        ('Two examples', lambda f: assert_close(f([[[1,0],[0,1]],[[1,0],[1,0]]]), dict(mean_probability=np.array([[1,0],[0.5,0.5]]),prediction=np.array([0,0]),vote_disagreement=np.array([0,0.5])))),
        ('Reject invalid sum', lambda f: rejects(f, [[[0.2,0.2]]])),
        ('Reject negative probability', lambda f: rejects(f, [[[-0.1,1.1]]])),
        ('Reject missing model axis', lambda f: rejects(f, [[0.5,0.5]])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[[0.9,0.1]],[[0.2,0.8]]]), dict(mean_probability=np.array([[0.55,0.45]]),prediction=np.array([0]),vote_disagreement=np.array([0.5])))),
    ]
    return run_cases(namespace, 'ensemble_audit', cases, mode)
