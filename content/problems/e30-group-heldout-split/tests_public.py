def run_tests(namespace, mode="all"):
    cases = [
        ('Repeated subject stays together', lambda f: assert_close(f(['u','v','u','w'], ['u']), dict(train=np.array([1,3]),test=np.array([0,2])))),
        ('No heldout groups', lambda f: assert_close(f(['u','v'], []), dict(train=np.array([0,1]),test=np.array([],dtype=int)))),
        ('All rows held out', lambda f: assert_close(f(['u','u'], ['u']), dict(train=np.array([],dtype=int),test=np.array([0,1])))),
        ('Empty data', lambda f: assert_close(f([], []), dict(train=np.array([],dtype=int),test=np.array([],dtype=int)))),
        ('Repeated holdout ID', lambda f: assert_close(f(['a','b'], ['a','a']), dict(train=np.array([1]),test=np.array([0])))),
        ('Multiple chosen groups', lambda f: assert_close(f(['a','b','c'], ['c','a']), dict(train=np.array([1]),test=np.array([0,2])))),
        ('Reject unknown group', lambda f: rejects(f, ['a'], ['b'])),
        ('Reject raw groups', lambda f: rejects(f, 'ab', ['a'])),
        ('Reject empty ID', lambda f: rejects(f, [''], [])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, ['u','v','u','w'], ['u']), dict(train=np.array([1,3]),test=np.array([0,2]))))
    ]
    return run_cases(namespace, 'group_split', cases, mode)
