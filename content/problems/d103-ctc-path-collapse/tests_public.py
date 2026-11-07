def run_tests(namespace, mode="all"):
    cases = [
        ('Repeats and blanks', lambda f: assert_close(f([1,1,0,1,2,2],0), np.array([1, 1, 2], dtype='int64'))),
        ('All blanks', lambda f: assert_close(f([0,0,0],0), np.array([], dtype='int64'))),
        ('No repeats', lambda f: assert_close(f([1,2,3],0), np.array([1, 2, 3], dtype='int64'))),
        ('Separated repeated label', lambda f: assert_close(f([2,0,2],0), np.array([2, 2], dtype='int64'))),
        ('Nonzero blank', lambda f: assert_close(f([9,1,1,9,2],9), np.array([1, 2], dtype='int64'))),
        ('Single label', lambda f: assert_close(f([4],0), np.array([4], dtype='int64'))),
        ('Reject fractional token', lambda f: rejects(f, [1,2.5],0)),
        ('Reject negative token', lambda f: rejects(f, [-1],0)),
        ('Reject matrix path', lambda f: rejects(f, [[1,2]],0)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1,1,0,1,2,2],0), np.array([1, 1, 2], dtype='int64'))),
    ]
    return run_cases(namespace, 'collapse_ctc_path', cases, mode)
