def run_tests(namespace, mode="all"):
    cases = [
        ('Mixed histories', lambda f: assert_close(f([[1,2,3]],[[4,5,6]],[[0.1,0.8,0.2]],0.5,9), np.array([[9, 1, 5]], dtype='int64'))),
        ('All teacher', lambda f: assert_close(f([[1,2]],[[3,4]],[[0.9,0.9]],1,0), np.array([[0, 1]], dtype='int64'))),
        ('No teacher', lambda f: assert_close(f([[1,2,3]],[[4,5,6]],[[0,0,0]],0,9), np.array([[9, 4, 5]], dtype='int64'))),
        ('Threshold equality', lambda f: assert_close(f([[1,2]],[[3,4]],[[0.5,0]],0.5,0), np.array([[0, 3]], dtype='int64'))),
        ('Separate examples', lambda f: assert_close(f([[1,2],[3,4]],[[5,6],[7,8]],[[0,0],[0.8,0]],0.5,9), np.array([[9, 1], [9, 7]], dtype='int64'))),
        ('Start token is ordinary ID', lambda f: assert_close(f([[0,2,3]],[[4,0,6]],[[0.2,0.7,0]],0.5,0), np.array([[0, 0, 0]], dtype='int64'))),
        ('Reject draw equals one', lambda f: rejects(f, [[1,2]],[[3,4]],[[1,0]],0.5,0)),
        ('Reject different shapes', lambda f: rejects(f, [[1,2]],[[3]],[[0,0]],0.5,0)),
        ('Reject fractional token', lambda f: rejects(f, [[1.5,2]],[[3,4]],[[0,0]],0.5,0)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[1,2,3]],[[4,5,6]],[[0.1,0.8,0.2]],0.5,9), np.array([[9, 1, 5]], dtype='int64'))),
    ]
    return run_cases(namespace, 'teacher_forcing_inputs', cases, mode)
