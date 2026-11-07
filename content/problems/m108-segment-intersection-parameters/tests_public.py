def run_tests(namespace, mode="all"):
    cases = [
        ('Crossing interiors', lambda f: assert_close(f([0,0],[2,2],[0,2],[2,0]), {'parameters':np.array([0.5, 0.5], dtype=float).reshape((2,)),'point':np.array([1.0, 1.0], dtype=float).reshape((2,)),'intersects':True})),
        ('Lines meet outside', lambda f: assert_close(f([0,0],[1,0],[2,-1],[2,1]), {'parameters':np.array([2.0, 0.5], dtype=float).reshape((2,)),'point':np.array([2.0, 0.0], dtype=float).reshape((2,)),'intersects':False})),
        ('Shared endpoint', lambda f: assert_close(f([0,0],[1,0],[1,0],[1,2]), {'parameters':np.array([1.0, 0.0], dtype=float).reshape((2,)),'point':np.array([1.0, 0.0], dtype=float).reshape((2,)),'intersects':True})),
        ('Reversed segment', lambda f: assert_close(f([2,2],[0,0],[0,2],[2,0]), {'parameters':np.array([0.5, 0.5], dtype=float).reshape((2,)),'point':np.array([1.0, 1.0], dtype=float).reshape((2,)),'intersects':True})),
        ('Negative parameter', lambda f: assert_close(f([0,0],[1,0],[-1,-1],[-1,1]), {'parameters':np.array([-1.0, 0.5], dtype=float).reshape((2,)),'point':np.array([-1.0, 0.0], dtype=float).reshape((2,)),'intersects':False})),
        ('Unequal lengths', lambda f: assert_close(f([0,0],[4,0],[1,-3],[1,1]), {'parameters':np.array([0.25, 0.75], dtype=float).reshape((2,)),'point':np.array([1.0, 0.0], dtype=float).reshape((2,)),'intersects':True})),
        ('Reject parallel', lambda f: rejects(f,[0,0],[1,0],[0,1],[2,1])),
        ('Reject degenerate', lambda f: rejects(f,[0,0],[0,0],[0,1],[1,0])),
        ('Reject wrong dimension', lambda f: rejects(f,[0,0,0],[1,0],[0,1],[1,1])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,0],[2,2],[0,2],[2,0]), {'parameters':np.array([0.5, 0.5], dtype=float).reshape((2,)),'point':np.array([1.0, 1.0], dtype=float).reshape((2,)),'intersects':True})),
    ]
    return run_cases(namespace, 'segment_intersection', cases, mode)
