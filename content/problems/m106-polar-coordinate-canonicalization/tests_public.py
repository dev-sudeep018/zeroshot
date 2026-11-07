def run_tests(namespace, mode="all"):
    cases = [
        ('Four directions', lambda f: assert_close(f([[1,0],[0,1],[-1,0],[0,-1]]), {'radius':np.array([1.0, 1.0, 1.0, 1.0], dtype=float).reshape((4,)),'angle':np.array([0.0, 1.5707963267948966, 3.141592653589793, 4.71238898038469], dtype=float).reshape((4,))})),
        ('Origin convention', lambda f: assert_close(f([[0,0],[3,4]]), {'radius':np.array([0.0, 5.0], dtype=float).reshape((2,)),'angle':np.array([0.0, 0.9272952180016122], dtype=float).reshape((2,))})),
        ('Different quadrants', lambda f: assert_close(f([[1,1],[-1,1],[-1,-1],[1,-1]]), {'radius':np.array([1.4142135623730951, 1.4142135623730951, 1.4142135623730951, 1.4142135623730951], dtype=float).reshape((4,)),'angle':np.array([0.7853981633974483, 2.356194490192345, 3.9269908169872414, 5.497787143782138], dtype=float).reshape((4,))})),
        ('Scaled position', lambda f: assert_close(f([[2,2],[4,4]]), {'radius':np.array([2.8284271247461903, 5.656854249492381], dtype=float).reshape((2,)),'angle':np.array([0.7853981633974483, 0.7853981633974483], dtype=float).reshape((2,))})),
        ('Negative axes', lambda f: assert_close(f([[-3,0],[0,-5]]), {'radius':np.array([3.0, 5.0], dtype=float).reshape((2,)),'angle':np.array([3.141592653589793, 4.71238898038469], dtype=float).reshape((2,))})),
        ('Small coordinates', lambda f: assert_close(f([[.3,.4],[-.3,.4]]), {'radius':np.array([0.5, 0.5], dtype=float).reshape((2,)),'angle':np.array([0.9272952180016123, 2.214297435588181], dtype=float).reshape((2,))})),
        ('Reject 3D point', lambda f: rejects(f,[[1,2,3]])),
        ('Reject vector', lambda f: rejects(f,[1,2])),
        ('Reject empty', lambda f: rejects(f,[])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[1,0],[0,1],[-1,0],[0,-1]]), {'radius':np.array([1.0, 1.0, 1.0, 1.0], dtype=float).reshape((4,)),'angle':np.array([0.0, 1.5707963267948966, 3.141592653589793, 4.71238898038469], dtype=float).reshape((4,))})),
    ]
    return run_cases(namespace, 'canonical_polar', cases, mode)
