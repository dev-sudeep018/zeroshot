def run_tests(namespace, mode="all"):
    cases = [
        ('Focused and diffuse', lambda f: assert_close(f([[1,0,0],[1/3,1/3,1/3]]), {'entropy':np.array([0.0, 1.0986122886681096], dtype='float64'),'effective_support':np.array([1.0, 2.9999999999999996], dtype='float64'),'peak':np.array([1.0, 0.3333333333333333], dtype='float64')})),
        ('Two equal keys', lambda f: assert_close(f([[0.5,0.5]]), {'entropy':np.array([0.6931471805599453], dtype='float64'),'effective_support':np.array([2.0], dtype='float64'),'peak':np.array([0.5], dtype='float64')})),
        ('Uneven probabilities', lambda f: assert_close(f([[0.9,0.1]]), {'entropy':np.array([0.3250829733914482], dtype='float64'),'effective_support':np.array([1.384145488461686], dtype='float64'),'peak':np.array([0.9], dtype='float64')})),
        ('Single key', lambda f: assert_close(f([[1],[1]]), {'entropy':np.array([0.0, 0.0], dtype='float64'),'effective_support':np.array([1.0, 1.0], dtype='float64'),'peak':np.array([1.0, 1.0], dtype='float64')})),
        ('Sparse uniform', lambda f: assert_close(f([[0.5,0,0.5,0]]), {'entropy':np.array([0.6931471805599453], dtype='float64'),'effective_support':np.array([2.0], dtype='float64'),'peak':np.array([0.5], dtype='float64')})),
        ('Near normalization tolerance', lambda f: assert_close(f([[0.5,0.500000001]]), {'entropy':np.array([0.6931471805599454], dtype='float64'),'effective_support':np.array([2.0], dtype='float64'),'peak':np.array([0.5000000004999999], dtype='float64')})),
        ('Reject bad sum', lambda f: rejects(f, [[0.2,0.2]])),
        ('Reject negative entry', lambda f: rejects(f, [[-0.1,1.1]])),
        ('Reject vector row', lambda f: rejects(f, [0.5,0.5])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[1,0,0],[1/3,1/3,1/3]]), {'entropy':np.array([0.0, 1.0986122886681096], dtype='float64'),'effective_support':np.array([1.0, 2.9999999999999996], dtype='float64'),'peak':np.array([1.0, 0.3333333333333333], dtype='float64')})),
    ]
    return run_cases(namespace, 'attention_support', cases, mode)
