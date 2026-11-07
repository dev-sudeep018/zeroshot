def run_tests(namespace, mode="all"):
    cases = [
        ('Separate group rates', lambda f: assert_close(f(['a','b','c'], ['a','x','c'], ['x','x','y']), {'x':dict(correct=1,total=2,accuracy=.5),'y':dict(correct=1,total=1,accuracy=1.0)})),
        ('Exact case matters', lambda f: assert_close(f(['A'], ['a'], ['g']), {'g':dict(correct=0,total=1,accuracy=0.0)})),
        ('Empty answers match', lambda f: assert_close(f([''], [''], ['g']), {'g':dict(correct=1,total=1,accuracy=1.0)})),
        ('No examples', lambda f: assert_close(f([], [], []), {})),
        ('All wrong', lambda f: assert_close(f(['a','b'], ['x','y'], ['g','g']), {'g':dict(correct=0,total=2,accuracy=0.0)})),
        ('Noncontiguous group', lambda f: assert_close(f(['a','b','c'], ['a','b','x'], ['x','y','x']), {'x':dict(correct=1,total=2,accuracy=.5),'y':dict(correct=1,total=1,accuracy=1.0)})),
        ('Reject mismatched predictions', lambda f: rejects(f, ['a'], [], ['g'])),
        ('Reject empty group', lambda f: rejects(f, ['a'], ['a'], [''])),
        ('Reject nontext answer', lambda f: rejects(f, [1], ['1'], ['g'])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['a','b','c'], ['a','x','c'], ['x','x','y']), {'x':dict(correct=1,total=2,accuracy=.5),'y':dict(correct=1,total=1,accuracy=1.0)}))
    ]
    return run_cases(namespace, 'group_accuracy', cases, mode)
