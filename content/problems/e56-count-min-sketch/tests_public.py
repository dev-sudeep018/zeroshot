def run_tests(namespace, mode="all"):
    cases = [
        ('Second hash removes a collision', lambda f: assert_close(f([[0,0],[0,1]], [2,3], [[0,0],[0,1]], 2), dict(sketch=np.array([[5,0],[2,3]]),estimates=np.array([2,3])))),
        ('All rows collide', lambda f: assert_close(f([[0,0],[0,0]], [2,3], [[0,0]], 2), dict(sketch=np.array([[5,0],[5,0]]),estimates=np.array([5])))),
        ('Unseen buckets remain zero', lambda f: assert_close(f([[0,0]], [4], [[1,1]], 2), dict(sketch=np.array([[4,0],[4,0]]),estimates=np.array([0])))),
        ('Zero increment', lambda f: assert_close(f([[0]], [0], [[0]], 1), dict(sketch=np.array([[0]]),estimates=np.array([0])))),
        ('No updates', lambda f: assert_close(f(np.empty((0,2)), [], [[0,1]], 2), dict(sketch=np.zeros((2,2),dtype=int),estimates=np.array([0])))),
        ('Repeated update accumulates', lambda f: assert_close(f([[1],[1]], [2,3], [[1]], 2), dict(sketch=np.array([[0,5]]),estimates=np.array([5])))),
        ('Reject negative count', lambda f: rejects(f, [[0]], [-1], [[0]], 1)),
        ('Reject bucket outside width', lambda f: rejects(f, [[1]], [1], [[0]], 1)),
        ('Reject different depth', lambda f: rejects(f, [[0,0]], [1], [[0]], 1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[0,0],[0,1]], [2,3], [[0,0],[0,1]], 2), dict(sketch=np.array([[5,0],[2,3]]),estimates=np.array([2,3]))))
    ]
    return run_cases(namespace, 'count_min_sketch', cases, mode)
