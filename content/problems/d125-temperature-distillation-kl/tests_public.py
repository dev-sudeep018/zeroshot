def run_tests(namespace, mode="all"):
    cases = [
        ('Teacher favors one class', lambda f: assert_close(f([[0,0]],[[0,2]],1), {'loss':0.32781332547273756,'gradient':np.array([[0.3807970779778825, -0.3807970779778823]], dtype='float64')})),
        ('Matching predictions', lambda f: assert_close(f([[1,2]],[[1,2]],2), {'loss':0.0,'gradient':np.array([[0.0, 0.0]], dtype='float64')})),
        ('Hotter predictions', lambda f: assert_close(f([[1,-1]],[[0,2]],3), {'loss':1.9290764251898056,'gradient':np.array([[0.964538212594903, -0.964538212594903]], dtype='float64')})),
        ('Two examples', lambda f: assert_close(f([[1,0],[0,1]],[[0,1],[1,0]],1), {'loss':0.4621171572600098,'gradient':np.array([[0.2310585786300049, -0.2310585786300049], [-0.2310585786300049, 0.2310585786300049]], dtype='float64')})),
        ('Common offsets', lambda f: assert_close(f([[100,101]],[[-3,-2]],2), {'loss':0.0,'gradient':np.array([[0.0, 0.0]], dtype='float64')})),
        ('Extreme logits', lambda f: assert_close(f([[1000,-1000]],[[-1000,1000]],0.5), {'loss':1000.0,'gradient':np.array([[0.5, -0.5]], dtype='float64')})),
        ('Reject temperature zero', lambda f: rejects(f, [[1,2]],[[2,1]],0)),
        ('Reject shape mismatch', lambda f: rejects(f, [[1,2]],[[1,2,3]],1)),
        ('Reject single class', lambda f: rejects(f, [[1]],[[2]],1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[0,0]],[[0,2]],1), {'loss':0.32781332547273756,'gradient':np.array([[0.3807970779778825, -0.3807970779778823]], dtype='float64')})),
    ]
    return run_cases(namespace, 'distillation_kl', cases, mode)
