def run_tests(namespace, mode="all"):
    cases = [
        ('Two clusters', lambda f: assert_close(f([[0],[2],[8],[10]],[0,0,1,1],[[1],[5],[9]],2), {'centroids':np.array([[1.0], [9.0]], dtype=float).reshape((2, 1)),'predictions':np.array([0, 0, 1], dtype=float).reshape((3,))})),
        ('Two-dimensional classes', lambda f: assert_close(f([[0,0],[2,0],[0,4],[2,4]],[0,0,1,1],[[1,1],[1,3]],2), {'centroids':np.array([[1.0, 0.0], [1.0, 4.0]], dtype=float).reshape((2, 2)),'predictions':np.array([0, 1], dtype=float).reshape((2,))})),
        ('One class', lambda f: assert_close(f([[1],[3]],[0,0],[[99],[-1]],1), {'centroids':np.array([[2.0]], dtype=float).reshape((1, 1)),'predictions':np.array([0, 0], dtype=float).reshape((2,))})),
        ('Tie chooses first class', lambda f: assert_close(f([[0],[2]],[0,1],[[1]],2), {'centroids':np.array([[0.0], [2.0]], dtype=float).reshape((2, 1)),'predictions':np.array([0], dtype=float).reshape((1,))})),
        ('Unsorted training labels', lambda f: assert_close(f([[10],[0],[8],[2]],[1,0,1,0],[[5],[9]],2), {'centroids':np.array([[1.0], [9.0]], dtype=float).reshape((2, 1)),'predictions':np.array([0, 1], dtype=float).reshape((2,))})),
        ('Three classes', lambda f: assert_close(f([[0],[4],[8]],[0,1,2],[[3],[7],[0]],3), {'centroids':np.array([[0.0], [4.0], [8.0]], dtype=float).reshape((3, 1)),'predictions':np.array([1, 2, 0], dtype=float).reshape((3,))})),
        ('Reject missing class', lambda f: rejects(f,[[0]],[0],[[1]],2)),
        ('Reject feature mismatch', lambda f: rejects(f,[[0,1]],[0],[[1]],1)),
        ('Reject label length', lambda f: rejects(f,[[0],[1]],[0],[[1]],1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[0],[2],[8],[10]],[0,0,1,1],[[1],[5],[9]],2), {'centroids':np.array([[1.0], [9.0]], dtype=float).reshape((2, 1)),'predictions':np.array([0, 0, 1], dtype=float).reshape((3,))})),
    ]
    return run_cases(namespace, 'nearest_centroid_predict', cases, mode)
