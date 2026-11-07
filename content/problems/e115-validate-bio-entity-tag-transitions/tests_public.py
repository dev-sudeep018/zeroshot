def run_tests(namespace, mode="all"):
    cases = [
        ('Valid entity span', lambda f: assert_close(f(['B-PER','I-PER','O']), [])),
        ('Initial inside tag', lambda f: assert_close(f(['I-PER','I-PER']), [0])),
        ('Type mismatch', lambda f: assert_close(f(['B-PER','I-ORG','I-ORG']), [1])),
        ('Outside breaks span', lambda f: assert_close(f(['B-X','O','I-X']), [2])),
        ('Empty tags', lambda f: assert_close(f([]), [])),
        ('Begin after begin', lambda f: assert_close(f(['B-X','B-Y','I-Y']), [])),
        ('Reject missing entity type', lambda f: rejects(f, ['B-'])),
        ('Reject unknown prefix', lambda f: rejects(f, ['E-X'])),
        ('Reject numeric tag', lambda f: rejects(f, [1])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['B-PER','I-PER','O']), []))
    ]
    return run_cases(namespace, 'invalid_bio_transitions', cases, mode)
