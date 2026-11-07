def run_tests(namespace, mode="all"):
    cases = [
        ('Physical order differs from logical order', lambda f: assert_close(f(np.array([[[1],[2]],[[3],[4]]]), [[1,0]], [3]), [np.array([[3.],[4.],[1.]])])),
        ('Truncate final page', lambda f: assert_close(f(np.array([[[1],[99]]]), [[0]], [1]), [np.array([[1.]])])),
        ('Zero tokens', lambda f: assert_close(f(np.array([[[1],[2]]]), [[0]], [0]), [np.empty((0,1))])),
        ('Shared page across sequences', lambda f: assert_close(f(np.array([[[1],[2]]]), [[0],[0]], [1,2]), [np.array([[1.]]),np.array([[1.],[2.]])])),
        ('Repeated logical page', lambda f: assert_close(f(np.array([[[7]]]), [[0,0]], [2]), [np.array([[7.],[7.]])])),
        ('Feature dimension retained', lambda f: assert_close(f(np.array([[[1,2],[3,4]]]), [[0]], [2]), [np.array([[1.,2.],[3.,4.]])])),
        ('Reject unknown page', lambda f: rejects(f, np.array([[[1]]]), [[1]], [1])),
        ('Reject length beyond capacity', lambda f: rejects(f, np.array([[[1]]]), [[0]], [2])),
        ('Reject fractional page ID', lambda f: rejects(f, np.array([[[1]]]), [[.5]], [1])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, np.array([[[1],[2]],[[3],[4]]]), [[1,0]], [3]), [np.array([[3.],[4.],[1.]])]))
    ]
    return run_cases(namespace, 'gather_kv_pages', cases, mode)
