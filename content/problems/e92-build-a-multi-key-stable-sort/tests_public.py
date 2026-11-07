def run_tests(namespace, mode="all"):
    cases = [
        ('Two sort directions', lambda f: assert_close(f([dict(category='b',priority=9),dict(category='a',priority=1),dict(category='a',priority=3)]), [dict(category='a',priority=3),dict(category='a',priority=1),dict(category='b',priority=9)])),
        ('Stable exact ties', lambda f: assert_close(f([dict(category='a',priority=1,id='z'),dict(category='a',priority=1,id='a')]), [dict(category='a',priority=1,id='z'),dict(category='a',priority=1,id='a')])),
        ('Negative priorities', lambda f: assert_close(f([dict(category='a',priority=-2),dict(category='a',priority=-1)]), [dict(category='a',priority=-1),dict(category='a',priority=-2)])),
        ('Empty rows', lambda f: assert_close(f([]), [])),
        ('One row', lambda f: assert_close(f([dict(category='x',priority=0)]), [dict(category='x',priority=0)])),
        ('Case-sensitive order', lambda f: assert_close(f([dict(category='a',priority=1),dict(category='A',priority=1)]), [dict(category='A',priority=1),dict(category='a',priority=1)])),
        ('Reject missing category', lambda f: rejects(f, [dict(priority=1)])),
        ('Reject fractional priority', lambda f: rejects(f, [dict(category='a',priority=1.5)])),
        ('Reject empty category', lambda f: rejects(f, [dict(category='',priority=1)])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [dict(category='b',priority=9),dict(category='a',priority=1),dict(category='a',priority=3)]), [dict(category='a',priority=3),dict(category='a',priority=1),dict(category='b',priority=9)]))
    ]
    return run_cases(namespace, 'sort_work_records', cases, mode)
