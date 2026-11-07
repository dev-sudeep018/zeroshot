def run_tests(namespace, mode="all"):
    cases = [
        ('Center and extremes', lambda f: assert_close(f([[0,1000],[0,-1000]],0.1), dict(probabilities=np.array([[0.5,1],[0.5,0]]),mean_derivative=np.array([0.25,0]),saturated_fraction=np.array([0,1])))),
        ('Central unit', lambda f: assert_close(f([[0]],0.2), dict(probabilities=np.array([[0.5]]),mean_derivative=np.array([0.25]),saturated_fraction=np.array([0])))),
        ('Positive threshold equality', lambda f: assert_close(f([[np.log(3)]],0.25), dict(probabilities=np.array([[0.75]]),mean_derivative=np.array([0.1875]),saturated_fraction=np.array([1])))),
        ('Negative threshold equality', lambda f: assert_close(f([[-np.log(3)]],0.25), dict(probabilities=np.array([[0.25]]),mean_derivative=np.array([0.1875]),saturated_fraction=np.array([1])))),
        ('Batch fraction', lambda f: assert_close(f([[0],[1000]],0.1), dict(probabilities=np.array([[0.5],[1]]),mean_derivative=np.array([0.125]),saturated_fraction=np.array([0.5])))),
        ('Threshold near one half', lambda f: assert_close(f([[0,0]],0.49), dict(probabilities=np.array([[0.5,0.5]]),mean_derivative=np.array([0.25,0.25]),saturated_fraction=np.array([0,0])))),
        ('Reject zero threshold', lambda f: rejects(f, [[0]],0)),
        ('Reject half threshold', lambda f: rejects(f, [[0]],0.5)),
        ('Reject nonfinite logits', lambda f: rejects(f, [[np.nan]],0.1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[0,1000],[0,-1000]],0.1), dict(probabilities=np.array([[0.5,1],[0.5,0]]),mean_derivative=np.array([0.25,0]),saturated_fraction=np.array([0,1])))),
    ]
    return run_cases(namespace, 'sigmoid_audit', cases, mode)
