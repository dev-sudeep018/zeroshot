def run_tests(namespace, mode="all"):
    cases = [
        ('Inside outside boundary', lambda f: assert_close(f([[1,1],[3,1],[0,1]],[[0,0],[2,0],[2,2],[0,2]]), np.array([True, False, True], dtype=bool).reshape((3,)))),
        ('Concave notch', lambda f: assert_close(f([[.5,2],[2,2],[2,.5]],[[0,0],[3,0],[3,1],[1,1],[1,3],[0,3]]), np.array([True, False, True], dtype=bool).reshape((3,)))),
        ('Triangle vertices', lambda f: assert_close(f([[0,0],[1,1],[3,3]],[[0,0],[4,0],[0,4]]), np.array([True, True, False], dtype=bool).reshape((3,)))),
        ('Clockwise polygon', lambda f: assert_close(f([[1,1],[2,2]],[[0,0],[0,2],[2,2],[2,0]]), np.array([True, True], dtype=bool).reshape((2,)))),
        ('Horizontal boundary', lambda f: assert_close(f([[1,0],[3,0]],[[0,0],[2,0],[2,2],[0,2]]), np.array([True, False], dtype=bool).reshape((2,)))),
        ('Negative polygon', lambda f: assert_close(f([[-1,-1],[1,1]],[[-2,-2],[0,-2],[0,0],[-2,0]]), np.array([True, False], dtype=bool).reshape((2,)))),
        ('Reject crossed polygon', lambda f: rejects(f,[[1,1]],[[0,0],[3,3],[0,2],[3,0]])),
        ('Reject repeated vertex', lambda f: rejects(f,[[1,1]],[[0,0],[2,0],[2,0],[0,2]])),
        ('Reject fractional vertex', lambda f: rejects(f,[[1,1]],[[0,0],[2.5,0],[0,2]])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[1,1],[3,1],[0,1]],[[0,0],[2,0],[2,2],[0,2]]), np.array([True, False, True], dtype=bool).reshape((3,)))),
    ]
    return run_cases(namespace, 'points_in_polygon', cases, mode)
