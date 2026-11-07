def run_tests(namespace, mode="all"):
    cases = [
        ('Unequal sequence lengths', lambda f: assert_close(f([[2,3,4,0],[5,6,0,0]],[3,2],0), {'inputs':np.array([[2, 3, 0], [5, 0, 0]], dtype='int64'),'targets':np.array([[3, 4, 0], [6, 0, 0]], dtype='int64'),'mask':np.array([[True, True, False], [True, False, False]], dtype='bool')})),
        ('Full sequence', lambda f: assert_close(f([[1,2,3]],[3],0), {'inputs':np.array([[1, 2]], dtype='int64'),'targets':np.array([[2, 3]], dtype='int64'),'mask':np.array([[True, True]], dtype='bool')})),
        ('Minimum pair', lambda f: assert_close(f([[7,8]],[2],0), {'inputs':np.array([[7]], dtype='int64'),'targets':np.array([[8]], dtype='int64'),'mask':np.array([[True]], dtype='bool')})),
        ('Padding id is valid token', lambda f: assert_close(f([[0,2,0]],[2],0), {'inputs':np.array([[0, 0]], dtype='int64'),'targets':np.array([[2, 0]], dtype='int64'),'mask':np.array([[True, False]], dtype='bool')})),
        ('Ignore trailing garbage', lambda f: assert_close(f([[1,2,99,98]],[2],-0), {'inputs':np.array([[1, 0, 0]], dtype='int64'),'targets':np.array([[2, 0, 0]], dtype='int64'),'mask':np.array([[True, False, False]], dtype='bool')})),
        ('Nonzero padding', lambda f: assert_close(f([[1,2,3],[4,5,6]],[2,3],9), {'inputs':np.array([[1, 9], [4, 5]], dtype='int64'),'targets':np.array([[2, 9], [5, 6]], dtype='int64'),'mask':np.array([[True, False], [True, True]], dtype='bool')})),
        ('Reject too short sequence', lambda f: rejects(f, [[1,2]],[1],0)),
        ('Reject fractional token', lambda f: rejects(f, [[1,2.5]],[2],0)),
        ('Reject length beyond width', lambda f: rejects(f, [[1,2]],[3],0)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[2,3,4,0],[5,6,0,0]],[3,2],0), {'inputs':np.array([[2, 3, 0], [5, 0, 0]], dtype='int64'),'targets':np.array([[3, 4, 0], [6, 0, 0]], dtype='int64'),'mask':np.array([[True, True, False], [True, False, False]], dtype='bool')})),
    ]
    return run_cases(namespace, 'shift_language_batch', cases, mode)
