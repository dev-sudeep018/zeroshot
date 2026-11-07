def run_tests(namespace, mode="all"):
    cases = [
        ('Single frame label', lambda f: assert_close(f([[.3,.7]],[1]),0.7)),
        ('Three alignments for one label', lambda f: assert_close(f([[.5,.5],[.5,.5]],[1]),0.75)),
        ('Repeated target needs blank', lambda f: assert_close(f(np.full((3,2),.5),[1,1]),0.125)),
        ('Empty target', lambda f: assert_close(f(np.full((3,2),.5),[]),0.125)),
        ('Impossible repeated target', lambda f: assert_close(f(np.full((2,2),.5),[1,1]),0.)),
        ('Different blank index', lambda f: assert_close(f([[.7,.3]],[0],1),0.7)),
        ('Distinct label transition', lambda f: assert_close(f(np.full((2,3),1/3),[1,2]),1/9)),
        ('Reject target blank', lambda f: rejects(f,[[.5,.5]],[0])),
        ('Reject unnormalized probabilities', lambda f: rejects(f,[[.4,.4]],[1])),
        ('Reject fractional labels', lambda f: rejects(f,[[.5,.5]],[1.0])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[.3,.7]],[1]),0.7)),
    ]
    return run_cases(namespace, 'ctc_probability', cases, mode)
