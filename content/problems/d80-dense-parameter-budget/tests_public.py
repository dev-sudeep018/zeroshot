def run_tests(namespace, mode="all"):
    cases = [
        ('Two layers', lambda f: assert_close(f([3,4,2],[1,1]), dict(weights=np.array([12,8]),biases=np.array([4,2]),per_layer=np.array([16,10]),total=26))),
        ('No bias', lambda f: assert_close(f([2,3],[0]), dict(weights=np.array([6]),biases=np.array([0]),per_layer=np.array([6]),total=6))),
        ('Mixed flags', lambda f: assert_close(f([1,2,1],[0,1]), dict(weights=np.array([2,2]),biases=np.array([0,1]),per_layer=np.array([2,3]),total=5))),
        ('Single neuron chain', lambda f: assert_close(f([1,1,1],[1,1]), dict(weights=np.array([1,1]),biases=np.array([1,1]),per_layer=np.array([2,2]),total=4))),
        ('Wide output', lambda f: assert_close(f([2,64],[1]), dict(weights=np.array([128]),biases=np.array([64]),per_layer=np.array([192]),total=192))),
        ('Three blocks', lambda f: assert_close(f([2,3,4,2],[1,0,1]), dict(weights=np.array([6,12,8]),biases=np.array([3,0,2]),per_layer=np.array([9,12,10]),total=31))),
        ('Reject missing layer', lambda f: rejects(f, [3],[1])),
        ('Reject flag count', lambda f: rejects(f, [2,3,4],[1])),
        ('Reject fractional width', lambda f: rejects(f, [2,3.5],[1])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [3,4,2],[1,1]), dict(weights=np.array([12,8]),biases=np.array([4,2]),per_layer=np.array([16,10]),total=26))),
    ]
    return run_cases(namespace, 'dense_budget', cases, mode)
