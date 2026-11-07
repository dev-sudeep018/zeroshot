def run_tests(namespace, mode="all"):
    cases = [
        ('Planar cloud', lambda f: assert_close(f([[0,1],[4,2],[1,5]]), {'lower':np.array([0.0, 1.0], dtype=float).reshape((2,)),'upper':np.array([4.0, 5.0], dtype=float).reshape((2,)),'center':np.array([2.0, 3.0], dtype=float).reshape((2,)),'lengths':np.array([4.0, 4.0], dtype=float).reshape((2,)),'volume':16.0})),
        ('One point', lambda f: assert_close(f([[2,3]]), {'lower':np.array([2.0, 3.0], dtype=float).reshape((2,)),'upper':np.array([2.0, 3.0], dtype=float).reshape((2,)),'center':np.array([2.0, 3.0], dtype=float).reshape((2,)),'lengths':np.array([0.0, 0.0], dtype=float).reshape((2,)),'volume':0.0})),
        ('Flat 3D cloud', lambda f: assert_close(f([[0,0,1],[2,3,1]]), {'lower':np.array([0.0, 0.0, 1.0], dtype=float).reshape((3,)),'upper':np.array([2.0, 3.0, 1.0], dtype=float).reshape((3,)),'center':np.array([1.0, 1.5, 1.0], dtype=float).reshape((3,)),'lengths':np.array([2.0, 3.0, 0.0], dtype=float).reshape((3,)),'volume':0.0})),
        ('Negative coordinates', lambda f: assert_close(f([[-4,-2],[-1,-8],[-3,-5]]), {'lower':np.array([-4.0, -8.0], dtype=float).reshape((2,)),'upper':np.array([-1.0, -2.0], dtype=float).reshape((2,)),'center':np.array([-2.5, -5.0], dtype=float).reshape((2,)),'lengths':np.array([3.0, 6.0], dtype=float).reshape((2,)),'volume':18.0})),
        ('One dimension', lambda f: assert_close(f([[2],[8],[3]]), {'lower':np.array([2.0], dtype=float).reshape((1,)),'upper':np.array([8.0], dtype=float).reshape((1,)),'center':np.array([5.0], dtype=float).reshape((1,)),'lengths':np.array([6.0], dtype=float).reshape((1,)),'volume':6.0})),
        ('Duplicate corners', lambda f: assert_close(f([[0,0],[2,2],[0,0]]), {'lower':np.array([0.0, 0.0], dtype=float).reshape((2,)),'upper':np.array([2.0, 2.0], dtype=float).reshape((2,)),'center':np.array([1.0, 1.0], dtype=float).reshape((2,)),'lengths':np.array([2.0, 2.0], dtype=float).reshape((2,)),'volume':4.0})),
        ('Reject vector', lambda f: rejects(f,[1,2])),
        ('Reject empty row', lambda f: rejects(f,[[]])),
        ('Reject nonfinite', lambda f: rejects(f,[[1,np.nan]])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[0,1],[4,2],[1,5]]), {'lower':np.array([0.0, 1.0], dtype=float).reshape((2,)),'upper':np.array([4.0, 5.0], dtype=float).reshape((2,)),'center':np.array([2.0, 3.0], dtype=float).reshape((2,)),'lengths':np.array([4.0, 4.0], dtype=float).reshape((2,)),'volume':16.0})),
    ]
    return run_cases(namespace, 'point_cloud_bounds', cases, mode)
