def run_tests(namespace, mode="all"):
    cases = [
        ('Duplicate box suppressed', lambda f: assert_close(f([[0,0,1,1],[0,0,1,1],[2,2,3,3]], [.8,.9,.7], .5), [1,2])),
        ('Score tie keeps lower index', lambda f: assert_close(f([[0,0,1,1],[0,0,1,1]], [1,1], .5), [0])),
        ('Threshold equality survives', lambda f: assert_close(f([[0,0,1,1],[0,0,1,1]], [1,.5], 1), [0,1])),
        ('Disjoint boxes survive zero threshold', lambda f: assert_close(f([[0,0,1,1],[2,2,3,3]], [.1,.9], 0), [1,0])),
        ('Zero-area boxes survive', lambda f: assert_close(f([[0,0,0,0],[0,0,0,0]], [1,1], 0), [0,1])),
        ('Empty detections', lambda f: assert_close(f(np.empty((0,4)), [], .5), [])),
        ('Reject negative threshold', lambda f: rejects(f, [[0,0,1,1]], [1], -.1)),
        ('Reject score mismatch', lambda f: rejects(f, [[0,0,1,1]], [], .5)),
        ('Reject invalid geometry', lambda f: rejects(f, [[1,0,0,1]], [1], .5)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[0,0,1,1],[0,0,1,1],[2,2,3,3]], [.8,.9,.7], .5), [1,2]))
    ]
    return run_cases(namespace, 'non_max_suppression', cases, mode)
