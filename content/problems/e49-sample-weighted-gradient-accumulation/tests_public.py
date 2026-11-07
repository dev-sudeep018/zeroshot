def run_tests(namespace, mode="all"):
    cases = [
        ('Unequal microbatch sizes', lambda f: assert_close(f([[1,3],[5,7]], [3,1]), np.array([2.,4.]))),
        ('Equal counts', lambda f: assert_close(f([[1],[3]], [2,2]), np.array([2.]))),
        ('One microbatch', lambda f: assert_close(f([[2,-3]], [10]), np.array([2.,-3.]))),
        ('Opposing gradients cancel', lambda f: assert_close(f([[2],[-1]], [1,2]), np.array([0.]))),
        ('Matrix parameter', lambda f: assert_close(f(np.array([[[1,2]],[[3,4]]]), [1,1]), np.array([[2.,3.]]))),
        ('Zero gradients', lambda f: assert_close(f(np.zeros((3,2)), [1,2,3]), np.zeros(2))),
        ('Reject zero count', lambda f: rejects(f, [[1],[2]], [1,0])),
        ('Reject batch mismatch', lambda f: rejects(f, [[1],[2]], [1])),
        ('Reject missing parameter axis', lambda f: rejects(f, [1,2], [1,1])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[1,3],[5,7]], [3,1]), np.array([2.,4.])))
    ]
    return run_cases(namespace, 'accumulate_gradients', cases, mode)
