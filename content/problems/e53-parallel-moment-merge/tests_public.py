def run_tests(namespace, mode="all"):
    cases = [
        ('Between-partition variation matters', lambda f: assert_close(f([2,2], [1.5,3.5], [.5,.5]), dict(count=4,mean=2.5,m2=5.))),
        ('Unequal partition sizes', lambda f: assert_close(f([1,3], [0,4], [0,2]), dict(count=4,mean=3.,m2=14.))),
        ('Ignore empty partitions', lambda f: assert_close(f([0,2], [0,3], [0,2]), dict(count=2,mean=3.,m2=2.))),
        ('All partitions empty', lambda f: assert_close(f([0,0], [0,0], [0,0]), dict(count=0,mean=0.,m2=0.))),
        ('No partitions', lambda f: assert_close(f([], [], []), dict(count=0,mean=0.,m2=0.))),
        ('Equal means add m2', lambda f: assert_close(f([2,3], [5,5], [2,6]), dict(count=5,mean=5.,m2=8.))),
        ('Reject inconsistent empty partition', lambda f: rejects(f, [0], [1], [0])),
        ('Reject negative dispersion', lambda f: rejects(f, [2], [1], [-1])),
        ('Reject mismatched state lengths', lambda f: rejects(f, [1,2], [0], [0,0])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [2,2], [1.5,3.5], [.5,.5]), dict(count=4,mean=2.5,m2=5.)))
    ]
    return run_cases(namespace, 'merge_moments', cases, mode)
