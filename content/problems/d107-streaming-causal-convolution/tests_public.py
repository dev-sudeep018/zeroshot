def run_tests(namespace, mode="all"):
    cases = [
        ('Two tap stream', lambda f: assert_close(f([3,4],[1,2],[2]), {'output':np.array([7.0, 10.0], dtype='float64'),'state':np.array([4.0], dtype='float64')})),
        ('Short chunk retains history', lambda f: assert_close(f([4],[1,2,3,4],[1,2,3]), {'output':np.array([20.0], dtype='float64'),'state':np.array([2.0, 3.0, 4.0], dtype='float64')})),
        ('Zero history', lambda f: assert_close(f([1,2,3],[1,-1],[0]), {'output':np.array([1.0, 1.0, 1.0], dtype='float64'),'state':np.array([3.0], dtype='float64')})),
        ('Current sample only', lambda f: assert_close(f([2,4],[1,0],[8]), {'output':np.array([2.0, 4.0], dtype='float64'),'state':np.array([4.0], dtype='float64')})),
        ('Delayed sample only', lambda f: assert_close(f([2,4],[0,1],[8]), {'output':np.array([8.0, 2.0], dtype='float64'),'state':np.array([4.0], dtype='float64')})),
        ('Negative kernel', lambda f: assert_close(f([1,-1],[2,-1,0.5],[3,2]), {'output':np.array([1.5, -2.0], dtype='float64'),'state':np.array([1.0, -1.0], dtype='float64')})),
        ('Reject state mismatch', lambda f: rejects(f, [1],[1,2,3],[0])),
        ('Reject single-tap kernel', lambda f: rejects(f, [1],[1],[0])),
        ('Reject empty chunk', lambda f: rejects(f, [],[1,2],[0])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [3,4],[1,2],[2]), {'output':np.array([7.0, 10.0], dtype='float64'),'state':np.array([4.0], dtype='float64')})),
    ]
    return run_cases(namespace, 'causal_convolution_chunk', cases, mode)
