def run_tests(namespace, mode="all"):
    cases = [
        ('Square root of two', lambda f: assert_close(f([1,0,-2],0,2,8), {'root':1.41796875,'bracket':np.array([1.4140625, 1.421875], dtype=float).reshape((2,))})),
        ('Exact midpoint root', lambda f: assert_close(f([1,-1],0,2,4), {'root':1.0,'bracket':np.array([1.0, 1.0], dtype=float).reshape((2,))})),
        ('Endpoint root', lambda f: assert_close(f([1,-2],0,2,3), {'root':2.0,'bracket':np.array([2.0, 2.0], dtype=float).reshape((2,))})),
        ('Zero steps', lambda f: assert_close(f([1,-.3],0,1,0), {'root':0.5,'bracket':np.array([0.0, 1.0], dtype=float).reshape((2,))})),
        ('Negative root', lambda f: assert_close(f([1,0,-2],-2,0,12), {'root':-1.414306640625,'bracket':np.array([-1.41455078125, -1.4140625], dtype=float).reshape((2,))})),
        ('Cubic root', lambda f: assert_close(f([1,0,0,-3],1,2,10), {'root':1.44189453125,'bracket':np.array([1.44140625, 1.4423828125], dtype=float).reshape((2,))})),
        ('Tiny coefficient sign change', lambda f: assert_close(f([1e-200,0],-1,2,20), {'root':4.76837158203125e-07,'bracket':np.array([-9.5367431640625e-07, 1.9073486328125e-06], dtype=float).reshape((2,))})),
        ('Reject tiny same-sign endpoints', lambda f: rejects(f,[1e-200,0,1e-200],-1,1,3)),
        ('Reject no sign change', lambda f: rejects(f,[1,0,1],-1,1,3)),
        ('Reject reversed bracket', lambda f: rejects(f,[1,0],1,-1,3)),
        ('Reject negative steps', lambda f: rejects(f,[1,0],-1,1,-1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,0,-2],0,2,8), {'root':1.41796875,'bracket':np.array([1.4140625, 1.421875], dtype=float).reshape((2,))})),
    ]
    return run_cases(namespace, 'bisect_polynomial', cases, mode)
