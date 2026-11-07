def run_tests(namespace, mode="all"):
    cases = [
        ('Horizontal plane', lambda f: assert_close(f([0,0,2],[1,0,2],[0,1,2]), {'normal':np.array([0.0, 0.0, 1.0], dtype=float).reshape((3,)),'offset':-2.0})),
        ('Reverse orientation', lambda f: assert_close(f([0,0,2],[0,1,2],[1,0,2]), {'normal':np.array([0.0, 0.0, -1.0], dtype=float).reshape((3,)),'offset':2.0})),
        ('Sloping plane', lambda f: assert_close(f([1,0,0],[0,1,0],[0,0,1]), {'normal':np.array([0.5773502691896258, 0.5773502691896258, 0.5773502691896258], dtype=float).reshape((3,)),'offset':-0.5773502691896258})),
        ('Plane through origin', lambda f: assert_close(f([0,0,0],[1,1,0],[0,0,1]), {'normal':np.array([0.7071067811865475, -0.7071067811865475, 0.0], dtype=float).reshape((3,)),'offset':0.0})),
        ('Vertical plane', lambda f: assert_close(f([3,0,0],[3,2,0],[3,0,4]), {'normal':np.array([1.0, 0.0, 0.0], dtype=float).reshape((3,)),'offset':-3.0})),
        ('Translated vertices', lambda f: assert_close(f([1,2,3],[2,2,4],[1,3,4]), {'normal':np.array([-0.5773502691896258, -0.5773502691896258, 0.5773502691896258], dtype=float).reshape((3,)),'offset':1.1102230246251565e-16})),
        ('Reject collinear', lambda f: rejects(f,[0,0,0],[1,1,1],[2,2,2])),
        ('Reject wrong dimension', lambda f: rejects(f,[0,0],[1,0,0],[0,1,0])),
        ('Reject tiny triangle', lambda f: rejects(f,[0,0,0],[1e-4,0,0],[0,1e-4,0])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,0,2],[1,0,2],[0,1,2]), {'normal':np.array([0.0, 0.0, 1.0], dtype=float).reshape((3,)),'offset':-2.0})),
    ]
    return run_cases(namespace, 'plane_from_points', cases, mode)
