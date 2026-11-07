def run_tests(namespace, mode="all"):
    cases = [
        ('One inactive neuron', lambda f: assert_close(f([[1,-1,0],[3,-2,2]]), dict(active_fraction=np.array([1,0,0.5]),mean_output=np.array([2,0,1]),inactive=np.array([False,True,False])))),
        ('Exact zeros', lambda f: assert_close(f([[0,0]]), dict(active_fraction=np.zeros(2),mean_output=np.zeros(2),inactive=np.ones(2,dtype=bool)))),
        ('Mixed signs', lambda f: assert_close(f([[-1],[1],[-2],[3]]), dict(active_fraction=np.array([0.5]),mean_output=np.array([1]),inactive=np.array([False])))),
        ('Positive row', lambda f: assert_close(f([[2,4]]), dict(active_fraction=np.ones(2),mean_output=np.array([2,4]),inactive=np.zeros(2,dtype=bool)))),
        ('All negative', lambda f: assert_close(f([[-1],[-5]]), dict(active_fraction=np.array([0]),mean_output=np.array([0]),inactive=np.array([True])))),
        ('Rare high response', lambda f: assert_close(f([[0],[0],[12]]), dict(active_fraction=np.array([1/3]),mean_output=np.array([4]),inactive=np.array([False])))),
        ('Reject vector input', lambda f: rejects(f, [1,2])),
        ('Reject nonfinite input', lambda f: rejects(f, [[np.inf]])),
        ('Reject empty batch', lambda f: rejects(f, np.empty((0,2)))),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[1,-1,0],[3,-2,2]]), dict(active_fraction=np.array([1,0,0.5]),mean_output=np.array([2,0,1]),inactive=np.array([False,True,False])))),
    ]
    return run_cases(namespace, 'relu_activity', cases, mode)
