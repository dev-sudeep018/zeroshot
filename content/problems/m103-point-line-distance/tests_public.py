def run_tests(namespace, mode="all"):
    cases = [
        ('Horizontal line', lambda f: assert_close(f([2,4],[0,2],-2), {'signed_distance':3.0,'foot':np.array([2.0, 1.0], dtype=float).reshape((2,))})),
        ('Vertical line', lambda f: assert_close(f([-3,2],[1,0],-1), {'signed_distance':-4.0,'foot':np.array([1.0, 2.0], dtype=float).reshape((2,))})),
        ('Sloping line', lambda f: assert_close(f([2,0],[1,1],-1), {'signed_distance':0.7071067811865475,'foot':np.array([1.5, -0.49999999999999994], dtype=float).reshape((2,))})),
        ('On line', lambda f: assert_close(f([2,3],[1,1],-5), {'signed_distance':0.0,'foot':np.array([2.0, 3.0], dtype=float).reshape((2,))})),
        ('Normal reversed', lambda f: assert_close(f([2,4],[0,-2],2), {'signed_distance':-3.0,'foot':np.array([2.0, 1.0], dtype=float).reshape((2,))})),
        ('Origin query', lambda f: assert_close(f([0,0],[3,4],-5), {'signed_distance':-1.0,'foot':np.array([0.6, 0.8], dtype=float).reshape((2,))})),
        ('Reject zero normal', lambda f: rejects(f,[1,2],[0,0],1)),
        ('Reject tiny normal', lambda f: rejects(f,[1,2],[1e-9,0],1)),
        ('Reject wrong dimension', lambda f: rejects(f,[1,2,3],[1,0],1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[2,4],[0,2],-2), {'signed_distance':3.0,'foot':np.array([2.0, 1.0], dtype=float).reshape((2,))})),
    ]
    return run_cases(namespace, 'point_line_projection', cases, mode)
