def run_tests(namespace, mode="all"):
    cases = [
        ('Ignore visible errors', lambda f: assert_close(f([[[1,3],[100,100]]],[[[0,1],[0,0]]],[[1,0]]), {'loss':2.5,'gradient':np.array([[[1.0, 2.0], [0.0, 0.0]]], dtype='float64')})),
        ('All patches masked', lambda f: assert_close(f([[[1],[3]]],[[[0],[1]]],[[1,1]]), {'loss':2.5,'gradient':np.array([[[1.0], [2.0]]], dtype='float64')})),
        ('Exact prediction', lambda f: assert_close(f([[[2,4]]],[[[2,4]]],[[1]]), {'loss':0.0,'gradient':np.array([[[0.0, 0.0]]], dtype='float64')})),
        ('Two examples', lambda f: assert_close(f([[[2],[4]],[[6],[8]]],np.zeros((2,2,1)),[[0,1],[1,0]]), {'loss':26.0,'gradient':np.array([[[0.0], [4.0]], [[6.0], [0.0]]], dtype='float64')})),
        ('Negative residual', lambda f: assert_close(f([[[-2,1]]],[[[0,3]]],[[1]]), {'loss':4.0,'gradient':np.array([[[-2.0, -2.0]]], dtype='float64')})),
        ('One scalar', lambda f: assert_close(f([[[3]]],[[[1]]],[[1]]), {'loss':4.0,'gradient':np.array([[[4.0]]], dtype='float64')})),
        ('Reject empty objective', lambda f: rejects(f, [[[1]]],[[[0]]],[[0]])),
        ('Reject nonbinary mask', lambda f: rejects(f, [[[1]]],[[[0]]],[[0.5]])),
        ('Reject mask shape', lambda f: rejects(f, [[[1],[2]]],[[[0],[0]]],[[1]])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[[1,3],[100,100]]],[[[0,1],[0,0]]],[[1,0]]), {'loss':2.5,'gradient':np.array([[[1.0, 2.0], [0.0, 0.0]]], dtype='float64')})),
    ]
    return run_cases(namespace, 'masked_reconstruction', cases, mode)
