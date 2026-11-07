def run_tests(namespace, mode="all"):
    cases = [
        ('Association', lambda f: assert_close(f([[3,1],[1,3]]), {'expected':np.array([[2.0, 2.0], [2.0, 2.0]], dtype=float).reshape((2, 2)),'residual':np.array([[1.0, -1.0], [-1.0, 1.0]], dtype=float).reshape((2, 2))})),
        ('Already independent', lambda f: assert_close(f([[1,2],[2,4]]), {'expected':np.array([[1.0, 2.0], [2.0, 4.0]], dtype=float).reshape((2, 2)),'residual':np.array([[0.0, 0.0], [0.0, 0.0]], dtype=float).reshape((2, 2))})),
        ('Zero row', lambda f: assert_close(f([[0,0],[2,4]]), {'expected':np.array([[0.0, 0.0], [2.0, 4.0]], dtype=float).reshape((2, 2)),'residual':np.array([[0.0, 0.0], [0.0, 0.0]], dtype=float).reshape((2, 2))})),
        ('One column', lambda f: assert_close(f([[1],[3]]), {'expected':np.array([[1.0], [3.0]], dtype=float).reshape((2, 1)),'residual':np.array([[0.0], [0.0]], dtype=float).reshape((2, 1))})),
        ('Sparse table', lambda f: assert_close(f([[2,0,0],[0,1,0]]), {'expected':np.array([[1.3333333333333333, 0.6666666666666666, 0.0], [0.6666666666666666, 0.3333333333333333, 0.0]], dtype=float).reshape((2, 3)),'residual':np.array([[0.6666666666666667, -0.6666666666666666, 0.0], [-0.6666666666666666, 0.6666666666666667, 0.0]], dtype=float).reshape((2, 3))})),
        ('Fractional data', lambda f: assert_close(f([[.5,.5],[1,0]]), {'expected':np.array([[0.75, 0.25], [0.75, 0.25]], dtype=float).reshape((2, 2)),'residual':np.array([[-0.25, 0.25], [0.25, -0.25]], dtype=float).reshape((2, 2))})),
        ('Reject no counts', lambda f: rejects(f,[[0,0]])),
        ('Reject negative count', lambda f: rejects(f,[[1,-1]])),
        ('Reject nonmatrix', lambda f: rejects(f,[1,2])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[3,1],[1,3]]), {'expected':np.array([[2.0, 2.0], [2.0, 2.0]], dtype=float).reshape((2, 2)),'residual':np.array([[1.0, -1.0], [-1.0, 1.0]], dtype=float).reshape((2, 2))})),
    ]
    return run_cases(namespace, 'independence_baseline', cases, mode)
