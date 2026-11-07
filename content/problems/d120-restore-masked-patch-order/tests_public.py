def run_tests(namespace, mode="all"):
    cases = [
        ('Unsorted visible patches', lambda f: assert_close(f([[5,6],[1,2]],[2,0],[-1,-1],4), {'tokens':np.array([[1.0, 2.0], [-1.0, -1.0], [5.0, 6.0], [-1.0, -1.0]], dtype='float64'),'masked':np.array([False, True, False, True], dtype='bool')})),
        ('All visible', lambda f: assert_close(f([[2],[3]],[1,0],[0],2), {'tokens':np.array([[3.0], [2.0]], dtype='float64'),'masked':np.array([False, False], dtype='bool')})),
        ('One visible patch', lambda f: assert_close(f([[7]],[1],[-2],3), {'tokens':np.array([[-2.0], [7.0], [-2.0]], dtype='float64'),'masked':np.array([True, False, True], dtype='bool')})),
        ('Token equals visible', lambda f: assert_close(f([[0]],[0],[0],2), {'tokens':np.array([[0.0], [0.0]], dtype='float64'),'masked':np.array([False, True], dtype='bool')})),
        ('Vector embeddings', lambda f: assert_close(f([[1,2,3]],[2],[4,5,6],3), {'tokens':np.array([[4.0, 5.0, 6.0], [4.0, 5.0, 6.0], [1.0, 2.0, 3.0]], dtype='float64'),'masked':np.array([True, True, False], dtype='bool')})),
        ('Single patch', lambda f: assert_close(f([[8]],[0],[1],1), {'tokens':np.array([[8.0]], dtype='float64'),'masked':np.array([False], dtype='bool')})),
        ('Reject repeated position', lambda f: rejects(f, [[1],[2]],[0,0],[0],2)),
        ('Reject position outside sequence', lambda f: rejects(f, [[1]],[2],[0],2)),
        ('Reject feature mismatch', lambda f: rejects(f, [[1,2]],[0],[0],2)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[5,6],[1,2]],[2,0],[-1,-1],4), {'tokens':np.array([[1.0, 2.0], [-1.0, -1.0], [5.0, 6.0], [-1.0, -1.0]], dtype='float64'),'masked':np.array([False, True, False, True], dtype='bool')})),
    ]
    return run_cases(namespace, 'restore_patches', cases, mode)
