def run_tests(namespace, mode="all"):
    cases = [
        ('Skip shared document', lambda f: assert_close(f([1,2,3], [1,4,2], 4), dict(documents=[1,4,2,3],owners=[0,1,0,0]))),
        ('Disjoint rankings alternate', lambda f: assert_close(f([1,2], [3,4], 4), dict(documents=[1,3,2,4],owners=[0,1,0,1]))),
        ('Left exhausted immediately', lambda f: assert_close(f([], [3,4], 3), dict(documents=[3,4],owners=[1,1]))),
        ('Repeated IDs remain unique', lambda f: assert_close(f([1,1,2], [1,1], 4), dict(documents=[1,2],owners=[0,0]))),
        ('Zero requested results', lambda f: assert_close(f([1], [2], 0), dict(documents=[],owners=[]))),
        ('Cut off after one result', lambda f: assert_close(f([5,6], [7], 1), dict(documents=[5],owners=[0]))),
        ('Reject negative document ID', lambda f: rejects(f, [-1], [2], 1)),
        ('Reject negative requested count', lambda f: rejects(f, [1], [2], -1)),
        ('Reject fractional document ID', lambda f: rejects(f, [1.5], [2], 1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1,2,3], [1,4,2], 4), dict(documents=[1,4,2,3],owners=[0,1,0,0])))
    ]
    return run_cases(namespace, 'interleave_rankings', cases, mode)
