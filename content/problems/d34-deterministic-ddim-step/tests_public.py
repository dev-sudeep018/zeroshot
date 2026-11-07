def run_tests(namespace, mode="all"):
    cases = [
        ('Reach the clean endpoint', lambda f: assert_close(f([2],[0],.25,1),{"sample":np.array([4.]),"predicted_clean":np.array([4.])})),
        ('Identity step with predicted noise', lambda f: assert_close(f([2],[1],.25,.25),{"sample":np.array([2.]),"predicted_clean":np.array([4-np.sqrt(3)])})),
        ('Intermediate cleaner state', lambda f: assert_close(f([2],[0],.25,.75),{"sample":np.array([np.sqrt(12)]),"predicted_clean":np.array([4.])})),
        ('Already clean', lambda f: assert_close(f([2],[100],1,1)["sample"],np.array([2.]))),
        ('Preserve image dimensions', lambda f: assert_close(f(np.ones((2,1,3,4)),np.zeros((2,1,3,4)),.25,1)["sample"],np.full((2,1,3,4),2.))),
        ('Small permitted retention', lambda f: assert_close(f([1e-6],[0],1e-12,1)["sample"],np.array([1.]))),
        ('Reject backward ordering', lambda f: rejects(f,[1],[0],.75,.25)),
        ('Reject invalid retention', lambda f: [rejects(f,[1],[0],a,b) for a,b in ((0,1),(1e-13,1),(.5,1.1),(True,1))]),
        ('Reject broadcast noise', lambda f: rejects(f,[[1,2]],[[0]],.5,1)),
        ('Reject scalar sample', lambda f: rejects(f,1,0,.5,1)),
        ('Reject nonfinite noise', lambda f: rejects(f,[1],[np.inf],.5,1)),
        ('No mutation', lambda f: assert_close(unchanged(f,np.array([2.]),np.array([0.]),.25,1)["sample"],np.array([4.])))
    ]
    return run_cases(namespace, 'ddim_step', cases, mode)
