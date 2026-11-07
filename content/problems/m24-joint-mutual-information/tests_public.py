def run_tests(namespace, mode="all"):
    cases = [
        ('Independent coins', lambda f: assert_close(f([[.25,.25],[.25,.25]]), 0)),
        ('Perfect agreement', lambda f: assert_close(f([[.5,0],[0,.5]]), np.log(2))),
        ('Unequal dependent outcomes', lambda f: assert_close(f([[.25,0],[0,.75]]), -.25*np.log(.25)-.75*np.log(.75))),
        ('Single row', lambda f: assert_close(f([[.2,.3,.5]]), 0)),
        ('Unused category', lambda f: assert_close(f([[.5,0,0],[0,.5,0],[0,0,0]]), np.log(2))),
        ('Independent unequal marginals', lambda f: assert_close(f([[.1,.15],[.3,.45]]), 0)),
        ('Reject negative mass', lambda f: rejects(f,[[-.1,.6],[.5,0]])),
        ('Reject invalid sum', lambda f: rejects(f,[[1,1]])),
        ('Reject vector', lambda f: rejects(f,[.5,.5])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([[.5,0],[0,.5]])),np.log(2))),
        ('Tiny joint mass uses logarithmic ratios', lambda f: assert_close(f([[1e-300,0],[0,1]]),-1e-300*np.log(1e-300),atol=1e-310)),
    ]
    return run_cases(namespace, 'mutual_information', cases, mode)
