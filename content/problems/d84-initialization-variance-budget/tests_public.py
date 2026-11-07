def run_tests(namespace, mode="all"):
    cases = [
        ('Equal widths', lambda f: assert_close(f(4,4,1), np.array([[0.25,1],[0.5,2]]))),
        ('Expanding layer', lambda f: assert_close(f(2,6,1), np.array([[0.25,0.5],[1,2]]))),
        ('Larger input variance', lambda f: assert_close(f(2,2,3), np.array([[0.5,3],[1,6]]))),
        ('Zero input variance', lambda f: assert_close(f(3,5,0), np.array([[0.25,0],[2/3,0]]))),
        ('One connection', lambda f: assert_close(f(1,1,2), np.array([[1,2],[2,4]]))),
        ('Narrow output', lambda f: assert_close(f(6,2,2), np.array([[0.25,3],[1/3,4]]))),
        ('Reject zero fan', lambda f: rejects(f, 0,2,1)),
        ('Reject negative variance', lambda f: rejects(f, 2,2,-1)),
        ('Reject fractional fan', lambda f: rejects(f, 2.5,2,1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, 4,4,1), np.array([[0.25,1],[0.5,2]]))),
    ]
    return run_cases(namespace, 'initialization_budget', cases, mode)
