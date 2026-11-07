def run_tests(namespace, mode="all"):
    cases = [
        ('Exact ties choose lower path', lambda f: assert_close(f(np.zeros((2,2)),np.zeros((2,2)),[0,0],[0,0]),{"path":np.array([0,0]),"score":0.})),
        ('One-step best label', lambda f: assert_close(f([[1,3]],np.zeros((2,2)),[0,0],[0,0]),{"path":np.array([1]),"score":3.})),
        ('Transition overrides local choices', lambda f: assert_close(f([[2,0],[2,0]],[[0,10],[0,0]],[0,0],[0,0]),{"path":np.array([0,1]),"score":12.})),
        ('End score changes winner', lambda f: assert_close(f([[2,0]],np.zeros((2,2)),[0,0],[0,3]),{"path":np.array([1]),"score":3.})),
        ('Single-label chain', lambda f: assert_close(f([[1],[2],[3]],[[4]],[5],[6]),{"path":np.array([0,0,0]),"score":25.})),
        ('Prefix tie compares full path', lambda f: assert_close(f(np.zeros((2,2)),[[0,1],[1,0]],[0,0],[0,0]),{"path":np.array([0,1]),"score":1.})),
        ('Negative scores preserved', lambda f: assert_close(f([[-3,-1]],np.zeros((2,2)),[0,0],[0,0]),{"path":np.array([1]),"score":-1.})),
        ('Reject transition width', lambda f: rejects(f,[[0,0]],[[0]],[0,0],[0,0])),
        ('Reject start width', lambda f: rejects(f,[[0,0]],np.zeros((2,2)),[0],[0,0])),
        ('Reject nonfinite emission', lambda f: rejects(f,[[np.nan]],[[0]],[0],[0])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,np.zeros((2,2)),np.zeros((2,2)),[0,0],[0,0]),{"path":np.array([0,0]),"score":0.})),
    ]
    return run_cases(namespace, 'chain_viterbi', cases, mode)
