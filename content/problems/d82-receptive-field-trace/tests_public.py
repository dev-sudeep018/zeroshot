def run_tests(namespace, mode="all"):
    cases = [
        ('Two local layers', lambda f: assert_close(f([3,3],[1,1],[1,1]), dict(field=np.array([3,5]),jump=np.array([1,1])))),
        ('Early stride', lambda f: assert_close(f([3,3],[2,1],[1,1]), dict(field=np.array([3,7]),jump=np.array([2,2])))),
        ('Dilated layer', lambda f: assert_close(f([3,3],[1,1],[1,2]), dict(field=np.array([3,7]),jump=np.array([1,1])))),
        ('Pointwise kernel', lambda f: assert_close(f([1],[2],[4]), dict(field=np.array([1]),jump=np.array([2])))),
        ('Three scales', lambda f: assert_close(f([2,2,3],[2,2,1],[1,1,1]), dict(field=np.array([2,4,12]),jump=np.array([2,4,4])))),
        ('Combined dilation', lambda f: assert_close(f([2,3],[3,2],[2,3]), dict(field=np.array([3,21]),jump=np.array([3,6])))),
        ('Reject unequal lengths', lambda f: rejects(f, [3,3],[1],[1,1])),
        ('Reject zero stride', lambda f: rejects(f, [3],[0],[1])),
        ('Reject too many layers', lambda f: rejects(f, [1]*9,[1]*9,[1]*9)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [3,3],[1,1],[1,1]), dict(field=np.array([3,5]),jump=np.array([1,1])))),
    ]
    return run_cases(namespace, 'receptive_fields', cases, mode)
