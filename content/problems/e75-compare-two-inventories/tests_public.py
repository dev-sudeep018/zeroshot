def run_tests(namespace, mode="all"):
    cases = [
        ('All change types', lambda f: assert_close(f({'a':1,'b':2},{'b':3,'c':0}), dict(added=['c'],removed=['a'],changed=[['b',2,3]]))),
        ('Unchanged stock', lambda f: assert_close(f({'a':0},{'a':0}), dict(added=[],removed=[],changed=[]))),
        ('Added zero item', lambda f: assert_close(f({}, {'x':0}), dict(added=['x'],removed=[],changed=[]))),
        ('Both empty', lambda f: assert_close(f({}, {}), dict(added=[],removed=[],changed=[]))),
        ('Sorted removals', lambda f: assert_close(f({'z':1,'a':2}, {}), dict(added=[],removed=['a','z'],changed=[]))),
        ('Quantity decrease', lambda f: assert_close(f({'a':5}, {'a':1}), dict(added=[],removed=[],changed=[['a',5,1]]))),
        ('Reject negative quantity', lambda f: rejects(f, {'a':-1}, {})),
        ('Reject fractional quantity', lambda f: rejects(f, {}, {'a':0.5})),
        ('Reject nonmapping inventory', lambda f: rejects(f, [], {})),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, {'a':1,'b':2},{'b':3,'c':0}), dict(added=['c'],removed=['a'],changed=[['b',2,3]])))
    ]
    return run_cases(namespace, 'compare_inventories', cases, mode)
