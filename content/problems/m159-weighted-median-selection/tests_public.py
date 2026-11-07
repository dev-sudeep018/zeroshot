def run_tests(namespace, mode="all"):
    cases = [
        ('Unequal weights', lambda f: assert_close(f([1,3,8],[1,5,2]), 3.0)),
        ('Exact half boundary', lambda f: assert_close(f([1,9],[1,1]), 1.0)),
        ('Unsorted values', lambda f: assert_close(f([8,1,4],[1,1,4]), 4.0)),
        ('Zero weight outlier', lambda f: assert_close(f([-99,2,5],[0,1,2]), 5.0)),
        ('Repeated values', lambda f: assert_close(f([1,1,4],[1,2,3]), 1.0)),
        ('Single value', lambda f: assert_close(f([7],[2]), 7.0)),
        ('Reject all zero weights', lambda f: rejects(f,[1,2],[0,0])),
        ('Reject negative weight', lambda f: rejects(f,[1,2],[-1,2])),
        ('Reject mismatch', lambda f: rejects(f,[1,2],[1])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,3,8],[1,5,2]), 3.0)),
    ]
    return run_cases(namespace, 'weighted_median', cases, mode)
