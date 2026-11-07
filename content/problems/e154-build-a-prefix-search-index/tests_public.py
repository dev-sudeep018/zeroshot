def run_tests(namespace, mode="all"):
    cases = [
        ('Shared prefixes', lambda f: assert_close(f(['car','cat']), {'c':['car','cat'],'ca':['car','cat'],'car':['car'],'cat':['cat']})),
        ('Remove duplicate terms', lambda f: assert_close(f(['a','ab','a']), {'a':['a','ab'],'ab':['ab']})),
        ('Case-sensitive', lambda f: assert_close(f(['a','A']), {'A':['A'],'a':['a']})),
        ('Empty collection', lambda f: assert_close(f([]), {})),
        ('Unicode prefix', lambda f: assert_close(f(['éa','éb']), {'é':['éa','éb'],'éa':['éa'],'éb':['éb']})),
        ('Unrelated terms', lambda f: assert_close(f(['z','b']), {'b':['b'],'z':['z']})),
        ('Reject empty term', lambda f: rejects(f, [''])),
        ('Reject nonstring term', lambda f: rejects(f, [1])),
        ('Reject too long', lambda f: rejects(f, ['x'*101])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['car','cat']), {'c':['car','cat'],'ca':['car','cat'],'car':['car'],'cat':['cat']}))
    ]
    return run_cases(namespace, 'prefix_index', cases, mode)
