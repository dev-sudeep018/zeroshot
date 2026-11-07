def run_tests(namespace, mode="all"):
    cases = [
        ('No distance penalty', lambda f: assert_close(f([[[0],[0]]],[[[0],[0]]],[[[0],[8]]],[0]),np.array([[[4.],[4.]]]))),
        ('Prefer the nearest position', lambda f: assert_close(f([[[0],[0]]],[[[0],[0]]],[[[0],[8]]],[np.log(3)]),np.array([[[2.],[6.]]]))),
        ('A single position', lambda f: assert_close(f([[[1]]],[[[1]]],[[[7,9]]],[2]),np.array([[[7.,9.]]]))),
        ('Independent head slopes', lambda f: assert_close(f(np.zeros((2,2,1)),np.zeros((2,2,1)),np.array([[[0],[8]],[[0],[8]]]),[0,np.log(3)]),np.array([[[4],[4]],[[2],[6]]]))),
        ('Scale content scores', lambda f: assert_close(f([[[1,1],[0,0]]],[[[1,1],[0,0]]],[[[1],[0]]],[0]),np.array([[[1/(1+np.exp(-np.sqrt(2)))],[.5]]]))),
        ('Stable extreme scores', lambda f: assert_close(f([[[1000],[1000]]],[[[1000],[-1000]]],[[[3],[9]]],[0]),np.full((1,2,1),3.))),
        ('Normalize boundaries', lambda f: assert_close(f(np.zeros((1,3,1)),np.zeros((1,3,1)),[[[0],[0],[21]]],[np.log(2)]),np.array([[[3.],[5.25],[12.]]]))),
        ('Reject negative slope', lambda f: rejects(f,[[[0]]],[[[0]]],[[[1]]],[-1])),
        ('Reject shared scalar slope', lambda f: rejects(f,[[[0]]],[[[0]]],[[[1]]],0)),
        ('Reject mismatched keys', lambda f: rejects(f,[[[0]]],[[[0],[0]]],[[[1]]],[0])),
        ('Reject nonfinite values', lambda f: rejects(f,[[[0]]],[[[0]]],[[[np.nan]]],[0])),
        ('No mutation', lambda f: assert_close(unchanged(f,np.zeros((1,2,1)),np.zeros((1,2,1)),np.array([[[0.],[8.]]]),np.zeros(1)),np.full((1,2,1),4.)))
    ]
    return run_cases(namespace, 'alibi_attention', cases, mode)
