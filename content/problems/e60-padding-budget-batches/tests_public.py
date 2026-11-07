def run_tests(namespace, mode="all"):
    cases = [
        ('Padding can exceed raw-length sum', lambda f: assert_close(f([2,5,2], 8, 10), dict(batches=[[0],[1],[2]],padded_tokens=[2,5,2]))),
        ('Exact budget fits', lambda f: assert_close(f([2,4], 8, 10), dict(batches=[[0,1]],padded_tokens=[8]))),
        ('Row-count cap', lambda f: assert_close(f([1,1,1], 10, 2), dict(batches=[[0,1],[2]],padded_tokens=[2,1]))),
        ('Empty input', lambda f: assert_close(f([], 10, 2), dict(batches=[],padded_tokens=[]))),
        ('Longest value persists', lambda f: assert_close(f([4,1,1], 12, 3), dict(batches=[[0,1,2]],padded_tokens=[12]))),
        ('One sequence per batch', lambda f: assert_close(f([2,3], 10, 1), dict(batches=[[0],[1]],padded_tokens=[2,3]))),
        ('Reject sequence cannot fit', lambda f: rejects(f, [11], 10, 2)),
        ('Reject zero-length sequence', lambda f: rejects(f, [0], 10, 2)),
        ('Reject zero row cap', lambda f: rejects(f, [1], 10, 0)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [2,5,2], 8, 10), dict(batches=[[0],[1],[2]],padded_tokens=[2,5,2])))
    ]
    return run_cases(namespace, 'padding_batches', cases, mode)
