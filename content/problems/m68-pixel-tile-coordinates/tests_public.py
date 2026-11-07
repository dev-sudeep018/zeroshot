def run_tests(namespace, mode="all"):
    cases = [
        ('Uneven final tiles', lambda f: assert_close(f(3,5,2,3,[0,4,14]), {'tile':np.array([[0, 0], [0, 1], [1, 1]], dtype=float).reshape((3, 2)),'local':np.array([[0, 0], [0, 1], [0, 1]], dtype=float).reshape((3, 2))})),
        ('One tile', lambda f: assert_close(f(2,2,4,4,[0,3,1]), {'tile':np.array([[0, 0], [0, 0], [0, 0]], dtype=float).reshape((3, 2)),'local':np.array([[0, 0], [1, 1], [0, 1]], dtype=float).reshape((3, 2))})),
        ('Unit tiles', lambda f: assert_close(f(2,3,1,1,[5,0]), {'tile':np.array([[1, 2], [0, 0]], dtype=float).reshape((2, 2)),'local':np.array([[0, 0], [0, 0]], dtype=float).reshape((2, 2))})),
        ('Repeated pixels', lambda f: assert_close(f(1,4,1,2,[2,2,3]), {'tile':np.array([[0, 1], [0, 1], [0, 1]], dtype=float).reshape((3, 2)),'local':np.array([[0, 0], [0, 0], [0, 1]], dtype=float).reshape((3, 2))})),
        ('Tall image', lambda f: assert_close(f(4,1,3,1,[0,2,3]), {'tile':np.array([[0, 0], [0, 0], [1, 0]], dtype=float).reshape((3, 2)),'local':np.array([[0, 0], [2, 0], [0, 0]], dtype=float).reshape((3, 2))})),
        ('Single pixel', lambda f: assert_close(f(1,1,1,1,[0]), {'tile':np.array([[0, 0]], dtype=float).reshape((1, 2)),'local':np.array([[0, 0]], dtype=float).reshape((1, 2))})),
        ('Reject outside pixel', lambda f: rejects(f,2,2,1,1,[4])),
        ('Reject fractional pixel', lambda f: rejects(f,2,2,1,1,[.5])),
        ('Reject zero tile', lambda f: rejects(f,2,2,0,1,[0])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,3,5,2,3,[0,4,14]), {'tile':np.array([[0, 0], [0, 1], [1, 1]], dtype=float).reshape((3, 2)),'local':np.array([[0, 0], [0, 1], [0, 1]], dtype=float).reshape((3, 2))})),
    ]
    return run_cases(namespace, 'pixel_tile_locations', cases, mode)
