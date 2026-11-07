def run_tests(namespace, mode="all"):
    cases = [
        ('Least loaded choice', lambda f: assert_close(f([3,2,4,1],2), dict(assignments=[0,1,1,0],loads=[4,6],makespan=6))),
        ('Tie uses first worker', lambda f: assert_close(f([2,2,1],2), dict(assignments=[0,1,0],loads=[3,2],makespan=3))),
        ('Zero jobs keep ties', lambda f: assert_close(f([0,0,1],2), dict(assignments=[0,0,0],loads=[1,0],makespan=1))),
        ('No jobs', lambda f: assert_close(f([],3), dict(assignments=[],loads=[0,0,0],makespan=0))),
        ('One worker', lambda f: assert_close(f([1.5,2],1), dict(assignments=[0,0],loads=[3.5],makespan=3.5))),
        ('More workers than jobs', lambda f: assert_close(f([5],3), dict(assignments=[0],loads=[5,0,0],makespan=5))),
        ('Reject negative duration', lambda f: rejects(f, [-1],2)),
        ('Reject zero workers', lambda f: rejects(f, [],0)),
        ('Reject bool duration', lambda f: rejects(f, [True],2)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [3,2,4,1],2), dict(assignments=[0,1,1,0],loads=[4,6],makespan=6)))
    ]
    return run_cases(namespace, 'worker_schedule', cases, mode)
