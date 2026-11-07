def run_tests(namespace, mode="all"):
    cases = [
        ('Reject overrepresented draft token', lambda f: assert_close(f([[.8,.2]], [[.2,.8]], [0], [.5]), dict(accepted=[],rejected_at=0,correction=np.array([0.,1.])))),
        ('Equal models accept', lambda f: assert_close(f([[.5,.5]], [[.5,.5]], [1], [.99]), dict(accepted=[1],rejected_at=-1,correction=np.zeros(2)))),
        ('Stop after accepted prefix', lambda f: assert_close(f([[.5,.5],[.8,.2]], [[.5,.5],[.2,.8]], [1,0], [.9,.5]), dict(accepted=[1],rejected_at=1,correction=np.array([0.,1.])))),
        ('Accept below ratio', lambda f: assert_close(f([[.8,.2]], [[.2,.8]], [0], [.1]), dict(accepted=[0],rejected_at=-1,correction=np.zeros(2)))),
        ('Equality rejects', lambda f: assert_close(f([[.8,.2]], [[.2,.8]], [0], [.25]), dict(accepted=[],rejected_at=0,correction=np.array([0.,1.])))),
        ('Zero target probability rejects', lambda f: assert_close(f([[.5,.5]], [[0.,1.]], [0], [0.]), dict(accepted=[],rejected_at=0,correction=np.array([0.,1.])))),
        ('Reject unnormalized probabilities', lambda f: rejects(f, [[.5,.6]], [[.5,.5]], [0], [.5])),
        ('Reject zero draft probability', lambda f: rejects(f, [[0.,1.]], [[.5,.5]], [0], [.5])),
        ('Reject invalid uniform', lambda f: rejects(f, [[.5,.5]], [[.5,.5]], [0], [1.])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[.8,.2]], [[.2,.8]], [0], [.5]), dict(accepted=[],rejected_at=0,correction=np.array([0.,1.]))))
        ,('Near-normalized rows are normalized', lambda f: assert_close(f([[.5,.5]], [[.5-1e-9,.5-1e-9]], [0], [.999999999]), dict(accepted=[0],rejected_at=-1,correction=np.zeros(2))))
    ]
    return run_cases(namespace, 'verify_draft', cases, mode)
