def run_tests(namespace, mode="all"):
    cases = [
        ('Move one logit', lambda f: assert_close(f([[.5,.5]],[[1,0]]),np.array([[.25,-.25]]))),
        ('Constant shift', lambda f: assert_close(f([[.2,.8]],[[3,3]]),np.zeros((1,2)))),
        ('Unequal probability weights', lambda f: assert_close(f([[.25,.75]],[[1,0]]),np.array([[.1875,-.1875]]))),
        ('One class', lambda f: assert_close(f([[1]],[[9]]),np.array([[0.]]))),
        ('Boundary distribution', lambda f: assert_close(f([[1,0]],[[1,3]]),np.zeros((1,2)))),
        ('Opposite direction', lambda f: assert_close(f([[.5,.5]],[[-1,0]]),np.array([[-.25,.25]]))),
        ('Independent batch rows', lambda f: assert_close(f([[.5,.5],[.25,.75]],[[1,0],[0,1]]),np.array([[.25,-.25],[-.1875,.1875]]))),
        ('Reject unnormalized row', lambda f: rejects(f,[[1,1]],[[1,0]])),
        ('Reject broadcast direction', lambda f: rejects(f,[[.5,.5]],[[1]])),
        ('Reject negative probability', lambda f: rejects(f,[[-.1,1.1]],[[1,0]])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[.5,.5]],[[1,0]]),np.array([[.25,-.25]]))),
    ]
    return run_cases(namespace, 'softmax_jvp', cases, mode)
