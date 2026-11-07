def run_tests(namespace, mode="all"):
    cases = [
        ('Mixed errors', lambda f: assert_close(f([10,20,0],[12,10,0]), {'per_item':np.array([0.18181818181818182, 0.6666666666666666, 0.0], dtype=float).reshape((3,)),'mean':0.2828282828282828})),
        ('Zero against nonzero', lambda f: assert_close(f([0,2],[3,0]), {'per_item':np.array([2.0, 2.0], dtype=float).reshape((2,)),'mean':2.0})),
        ('Opposite signs', lambda f: assert_close(f([-2,4],[2,-4]), {'per_item':np.array([2.0, 2.0], dtype=float).reshape((2,)),'mean':2.0})),
        ('Perfect prediction', lambda f: assert_close(f([1,-2,3],[1,-2,3]), {'per_item':np.array([0.0, 0.0, 0.0], dtype=float).reshape((3,)),'mean':0.0})),
        ('Small values', lambda f: assert_close(f([.1,.2],[.2,.1]), {'per_item':np.array([0.6666666666666666, 0.6666666666666666], dtype=float).reshape((2,)),'mean':0.6666666666666666})),
        ('Swapped pair', lambda f: assert_close(f([4,8],[8,4]), {'per_item':np.array([0.6666666666666666, 0.6666666666666666], dtype=float).reshape((2,)),'mean':0.6666666666666666})),
        ('Reject mismatch', lambda f: rejects(f,[1,2],[1])),
        ('Reject empty', lambda f: rejects(f,[],[])),
        ('Reject nonfinite', lambda f: rejects(f,[1],[np.inf])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[10,20,0],[12,10,0]), {'per_item':np.array([0.18181818181818182, 0.6666666666666666, 0.0], dtype=float).reshape((3,)),'mean':0.2828282828282828})),
    ]
    return run_cases(namespace, 'symmetric_percentage_errors', cases, mode)
