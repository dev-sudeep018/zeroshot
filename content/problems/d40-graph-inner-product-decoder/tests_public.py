def run_tests(namespace, mode="all"):
    cases = [
        ('No geometric evidence', lambda f: assert_close(f([[0],[0]]),np.full((2,2),.5))),
        ('Opposite embeddings', lambda f: assert_close(f([[1],[-1]]),np.array([[.731058578630005,.268941421369995],[.268941421369995,.731058578630005]]))),
        ('Orthogonal nodes', lambda f: assert_close(f(np.eye(2)),np.array([[.731058578630005,.5],[.5,.731058578630005]]))),
        ('Stable extreme similarities', lambda f: assert_close(f([[1000],[-1000]]),np.eye(2))),
        ('Do not remove self pairs', lambda f: assert_close(f([[2]]),np.array([[1/(1+np.exp(-4))]]))),
        ('Node count differs from feature count', lambda f: assert_close(f(np.zeros((3,2))),np.full((3,3),.5))),
        ('Repeated nodes retain equal probabilities', lambda f: assert_close(f([[1],[1]]),np.full((2,2),1/(1+np.exp(-1))))),
        ('Reject vector input', lambda f: rejects(f,[1,2])),
        ('Reject empty nodes', lambda f: rejects(f,np.empty((0,2)))),
        ('Reject nonfinite embeddings', lambda f: rejects(f,[[np.nan]])),
        ('Reject boolean embeddings', lambda f: rejects(f,[[True]])),
        ('No mutation', lambda f: assert_close(unchanged(f,np.zeros((2,1))),np.full((2,2),.5)))
    ]
    return run_cases(namespace, 'decode_graph', cases, mode)
