def run_tests(namespace, mode="all"):
    cases = [
        ('Interior point', lambda f: assert_close(f([1,1],[[0,0],[4,0],[0,4]]), {'weights':np.array([0.5, 0.25, 0.25], dtype=float).reshape((3,)),'inside':True})),
        ('Vertex boundary', lambda f: assert_close(f([4,0],[[0,0],[4,0],[0,4]]), {'weights':np.array([0.0, 1.0, 0.0], dtype=float).reshape((3,)),'inside':True})),
        ('Outside point', lambda f: assert_close(f([5,2],[[0,0],[4,0],[0,4]]), {'weights':np.array([-0.75, 1.25, 0.5], dtype=float).reshape((3,)),'inside':False})),
        ('Edge midpoint', lambda f: assert_close(f([2,2],[[0,0],[4,0],[0,4]]), {'weights':np.array([0.0, 0.5, 0.5], dtype=float).reshape((3,)),'inside':True})),
        ('Clockwise triangle', lambda f: assert_close(f([1,1],[[0,0],[0,4],[4,0]]), {'weights':np.array([0.5, 0.25, 0.25], dtype=float).reshape((3,)),'inside':True})),
        ('Translated triangle', lambda f: assert_close(f([3,3],[[2,2],[6,2],[2,6]]), {'weights':np.array([0.5, 0.25, 0.25], dtype=float).reshape((3,)),'inside':True})),
        ('Reject collinear', lambda f: rejects(f,[1,1],[[0,0],[1,1],[2,2]])),
        ('Reject wrong count', lambda f: rejects(f,[1,1],[[0,0],[2,0]])),
        ('Reject tiny area', lambda f: rejects(f,[0,0],[[0,0],[1e-6,0],[0,1e-6]])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,1],[[0,0],[4,0],[0,4]]), {'weights':np.array([0.5, 0.25, 0.25], dtype=float).reshape((3,)),'inside':True})),
    ]
    return run_cases(namespace, 'barycentric_location', cases, mode)
