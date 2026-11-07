def run_tests(namespace, mode="all"):
    cases = [
        ('One local violation', lambda f: assert_close(f([1,3,2,4],[1,1,1,1]), np.array([1.,2.5,2.5,4]))),
        ('Weighted merge', lambda f: assert_close(f([3,1],[1,3]), np.array([1.5,1.5]))),
        ('Already increasing', lambda f: assert_close(f([1,2,3],[4,2,1]), np.array([1.,2,3]))),
        ('Fully decreasing', lambda f: assert_close(f([3,2,1],[1,1,1]), np.array([2.,2,2]))),
        ('Merge cascades backward', lambda f: assert_close(f([1,4,3,0],[1,1,1,1]), np.array([1.,7/3,7/3,7/3]))),
        ('Single observation', lambda f: assert_close(f([9],[2]), np.array([9.]))),
        ('Reject zero weight', lambda f: rejects(f,[1,2],[1,0])),
        ('Reject weight shape', lambda f: rejects(f,[1,2],[1])),
        ('Reject negative weight', lambda f: rejects(f,[1],[-1])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([1.,3,2,4]),np.array([1.,1,1,1])),np.array([1.,2.5,2.5,4]))),
    ]
    return run_cases(namespace, 'isotonic_fit', cases, mode)
