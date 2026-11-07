def run_tests(namespace, mode="all"):
    cases = [
        ('Diagonal separation', lambda f: assert_close(f([[True,False],[False,True]]), {'labels':np.array([[0, -1], [-1, 1]], dtype=float).reshape((2, 2)),'sizes':np.array([1, 1], dtype=float).reshape((2,)),'perimeters':np.array([4, 4], dtype=float).reshape((2,))})),
        ('Solid square', lambda f: assert_close(f([[True,True],[True,True]]), {'labels':np.array([[0, 0], [0, 0]], dtype=float).reshape((2, 2)),'sizes':np.array([4], dtype=float).reshape((1,)),'perimeters':np.array([8], dtype=float).reshape((1,))})),
        ('No foreground', lambda f: assert_close(f([[False,False]]), {'labels':np.array([[-1, -1]], dtype=float).reshape((1, 2)),'sizes':np.array([], dtype=float).reshape((0,)),'perimeters':np.array([], dtype=float).reshape((0,))})),
        ('L shape', lambda f: assert_close(f([[True,False],[True,True]]), {'labels':np.array([[0, -1], [0, 0]], dtype=float).reshape((2, 2)),'sizes':np.array([3], dtype=float).reshape((1,)),'perimeters':np.array([8], dtype=float).reshape((1,))})),
        ('Single cell', lambda f: assert_close(f([[True]]), {'labels':np.array([[0]], dtype=float).reshape((1, 1)),'sizes':np.array([1], dtype=float).reshape((1,)),'perimeters':np.array([4], dtype=float).reshape((1,))})),
        ('Hole boundary', lambda f: assert_close(f([[True,True,True],[True,False,True],[True,True,True]]), {'labels':np.array([[0, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=float).reshape((3, 3)),'sizes':np.array([8], dtype=float).reshape((1,)),'perimeters':np.array([16], dtype=float).reshape((1,))})),
        ('Reject numeric mask', lambda f: rejects(f,[[1,0]])),
        ('Reject vector', lambda f: rejects(f,[True,False])),
        ('Reject empty grid', lambda f: rejects(f,[])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[True,False],[False,True]]), {'labels':np.array([[0, -1], [-1, 1]], dtype=float).reshape((2, 2)),'sizes':np.array([1, 1], dtype=float).reshape((2,)),'perimeters':np.array([4, 4], dtype=float).reshape((2,))})),
    ]
    return run_cases(namespace, 'connected_grid_regions', cases, mode)
