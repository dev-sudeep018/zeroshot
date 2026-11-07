def run_tests(namespace, mode="all"):
    cases = [
        ('Signed contributions', lambda f: assert_close(f(['a','b'], 4), np.array([-1.,1.,0.,0.]))),
        ('Opposite signs can cancel', lambda f: assert_close(f(['b','c'], 4), np.zeros(4))),
        ('Repetition accumulates', lambda f: assert_close(f(['a','a'], 2), np.array([-2.,0.]))),
        ('Empty document', lambda f: assert_close(f([], 3), np.zeros(3))),
        ('Single bucket collision', lambda f: assert_close(f(['a','b','b'], 1), np.array([1.]))),
        ('Multicharacter hash', lambda f: assert_close(f(['ab'], 4), np.array([-1.,0.,0.,0.]))),
        ('Reject zero buckets', lambda f: rejects(f, ['a'], 0)),
        ('Reject invalid token', lambda f: rejects(f, [3], 4)),
        ('Reject raw text', lambda f: rejects(f, 'abc', 4)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, ['a','b'], 4), np.array([-1.,1.,0.,0.])))
    ]
    return run_cases(namespace, 'hashed_features', cases, mode)
