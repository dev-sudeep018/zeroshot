def run_tests(namespace, mode="all"):
    cases = [
        ('Concentrated amount', lambda f: assert_close(f([0,0,9]), {'population':np.array([0.0, 0.3333333333333333, 0.6666666666666666, 1.0], dtype=float).reshape((4,)),'share':np.array([0.0, 0.0, 0.0, 1.0], dtype=float).reshape((4,)),'gini':0.6666666666666666})),
        ('Equal amounts', lambda f: assert_close(f([2,2,2]), {'population':np.array([0.0, 0.3333333333333333, 0.6666666666666666, 1.0], dtype=float).reshape((4,)),'share':np.array([0.0, 0.3333333333333333, 0.6666666666666666, 1.0], dtype=float).reshape((4,)),'gini':0.0})),
        ('Unequal amounts', lambda f: assert_close(f([1,2,3,4]), {'population':np.array([0.0, 0.25, 0.5, 0.75, 1.0], dtype=float).reshape((5,)),'share':np.array([0.0, 0.1, 0.3, 0.6, 1.0], dtype=float).reshape((5,)),'gini':0.25})),
        ('Single amount', lambda f: assert_close(f([7]), {'population':np.array([0.0, 1.0], dtype=float).reshape((2,)),'share':np.array([0.0, 1.0], dtype=float).reshape((2,)),'gini':0.0})),
        ('Unsorted amounts', lambda f: assert_close(f([8,1,1]), {'population':np.array([0.0, 0.3333333333333333, 0.6666666666666666, 1.0], dtype=float).reshape((4,)),'share':np.array([0.0, 0.1, 0.2, 1.0], dtype=float).reshape((4,)),'gini':0.4666666666666667})),
        ('Zeros included', lambda f: assert_close(f([0,1,1,2]), {'population':np.array([0.0, 0.25, 0.5, 0.75, 1.0], dtype=float).reshape((5,)),'share':np.array([0.0, 0.0, 0.25, 0.5, 1.0], dtype=float).reshape((5,)),'gini':0.375})),
        ('Reject zero total', lambda f: rejects(f,[0,0])),
        ('Reject negative amount', lambda f: rejects(f,[-1,3])),
        ('Reject empty', lambda f: rejects(f,[])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,0,9]), {'population':np.array([0.0, 0.3333333333333333, 0.6666666666666666, 1.0], dtype=float).reshape((4,)),'share':np.array([0.0, 0.0, 0.0, 1.0], dtype=float).reshape((4,)),'gini':0.6666666666666666})),
    ]
    return run_cases(namespace, 'lorenz_summary', cases, mode)
