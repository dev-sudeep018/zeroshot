def run_tests(namespace, mode="all"):
    cases = [
        ('Interior rectangle', lambda f: assert_close(f(np.arange(9).reshape(3,3),[1,1,3,3],-1), {'image':np.array([[0.0, 1.0, 2.0], [3.0, -1.0, -1.0], [6.0, -1.0, -1.0]], dtype='float64'),'mask':np.array([[False, False, False], [False, True, True], [False, True, True]], dtype='bool')})),
        ('Clip negative origin', lambda f: assert_close(f(np.ones((3,3)),[-2,-1,2,2],0), {'image':np.array([[0.0, 0.0, 1.0], [0.0, 0.0, 1.0], [1.0, 1.0, 1.0]], dtype='float64'),'mask':np.array([[True, True, False], [True, True, False], [False, False, False]], dtype='bool')})),
        ('Fully outside', lambda f: assert_close(f(np.ones((2,2)),[3,3,4,4],0), {'image':np.array([[1.0, 1.0], [1.0, 1.0]], dtype='float64'),'mask':np.array([[False, False], [False, False]], dtype='bool')})),
        ('Empty width', lambda f: assert_close(f(np.ones((2,2)),[0,1,2,1],7), {'image':np.array([[1.0, 1.0], [1.0, 1.0]], dtype='float64'),'mask':np.array([[False, False], [False, False]], dtype='bool')})),
        ('Erase whole image', lambda f: assert_close(f([[1,2],[3,4]],[0,0,2,2],0), {'image':np.array([[0.0, 0.0], [0.0, 0.0]], dtype='float64'),'mask':np.array([[True, True], [True, True]], dtype='bool')})),
        ('Single pixel', lambda f: assert_close(f([[2]],[0,0,1,1],-3), {'image':np.array([[-3.0]], dtype='float64'),'mask':np.array([[True]], dtype='bool')})),
        ('Reject reversed rectangle', lambda f: rejects(f, [[1]],[1,0,0,1],0)),
        ('Reject fractional coordinate', lambda f: rejects(f, [[1]],[0,0,1,0.5],0)),
        ('Reject wrong rectangle length', lambda f: rejects(f, [[1]],[0,0,1],0)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, np.arange(9).reshape(3,3),[1,1,3,3],-1), {'image':np.array([[0.0, 1.0, 2.0], [3.0, -1.0, -1.0], [6.0, -1.0, -1.0]], dtype='float64'),'mask':np.array([[False, False, False], [False, True, True], [False, True, True]], dtype='bool')})),
    ]
    return run_cases(namespace, 'erase_rectangle', cases, mode)
