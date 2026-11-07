def run_tests(namespace, mode="all"):
    cases = [
        ('Interleaving times', lambda f: assert_close(f([[1,'a'],[3,'c']], [[2,'b']]), [[1,'a'],[2,'b'],[3,'c']])),
        ('Left-first ties', lambda f: assert_close(f([[1,'l1'],[1,'l2']], [[1,'r']]), [[1,'l1'],[1,'l2'],[1,'r']])),
        ('Empty left', lambda f: assert_close(f([], [[2,'r']]), [[2,'r']])),
        ('Both empty', lambda f: assert_close(f([], []), [])),
        ('Empty right', lambda f: assert_close(f([[1,'l']], []), [[1,'l']])),
        ('Negative timestamps', lambda f: assert_close(f([[-2,'a']], [[-1,'b']]), [[-2,'a'],[-1,'b']])),
        ('Reject unsorted stream', lambda f: rejects(f, [[2,'a'],[1,'b']], [])),
        ('Reject bad event width', lambda f: rejects(f, [[1]], [])),
        ('Reject empty event ID', lambda f: rejects(f, [[1,'']], [])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [[1,'a'],[3,'c']], [[2,'b']]), [[1,'a'],[2,'b'],[3,'c']]))
    ]
    return run_cases(namespace, 'merge_events', cases, mode)
