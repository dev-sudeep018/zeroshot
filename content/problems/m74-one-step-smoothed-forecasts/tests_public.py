def run_tests(namespace, mode="all"):
    cases = [
        ('Partial updates', lambda f: assert_close(f([4,8,2],.5,0), {'forecast':np.array([0.0, 2.0, 5.0], dtype=float).reshape((3,)),'level':3.5})),
        ('No updating', lambda f: assert_close(f([4,8],0,3), {'forecast':np.array([3.0, 3.0], dtype=float).reshape((2,)),'level':3.0})),
        ('Last-observation forecast', lambda f: assert_close(f([4,8,2],1,0), {'forecast':np.array([0.0, 4.0, 8.0], dtype=float).reshape((3,)),'level':2.0})),
        ('Single observation', lambda f: assert_close(f([5],.2,1), {'forecast':np.array([1.0], dtype=float).reshape((1,)),'level':1.8})),
        ('Constant start', lambda f: assert_close(f([3,3,3],.7,3), {'forecast':np.array([3.0, 3.0, 3.0], dtype=float).reshape((3,)),'level':3.0})),
        ('Negative levels', lambda f: assert_close(f([-4,2],.5,-2), {'forecast':np.array([-2.0, -3.0], dtype=float).reshape((2,)),'level':-0.5})),
        ('Reject alpha above one', lambda f: rejects(f,[1],1.1,0)),
        ('Reject boolean alpha', lambda f: rejects(f,[1],True,0)),
        ('Reject nonfinite initial', lambda f: rejects(f,[1],.5,np.inf)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[4,8,2],.5,0), {'forecast':np.array([0.0, 2.0, 5.0], dtype=float).reshape((3,)),'level':3.5})),
    ]
    return run_cases(namespace, 'smoothed_forecasts', cases, mode)
