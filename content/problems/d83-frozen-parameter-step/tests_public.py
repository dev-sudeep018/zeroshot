def run_tests(namespace, mode="all"):
    cases = [
        ('One frozen coordinate', lambda f: assert_close(f([1,2],[2,4],[1,0],0.5), dict(weights=np.array([0,2]),delta=np.array([-1,0])))),
        ('Both trainable', lambda f: assert_close(f([2,-2],[1,-3],[1,1],0.1), dict(weights=np.array([1.9,-1.7]),delta=np.array([-0.1,0.3])))),
        ('Both frozen', lambda f: assert_close(f([1,2],[10,20],[0,0],1), dict(weights=np.array([1,2]),delta=np.zeros(2)))),
        ('Zero rate', lambda f: assert_close(f([1],[3],[1],0), dict(weights=np.array([1]),delta=np.array([0])))),
        ('Zero gradient', lambda f: assert_close(f([3],[0],[1],0.5), dict(weights=np.array([3]),delta=np.array([0])))),
        ('Negative gradients', lambda f: assert_close(f([0,0],[-2,-4],[1,0],0.25), dict(weights=np.array([0.5,0]),delta=np.array([0.5,0])))),
        ('Reject nonbinary mask', lambda f: rejects(f, [1],[2],[0.5],0.1)),
        ('Reject shape mismatch', lambda f: rejects(f, [1,2],[2],[1,1],0.1)),
        ('Reject negative rate', lambda f: rejects(f, [1],[2],[1],-1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [1,2],[2,4],[1,0],0.5), dict(weights=np.array([0,2]),delta=np.array([-1,0])))),
    ]
    return run_cases(namespace, 'frozen_sgd', cases, mode)
