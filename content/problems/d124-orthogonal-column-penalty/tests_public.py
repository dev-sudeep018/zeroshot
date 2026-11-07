def run_tests(namespace, mode="all"):
    cases = [
        ('Already orthogonal', lambda f: assert_close(f(np.eye(2)), {'loss':0.0,'gradient':np.array([[0.0, 0.0], [0.0, 0.0]], dtype='float64')})),
        ('Scaled axes', lambda f: assert_close(f([[2,0],[0,1]]), {'loss':9.0,'gradient':np.array([[24.0, 0.0], [0.0, 0.0]], dtype='float64')})),
        ('Correlated columns', lambda f: assert_close(f([[1,1],[0,0]]), {'loss':2.0,'gradient':np.array([[4.0, 4.0], [0.0, 0.0]], dtype='float64')})),
        ('Tall orthogonal map', lambda f: assert_close(f([[1,0],[0,1],[0,0]]), {'loss':0.0,'gradient':np.array([[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]], dtype='float64')})),
        ('Wide matrix', lambda f: assert_close(f([[1,0]]), {'loss':1.0,'gradient':np.array([[0.0, 0.0]], dtype='float64')})),
        ('Zero matrix', lambda f: assert_close(f(np.zeros((2,2))), {'loss':2.0,'gradient':np.array([[0.0, 0.0], [0.0, 0.0]], dtype='float64')})),
        ('Reject vector input', lambda f: rejects(f, [1,2])),
        ('Reject nonfinite weight', lambda f: rejects(f, [[np.nan]])),
        ('Reject boolean weight', lambda f: rejects(f, [[True]])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, np.eye(2)), {'loss':0.0,'gradient':np.array([[0.0, 0.0], [0.0, 0.0]], dtype='float64')})),
    ]
    return run_cases(namespace, 'orthogonality_penalty', cases, mode)
