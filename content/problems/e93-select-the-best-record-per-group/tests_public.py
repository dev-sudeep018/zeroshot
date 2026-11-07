def run_tests(namespace, mode="all"):
    cases = [
        ('Higher score wins', lambda f: assert_close(f([dict(group='a',score=1),dict(group='a',score=3)]), {'a':dict(group='a',score=3)})),
        ('First tie retained', lambda f: assert_close(f([dict(group='a',score=2,id='x'),dict(group='a',score=2,id='y')]), {'a':dict(group='a',score=2,id='x')})),
        ('Negative scores', lambda f: assert_close(f([dict(group='a',score=-3),dict(group='a',score=-1)]), {'a':dict(group='a',score=-1)})),
        ('Empty records', lambda f: assert_close(f([]), {})),
        ('Separate groups', lambda f: assert_close(f([dict(group='a',score=1),dict(group='b',score=0)]), {'a':dict(group='a',score=1),'b':dict(group='b',score=0)})),
        ('Zero score', lambda f: assert_close(f([dict(group='z',score=0)]), {'z':dict(group='z',score=0)})),
        ('Reject missing score', lambda f: rejects(f, [dict(group='a')])),
        ('Reject boolean score', lambda f: rejects(f, [dict(group='a',score=True)])),
        ('Reject nonfinite score', lambda f: rejects(f, [dict(group='a',score=float('nan'))])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [dict(group='a',score=1),dict(group='a',score=3)]), {'a':dict(group='a',score=3)}))
    ]
    return run_cases(namespace, 'best_per_group', cases, mode)
