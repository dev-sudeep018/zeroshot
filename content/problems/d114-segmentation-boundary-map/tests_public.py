def run_tests(namespace, mode="all"):
    cases = [
        ('Vertical split', lambda f: assert_close(f([[1,1,2],[1,1,2]]), np.array([[False, True, True], [False, True, True]], dtype='bool'))),
        ('Uniform region', lambda f: assert_close(f(np.ones((3,3))), np.array([[False, False, False], [False, False, False], [False, False, False]], dtype='bool'))),
        ('Single pixel', lambda f: assert_close(f([[4]]), np.array([[False]], dtype='bool'))),
        ('Checkerboard', lambda f: assert_close(f([[0,1],[1,0]]), np.array([[True, True], [True, True]], dtype='bool'))),
        ('One row', lambda f: assert_close(f([[1,1,2,2]]), np.array([[False, True, True, False]], dtype='bool'))),
        ('Center island', lambda f: assert_close(f([[0,0,0],[0,1,0],[0,0,0]]), np.array([[False, True, False], [True, True, True], [False, True, False]], dtype='bool'))),
        ('Reject fractional label', lambda f: rejects(f, [[0.5]])),
        ('Reject negative label', lambda f: rejects(f, [[-1]])),
        ('Reject vector input', lambda f: rejects(f, [1,2])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[1,1,2],[1,1,2]]), np.array([[False, True, True], [False, True, True]], dtype='bool'))),
    ]
    return run_cases(namespace, 'segmentation_boundaries', cases, mode)
