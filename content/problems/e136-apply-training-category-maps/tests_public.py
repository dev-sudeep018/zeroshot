def run_tests(namespace, mode="all"):
    cases = [
        ('Train-only vocabulary', lambda f: assert_close(f(['b','a','b'], ['a','c']), dict(vocabulary={'b':0,'a':1},train_codes=[0,1,0],heldout_codes=[1,-1],unknown_positions=[1]))),
        ('Empty training', lambda f: assert_close(f([], ['a']), dict(vocabulary={},train_codes=[],heldout_codes=[-1],unknown_positions=[0]))),
        ('Empty category', lambda f: assert_close(f([''], ['','x']), dict(vocabulary={'':0},train_codes=[0],heldout_codes=[0,-1],unknown_positions=[1]))),
        ('Both empty', lambda f: assert_close(f([], []), dict(vocabulary={},train_codes=[],heldout_codes=[],unknown_positions=[]))),
        ('No heldout', lambda f: assert_close(f(['x','x'], []), dict(vocabulary={'x':0},train_codes=[0,0],heldout_codes=[],unknown_positions=[]))),
        ('Case-sensitive', lambda f: assert_close(f(['A'], ['a']), dict(vocabulary={'A':0},train_codes=[0],heldout_codes=[-1],unknown_positions=[0]))),
        ('Reject nontext training', lambda f: rejects(f, [1], [])),
        ('Reject nontext heldout', lambda f: rejects(f, [], [None])),
        ('Reject raw training', lambda f: rejects(f, 'a', [])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['b','a','b'], ['a','c']), dict(vocabulary={'b':0,'a':1},train_codes=[0,1,0],heldout_codes=[1,-1],unknown_positions=[1])))
    ]
    return run_cases(namespace, 'fit_category_codes', cases, mode)
