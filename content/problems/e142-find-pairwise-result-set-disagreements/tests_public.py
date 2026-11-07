def run_tests(namespace, mode="all"):
    cases = [
        ('Partial overlap', lambda f: assert_close(f([['a','b']], [['b','c']]), [dict(overlap=['b'],left_only=['a'],right_only=['c'])])),
        ('Duplicates ignored', lambda f: assert_close(f([['a','a']], [['a']]), [dict(overlap=['a'],left_only=[],right_only=[])])),
        ('Empty first system', lambda f: assert_close(f([[]], [['x']]), [dict(overlap=[],left_only=[],right_only=['x'])])),
        ('No queries', lambda f: assert_close(f([], []), [])),
        ('Both empty result', lambda f: assert_close(f([[]], [[]]), [dict(overlap=[],left_only=[],right_only=[])])),
        ('Query order retained', lambda f: assert_close(f([['a'],['b']], [['b'],['b']]), [dict(overlap=[],left_only=['a'],right_only=['b']),dict(overlap=['b'],left_only=[],right_only=[])])),
        ('Reject query count mismatch', lambda f: rejects(f, [[]], [])),
        ('Reject empty ID', lambda f: rejects(f, [['']], [[]])),
        ('Reject raw query results', lambda f: rejects(f, ['abc'], [[]])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [['a','b']], [['b','c']]), [dict(overlap=['b'],left_only=['a'],right_only=['c'])]))
    ]
    return run_cases(namespace, 'result_disagreements', cases, mode)
