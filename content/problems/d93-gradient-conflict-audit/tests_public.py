def run_tests(namespace, mode="all"):
    cases = [
        ('Opposing tasks', lambda f: assert_close(f([[1,0],[-1,0],[0,1]]), {'cosine':np.array([[1.0, -1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]], dtype='float64'),'conflict':np.array([[False, True, False], [True, False, False], [False, False, False]], dtype='bool')})),
        ('Zero task', lambda f: assert_close(f([[0,0],[2,1]]), {'cosine':np.array([[0.0, 0.0], [0.0, 0.9999999999999999]], dtype='float64'),'conflict':np.array([[False, False], [False, False]], dtype='bool')})),
        ('Same direction', lambda f: assert_close(f([[1,2],[2,4]]), {'cosine':np.array([[0.9999999999999999, 0.9999999999999999], [0.9999999999999999, 0.9999999999999999]], dtype='float64'),'conflict':np.array([[False, False], [False, False]], dtype='bool')})),
        ('Single task', lambda f: assert_close(f([[3,4]]), {'cosine':np.array([[1.0]], dtype='float64'),'conflict':np.array([[False]], dtype='bool')})),
        ('All zero', lambda f: assert_close(f([[0],[0]]), {'cosine':np.array([[0.0, 0.0], [0.0, 0.0]], dtype='float64'),'conflict':np.array([[False, False], [False, False]], dtype='bool')})),
        ('Mixed directions', lambda f: assert_close(f([[1,1],[1,-1],[-2,-1]]), {'cosine':np.array([[0.9999999999999998, 0.0, -0.9486832980505137], [0.0, 0.9999999999999998, -0.3162277660168379], [-0.9486832980505137, -0.3162277660168379, 0.9999999999999999]], dtype='float64'),'conflict':np.array([[False, False, True], [False, False, True], [True, True, False]], dtype='bool')})),
        ('Numerical zero band', lambda f: assert_close(f([[1,0],[-1e-13,1],[-1e-8,1]]), {'cosine':np.array([[1,0,-1e-8],[0,1,1],[-1e-8,1,1.0]]),'conflict':np.array([[False,False,True],[False,False,False],[True,False,False]])})),
        ('Tiny nonzero gradients', lambda f: assert_close(f([[1e-200,0],[-1e-200,0]]), {'cosine':np.array([[1.,-1.],[-1.,1.]]),'conflict':np.array([[False,True],[True,False]])})),
        ('Reject vector input', lambda f: rejects(f, [1,2])),
        ('Reject empty task', lambda f: rejects(f, np.empty((0,2)))),
        ('Reject nonfinite value', lambda f: rejects(f, [[np.nan]])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[1,0],[-1,0],[0,1]]), {'cosine':np.array([[1.0, -1.0, 0.0], [-1.0, 1.0, 0.0], [0.0, 0.0, 1.0]], dtype='float64'),'conflict':np.array([[False, True, False], [True, False, False], [False, False, False]], dtype='bool')})),
    ]
    return run_cases(namespace, 'gradient_conflicts', cases, mode)
