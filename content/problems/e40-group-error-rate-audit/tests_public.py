def run_tests(namespace, mode="all"):
    cases = [
        ('Same selection unequal errors', lambda f: assert_close(f([1,0,1,0], [1,0,0,1], ['a','a','b','b']), {'a':dict(count=2,positives=1,negatives=1,selection_rate=.5,tpr=1.,fpr=0.),'b':dict(count=2,positives=1,negatives=1,selection_rate=.5,tpr=0.,fpr=1.)})),
        ('No positive labels', lambda f: assert_close(f([0,0], [1,0], ['a','a']), {'a':dict(count=2,positives=0,negatives=2,selection_rate=.5,tpr=0.,fpr=.5)})),
        ('No negative labels', lambda f: assert_close(f([1,1], [1,0], ['a','a']), {'a':dict(count=2,positives=2,negatives=0,selection_rate=.5,tpr=.5,fpr=0.)})),
        ('Empty audit', lambda f: assert_close(f([], [], []), {})),
        ('Perfect predictions', lambda f: assert_close(f([1,0], [1,0], ['g','g']), {'g':dict(count=2,positives=1,negatives=1,selection_rate=.5,tpr=1.,fpr=0.)})),
        ('All rejected', lambda f: assert_close(f([1,0], [0,0], ['g','g']), {'g':dict(count=2,positives=1,negatives=1,selection_rate=0.,tpr=0.,fpr=0.)})),
        ('Reject nonbinary label', lambda f: rejects(f, [2], [1], ['a'])),
        ('Reject missing group', lambda f: rejects(f, [1], [1], [])),
        ('Reject mismatched predictions', lambda f: rejects(f, [1], [], ['a'])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1,0,1,0], [1,0,0,1], ['a','a','b','b']), {'a':dict(count=2,positives=1,negatives=1,selection_rate=.5,tpr=1.,fpr=0.),'b':dict(count=2,positives=1,negatives=1,selection_rate=.5,tpr=0.,fpr=1.)}))
    ]
    return run_cases(namespace, 'group_error_rates', cases, mode)
