def assert_exact_integer(actual, expected):
    assert type(actual) is int, "Return an exact Python integer."
    assert actual == expected, "The exact combinatorial count differs."

def run_tests(namespace, mode="all"):
    cases = [
        ('Open rectangle', lambda f: assert_close(f([[False,False,False],[False,False,False]]), 3)),
        ('Blocked center', lambda f: assert_close(f([[False,False,False],[False,True,False],[False,False,False]]), 2)),
        ('Blocked start', lambda f: assert_close(f([[True,False],[False,False]]), 0)),
        ('Single open cell', lambda f: assert_close(f([[False]]), 1)),
        ('Blocked destination', lambda f: assert_close(f([[False,False],[False,True]]), 0)),
        ('Single corridor', lambda f: assert_close(f([[False,False,False,False]]), 1)),
        ('Reject numeric mask', lambda f: rejects(f,[[0,1],[0,0]])),
        ('Reject vector', lambda f: rejects(f,[False,False])),
        ('Reject empty grid', lambda f: rejects(f,[])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[False,False,False],[False,False,False]]), 3)),
        ('Exact large lattice count', lambda f: assert_exact_integer(f(np.zeros((32,32),dtype=bool)), 465428353255261088)),
    ]
    return run_cases(namespace, 'blocked_grid_paths', cases, mode)
