def run_tests(namespace, mode="all"):
    cases = [
        ('Three draws four labels', lambda f: assert_close(f(4,3), 0.625)),
        ('Birthday-sized example', lambda f: assert_close(f(365,23), 0.5072972343239854)),
        ('No draws', lambda f: assert_close(f(5,0), -0.0)),
        ('One draw', lambda f: assert_close(f(5,1), -0.0)),
        ('Pigeonhole certainty', lambda f: assert_close(f(3,4), 1.0)),
        ('Two draws', lambda f: assert_close(f(10,2), 0.1)),
        ('Reject zero categories', lambda f: rejects(f,0,2)),
        ('Reject negative draws', lambda f: rejects(f,4,-1)),
        ('Reject boolean count', lambda f: rejects(f,True,2)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,4,3), 0.625)),
    ]
    return run_cases(namespace, 'collision_probability', cases, mode)
