def run_tests(namespace, mode="all"):
    cases = [
        ('Extra candidate words', lambda f: assert_close(f(['a','x','b'], ['a','b']), dict(lcs=2,precision=2/3,recall=1.,f1=0.8))),
        ('Short candidate', lambda f: assert_close(f(['a'], ['a','b','c']), dict(lcs=1,precision=1.,recall=1/3,f1=0.5))),
        ('Reordered tokens', lambda f: assert_close(f(['b','a'], ['a','b']), dict(lcs=1,precision=0.5,recall=0.5,f1=0.5))),
        ('Empty pair', lambda f: assert_close(f([], []), dict(lcs=0,precision=0.,recall=0.,f1=0.))),
        ('Identical repeated tokens', lambda f: assert_close(f(['a','a'], ['a','a']), dict(lcs=2,precision=1.,recall=1.,f1=1.))),
        ('No overlap', lambda f: assert_close(f(['a'], ['b']), dict(lcs=0,precision=0.,recall=0.,f1=0.))),
        ('Reject raw string', lambda f: rejects(f, 'a', ['a'])),
        ('Reject empty token', lambda f: rejects(f, [''], ['a'])),
        ('Reject too many tokens', lambda f: rejects(f, [], ['a']*501)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, ['a','x','b'], ['a','b']), dict(lcs=2,precision=2/3,recall=1.,f1=0.8)))
    ]
    return run_cases(namespace, 'rouge_l', cases, mode)
