def run_tests(namespace, mode="all"):
    cases = [
        ('Mixed lengths', lambda f: assert_close(f([[1,2,3],[4]], 2), dict(sequences=[[1,2],[4]],original_lengths=[3,1],dropped_counts=[1,0]))),
        ('Zero limit', lambda f: assert_close(f([[1],[]], 0), dict(sequences=[[],[]],original_lengths=[1,0],dropped_counts=[1,0]))),
        ('Exact length', lambda f: assert_close(f([[1,2]], 2), dict(sequences=[[1,2]],original_lengths=[2],dropped_counts=[0]))),
        ('No sequences', lambda f: assert_close(f([], 3), dict(sequences=[],original_lengths=[],dropped_counts=[]))),
        ('Empty sequence', lambda f: assert_close(f([[]], 4), dict(sequences=[[]],original_lengths=[0],dropped_counts=[0]))),
        ('Preserve token values', lambda f: assert_close(f([['a',None,'c']], 2), dict(sequences=[['a',None]],original_lengths=[3],dropped_counts=[1]))),
        ('Reject negative limit', lambda f: rejects(f, [], -1)),
        ('Reject raw sequence', lambda f: rejects(f, ['abc'], 2)),
        ('Reject boolean limit', lambda f: rejects(f, [], True)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [[1,2,3],[4]], 2), dict(sequences=[[1,2],[4]],original_lengths=[3,1],dropped_counts=[1,0])))
    ]
    return run_cases(namespace, 'truncate_sequences', cases, mode)
