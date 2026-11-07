def run_tests(namespace, mode="all"):
    cases = [
        ('Boundary draws', lambda f: assert_close(f([.25,.25,.5],[0,.25,.5,.99]), {'cdf':np.array([0.25, 0.5, 1.0], dtype=float).reshape((3,)),'indices':np.array([0, 1, 2, 2], dtype=float).reshape((4,))})),
        ('Zero categories', lambda f: assert_close(f([0,.5,0,.5],[0,.5]), {'cdf':np.array([0.0, 0.5, 0.5, 1.0], dtype=float).reshape((4,)),'indices':np.array([1, 3], dtype=float).reshape((2,))})),
        ('Single category', lambda f: assert_close(f([1],[0,.9]), {'cdf':np.array([1.0], dtype=float).reshape((1,)),'indices':np.array([0, 0], dtype=float).reshape((2,))})),
        ('Unsorted draws', lambda f: assert_close(f([.2,.8],[.9,.1,.2]), {'cdf':np.array([0.2, 1.0], dtype=float).reshape((2,)),'indices':np.array([1, 0, 1], dtype=float).reshape((3,))})),
        ('Trailing zeros', lambda f: assert_close(f([.5,.5,0],[0,.5,.999]), {'cdf':np.array([0.5, 1.0, 1.0], dtype=float).reshape((3,)),'indices':np.array([0, 1, 1], dtype=float).reshape((3,))})),
        ('Repeated draw', lambda f: assert_close(f([.1,.2,.7],[.05,.05]), {'cdf':np.array([0.1, 0.30000000000000004, 1.0], dtype=float).reshape((3,)),'indices':np.array([0, 0], dtype=float).reshape((2,))})),
        ('Reject endpoint one', lambda f: rejects(f,[1],[1])),
        ('Reject negative draw', lambda f: rejects(f,[1],[-.1])),
        ('Reject invalid probability total', lambda f: rejects(f,[.2,.3],[.2])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[.25,.25,.5],[0,.25,.5,.99]), {'cdf':np.array([0.25, 0.5, 1.0], dtype=float).reshape((3,)),'indices':np.array([0, 1, 2, 2], dtype=float).reshape((4,))})),
    ]
    return run_cases(namespace, 'categorical_inverse_cdf', cases, mode)
