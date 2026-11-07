def run_tests(namespace, mode="all"):
    cases = [
        ('Separate repeated segments', lambda f: assert_close(f([1,1,2,1,1,1]), dict(values=np.array([1.,2.,1.]),lengths=np.array([2,1,3]),starts=np.array([0,2,3])))),
        ('Empty stream', lambda f: assert_close(f([]), dict(values=np.array([]),lengths=np.array([],dtype=int),starts=np.array([],dtype=int)))),
        ('One long run', lambda f: assert_close(f([5,5,5]), dict(values=np.array([5.]),lengths=np.array([3]),starts=np.array([0])))),
        ('Every value changes', lambda f: assert_close(f([1,2,3]), dict(values=np.array([1.,2.,3.]),lengths=np.array([1,1,1]),starts=np.array([0,1,2])))),
        ('Single value', lambda f: assert_close(f([-2]), dict(values=np.array([-2.]),lengths=np.array([1]),starts=np.array([0])))),
        ('Signed zeros match', lambda f: assert_close(f([0.,-0.]), dict(values=np.array([0.]),lengths=np.array([2]),starts=np.array([0])))),
        ('Reject matrix', lambda f: rejects(f, [[1,1]])),
        ('Reject nonfinite value', lambda f: rejects(f, [np.inf])),
        ('Reject string data', lambda f: rejects(f, ['a'])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1,1,2,1,1,1]), dict(values=np.array([1.,2.,1.]),lengths=np.array([2,1,3]),starts=np.array([0,2,3]))))
    ]
    return run_cases(namespace, 'run_length_encode', cases, mode)
