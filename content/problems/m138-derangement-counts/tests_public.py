def assert_exact_integer(actual, expected):
    assert type(actual) is int, "Return an exact Python integer."
    assert actual == expected, "The exact combinatorial count differs."

def run_tests(namespace, mode="all"):
    cases = [
        ('Four assignments', lambda f: assert_close(f(4), {'count':9,'probability':0.375})),
        ('Empty assignment', lambda f: assert_close(f(0), {'count':1,'probability':1.0})),
        ('One assignment', lambda f: assert_close(f(1), {'count':0,'probability':0.0})),
        ('Two assignments', lambda f: assert_close(f(2), {'count':1,'probability':0.5})),
        ('Five assignments', lambda f: assert_close(f(5), {'count':44,'probability':0.36666666666666664})),
        ('Larger assignment', lambda f: assert_close(f(20), {'count':895014631192902121,'probability':0.36787944117144233})),
        ('Reject negative size', lambda f: rejects(f,-1)),
        ('Reject fractional size', lambda f: rejects(f,2.5)),
        ('Reject excess size', lambda f: rejects(f,65)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,4), {'count':9,'probability':0.375})),
        ('Exact large derangement count', lambda f: assert_exact_integer(f(20)["count"], 895014631192902121)),
    ]
    return run_cases(namespace, 'derangement_probability', cases, mode)
