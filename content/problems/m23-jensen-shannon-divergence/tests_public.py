def run_tests(namespace, mode="all"):
    cases = [
        ('Identical distributions', lambda f: assert_close(f([.3,.7],[.3,.7]), 0)),
        ('Disjoint supports', lambda f: assert_close(f([1,0],[0,1]), np.log(2))),
        ('Partial overlap', lambda f: assert_close(f([1,0],[.5,.5]), .75*np.log(4/3))),
        ('Symmetry', lambda f: assert_close(f([.5,.5],[1,0]), .75*np.log(4/3))),
        ('Unused category', lambda f: assert_close(f([.5,.5,0],[.5,.5,0]), 0)),
        ('Separated groups', lambda f: assert_close(f([.2,.8,0,0],[0,0,.3,.7]), np.log(2))),
        ('Reject unequal shapes', lambda f: rejects(f,[1],[0,1])),
        ('Reject negative mass', lambda f: rejects(f,[-1,2],[.5,.5])),
        ('Reject empty distributions', lambda f: rejects(f,[],[])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([1.,0]),np.array([0.,1])),np.log(2))),
        ('Subnormal support remains finite', lambda f: assert_close(f([5e-324,1],[0,1]),0)),
    ]
    return run_cases(namespace, 'js_divergence', cases, mode)
