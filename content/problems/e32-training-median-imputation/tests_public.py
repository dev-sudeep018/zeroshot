def run_tests(namespace, mode="all"):
    cases = [
        ('Fit only observed training values', lambda f: assert_close(f([[1,10],[3,999]], [[100,0]], np.array([[False,False],[False,True]]), np.array([[False,True]])), dict(medians=np.array([2.,10.]),filled=np.array([[100.,10.]])))),
        ('Heldout extremes do not change median', lambda f: assert_close(f([[1],[3]], [[999],[0]], np.zeros((2,1),dtype=bool), np.array([[False],[True]])), dict(medians=np.array([2.]),filled=np.array([[999.],[2.]])))),
        ('Odd training count', lambda f: assert_close(f([[1],[9],[3]], [[0]], np.zeros((3,1),dtype=bool), np.ones((1,1),dtype=bool)), dict(medians=np.array([3.]),filled=np.array([[3.]])))),
        ('No replacements', lambda f: assert_close(f([[2]], [[8]], np.zeros((1,1),dtype=bool), np.zeros((1,1),dtype=bool)), dict(medians=np.array([2.]),filled=np.array([[8.]])))),
        ('Negative observations', lambda f: assert_close(f([[-4],[-2]], [[0]], np.zeros((2,1),dtype=bool), np.ones((1,1),dtype=bool)), dict(medians=np.array([-3.]),filled=np.array([[-3.]])))),
        ('One observed value', lambda f: assert_close(f([[99],[5]], [[0]], np.array([[True],[False]]), np.ones((1,1),dtype=bool)), dict(medians=np.array([5.]),filled=np.array([[5.]])))),
        ('Reject unobserved feature', lambda f: rejects(f, [[1]], [[0]], np.ones((1,1),dtype=bool), np.ones((1,1),dtype=bool))),
        ('Reject numeric mask', lambda f: rejects(f, [[1]], [[0]], np.array([[0]]), np.ones((1,1),dtype=bool))),
        ('Reject feature mismatch', lambda f: rejects(f, [[1,2]], [[0]], np.zeros((1,2),dtype=bool), np.ones((1,1),dtype=bool))),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[1,10],[3,999]], [[100,0]], np.array([[False,False],[False,True]]), np.array([[False,True]])), dict(medians=np.array([2.,10.]),filled=np.array([[100.,10.]]))))
    ]
    return run_cases(namespace, 'median_impute', cases, mode)
