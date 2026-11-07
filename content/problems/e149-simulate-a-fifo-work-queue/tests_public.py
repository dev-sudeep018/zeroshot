def run_tests(namespace, mode="all"):
    cases = [
        ('First in first out', lambda f: assert_close(f([['put','a'],['put','b'],['take']]), dict(served=['a'],pending=['b']))),
        ('Empty removal', lambda f: assert_close(f([['take'],['put','x'],['take'],['take']]), dict(served=[None,'x',None],pending=[]))),
        ('Duplicate jobs', lambda f: assert_close(f([['put','x'],['put','x'],['take']]), dict(served=['x'],pending=['x']))),
        ('No operations', lambda f: assert_close(f([]), dict(served=[],pending=[]))),
        ('Only insertions', lambda f: assert_close(f([['put','a'],['put','b']]), dict(served=[],pending=['a','b']))),
        ('Interleaved', lambda f: assert_close(f([['put','a'],['take'],['put','b'],['take']]), dict(served=['a','b'],pending=[]))),
        ('Reject unknown command', lambda f: rejects(f, [['pop']])),
        ('Reject bad arity', lambda f: rejects(f, [['take','x']])),
        ('Reject empty ID', lambda f: rejects(f, [['put','']])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [['put','a'],['put','b'],['take']]), dict(served=['a'],pending=['b'])))
    ]
    return run_cases(namespace, 'fifo_queue', cases, mode)
