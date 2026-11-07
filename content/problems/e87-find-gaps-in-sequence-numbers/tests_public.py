def run_tests(namespace, mode="all"):
    cases = [
        ('Interior gaps', lambda f: assert_close(f([2,4], 1, 5), [1,3,5])),
        ('Duplicates ignored', lambda f: assert_close(f([3,1,1], 1, 3), [2])),
        ('Complete range', lambda f: assert_close(f([0,1,2], 0, 2), [])),
        ('No observed IDs', lambda f: assert_close(f([], 2, 4), [2,3,4])),
        ('Single missing ID', lambda f: assert_close(f([], 5, 5), [5])),
        ('Single present ID', lambda f: assert_close(f([5], 5, 5), [])),
        ('Reject outside range', lambda f: rejects(f, [4], 1, 3)),
        ('Reject reversed bounds', lambda f: rejects(f, [], 2, 1)),
        ('Reject oversized range', lambda f: rejects(f, [], 0, 1001)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [2,4], 1, 5), [1,3,5]))
    ]
    return run_cases(namespace, 'missing_sequence_ids', cases, mode)
