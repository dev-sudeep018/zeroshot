def run_tests(namespace, mode="all"):
    cases = [
        ('Quarter image', lambda f: assert_close(f(np.zeros((2,2)),np.ones((2,2)),[1,0],[0,1],[0,0,1,1]), {'image':np.array([[1.0, 0.0], [0.0, 0.0]], dtype='float64'),'label':np.array([0.75, 0.25], dtype='float64'),'replaced_fraction':0.25})),
        ('Clipped half', lambda f: assert_close(f(np.zeros((2,2)),np.ones((2,2)),[1,0],[0,1],[-2,0,1,2]), {'image':np.array([[1.0, 1.0], [0.0, 0.0]], dtype='float64'),'label':np.array([0.5, 0.5], dtype='float64'),'replaced_fraction':0.5})),
        ('Whole image', lambda f: assert_close(f([[1]],[[2]],[1,0],[0,1],[0,0,1,1]), {'image':np.array([[2.0]], dtype='float64'),'label':np.array([0.0, 1.0], dtype='float64'),'replaced_fraction':1.0})),
        ('Outside rectangle', lambda f: assert_close(f([[1]],[[2]],[1,0],[0,1],[2,2,3,3]), {'image':np.array([[1.0]], dtype='float64'),'label':np.array([1.0, 0.0], dtype='float64'),'replaced_fraction':0.0})),
        ('Soft labels', lambda f: assert_close(f(np.zeros((2,2)),np.ones((2,2)),[0.8,0.2],[0.4,0.6],[0,0,1,2]), {'image':np.array([[1.0, 1.0], [0.0, 0.0]], dtype='float64'),'label':np.array([0.6000000000000001, 0.4], dtype='float64'),'replaced_fraction':0.5})),
        ('Empty rectangle', lambda f: assert_close(f([[1,2]],[[3,4]],[1],[1],[0,1,1,1]), {'image':np.array([[1.0, 2.0]], dtype='float64'),'label':np.array([1.0], dtype='float64'),'replaced_fraction':0.0})),
        ('Reject different image shapes', lambda f: rejects(f, [[1]],[[1,2]],[1],[1],[0,0,1,1])),
        ('Reject bad label sum', lambda f: rejects(f, [[1]],[[2]],[0.2,0.2],[1,0],[0,0,1,1])),
        ('Reject reversed patch', lambda f: rejects(f, [[1]],[[2]],[1],[1],[1,0,0,1])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, np.zeros((2,2)),np.ones((2,2)),[1,0],[0,1],[0,0,1,1]), {'image':np.array([[1.0, 0.0], [0.0, 0.0]], dtype='float64'),'label':np.array([0.75, 0.25], dtype='float64'),'replaced_fraction':0.25})),
    ]
    return run_cases(namespace, 'cutmix_pair', cases, mode)
