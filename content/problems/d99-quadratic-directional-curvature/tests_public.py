def run_tests(namespace, mode="all"):
    cases = [
        ('One dimensional descent', lambda f: assert_close(f([[2]],[3],[-1]), {'value':9.0,'slope':-6.0,'curvature':2.0,'step':3.0})),
        ('One dimensional uphill', lambda f: assert_close(f([[2]],[3],[1]), {'value':9.0,'slope':6.0,'curvature':2.0,'step':-3.0})),
        ('Two-dimensional line', lambda f: assert_close(f([[2,0],[0,4]],[1,2],[-1,-1]), {'value':9.0,'slope':-10.0,'curvature':6.0,'step':1.6666666666666667})),
        ('Stationary point', lambda f: assert_close(f([[1]],[0],[2]), {'value':0.0,'slope':0.0,'curvature':4.0,'step':-0.0})),
        ('Off diagonal curvature', lambda f: assert_close(f([[2,1],[1,3]],[1,-1],[1,2]), {'value':1.5,'slope':-3.0,'curvature':18.0,'step':0.16666666666666666})),
        ('Indefinite matrix valid line', lambda f: assert_close(f([[1,0],[0,-1]],[2,3],[1,0]), {'value':-2.5,'slope':2.0,'curvature':1.0,'step':-2.0})),
        ('Reject nonsymmetric matrix', lambda f: rejects(f, [[1,2],[0,1]],[1,1],[1,0])),
        ('Reject zero direction', lambda f: rejects(f, [[1]],[1],[0])),
        ('Reject negative curvature', lambda f: rejects(f, [[-1]],[1],[1])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[2]],[3],[-1]), {'value':9.0,'slope':-6.0,'curvature':2.0,'step':3.0})),
    ]
    return run_cases(namespace, 'quadratic_probe', cases, mode)
