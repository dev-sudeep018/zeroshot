def run_tests(namespace, mode="all"):
    cases = [
        ('Three inversions', lambda f: assert_close(f([2,1,0]), {'inversions':3,'parity':'odd'})),
        ('Already sorted', lambda f: assert_close(f([0,1,2,3]), {'inversions':0,'parity':'even'})),
        ('One swap', lambda f: assert_close(f([0,2,1,3]), {'inversions':1,'parity':'odd'})),
        ('Single element', lambda f: assert_close(f([0]), {'inversions':0,'parity':'even'})),
        ('Cycle', lambda f: assert_close(f([1,2,3,0]), {'inversions':3,'parity':'odd'})),
        ('Mixed order', lambda f: assert_close(f([3,0,4,1,2]), {'inversions':5,'parity':'odd'})),
        ('Reject duplicate', lambda f: rejects(f,[0,1,1])),
        ('Reject out of range', lambda f: rejects(f,[1,2,3])),
        ('Reject fractional values', lambda f: rejects(f,[0,1.5,2])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[2,1,0]), {'inversions':3,'parity':'odd'})),
    ]
    return run_cases(namespace, 'permutation_disorder', cases, mode)
