def run_tests(namespace, mode="all"):
    cases = [
        ('Intersection then exclusion', lambda f: assert_close(f({'a':[0,1,2],'b':[1,2],'x':[2]}, ['a','b'], ['x']), [1])),
        ('Unknown required term', lambda f: assert_close(f({'a':[1]}, ['a','missing'], []), [])),
        ('Unsorted repeated postings', lambda f: assert_close(f({'a':[3,1,3]}, ['a'], []), [1,3])),
        ('Unknown exclusion', lambda f: assert_close(f({'a':[2]}, ['a'], ['x']), [2])),
        ('Required and excluded same term', lambda f: assert_close(f({'a':[2]}, ['a'], ['a']), [])),
        ('Repeated query term', lambda f: assert_close(f({'a':[2,1]}, ['a','a'], []), [1,2])),
        ('Reject empty requirement', lambda f: rejects(f, {'a':[1]}, [], [])),
        ('Reject negative ID', lambda f: rejects(f, {'a':[-1]}, ['a'], [])),
        ('Reject invalid term key', lambda f: rejects(f, {'':[1]}, ['a'], [])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, {'a':[0,1,2],'b':[1,2],'x':[2]}, ['a','b'], ['x']), [1]))
    ]
    return run_cases(namespace, 'boolean_query', cases, mode)
