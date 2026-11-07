def run_tests(namespace, mode="all"):
    cases = [
        ('Same population', lambda f: assert_close(f([2,2], [2,2]), dict(reference=np.array([.5,.5]),current=np.array([.5,.5]),contributions=np.zeros(2),psi=0.))),
        ('Shift toward second bin', lambda f: assert_close(f([3,1], [1,3], 1), dict(reference=np.array([2/3,1/3]),current=np.array([1/3,2/3]),contributions=np.full(2,np.log(2)/3),psi=2*np.log(2)/3))),
        ('Empty bins stay finite', lambda f: assert_close(f([1,0], [0,1], 1), dict(reference=np.array([2/3,1/3]),current=np.array([1/3,2/3]),contributions=np.full(2,np.log(2)/3),psi=2*np.log(2)/3))),
        ('Single bin', lambda f: assert_close(f([2], [9]), dict(reference=np.array([1.]),current=np.array([1.]),contributions=np.array([0.]),psi=0.))),
        ('Uniform different totals', lambda f: assert_close(f([1,1], [5,5]), dict(reference=np.array([.5,.5]),current=np.array([.5,.5]),contributions=np.zeros(2),psi=0.))),
        ('Three equal bins', lambda f: assert_close(f([1,1,1], [2,2,2]), dict(reference=np.ones(3)/3,current=np.ones(3)/3,contributions=np.zeros(3),psi=0.))),
        ('Reject zero total', lambda f: rejects(f, [0,0], [1,2])),
        ('Reject too-small smoothing', lambda f: rejects(f, [1,2], [2,1], 5e-324)),
        ('Reject mismatched bins', lambda f: rejects(f, [1], [1,2])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [2,2], [2,2]), dict(reference=np.array([.5,.5]),current=np.array([.5,.5]),contributions=np.zeros(2),psi=0.)))
    ]
    return run_cases(namespace, 'population_stability', cases, mode)
