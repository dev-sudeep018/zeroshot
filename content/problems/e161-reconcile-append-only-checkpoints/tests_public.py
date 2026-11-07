def run_tests(namespace, mode="all"):
    cases = [
        ('Stop at first gap', lambda f: assert_close(f(2,[3,5,6]), dict(committed=3,pending=[5,6]))),
        ('Close earlier gap', lambda f: assert_close(f(2,[6,5,3,4]), dict(committed=6,pending=[]))),
        ('Start before zero', lambda f: assert_close(f(-1,[0,1,3]), dict(committed=1,pending=[3]))),
        ('No acknowledgments', lambda f: assert_close(f(4,[]), dict(committed=4,pending=[]))),
        ('Old and repeated IDs', lambda f: assert_close(f(2,[0,2,3,3,5]), dict(committed=3,pending=[5]))),
        ('No next ID', lambda f: assert_close(f(2,[8,6]), dict(committed=2,pending=[6,8]))),
        ('Reject invalid initial', lambda f: rejects(f, -2,[])),
        ('Reject negative acknowledgment', lambda f: rejects(f, 0,[-1])),
        ('Reject bool acknowledgment', lambda f: rejects(f, 0,[True])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, 2,[3,5,6]), dict(committed=3,pending=[5,6])))
    ]
    return run_cases(namespace, 'advance_checkpoint', cases, mode)
