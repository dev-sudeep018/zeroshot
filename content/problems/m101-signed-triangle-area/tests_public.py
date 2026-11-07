def run_tests(namespace, mode="all"):
    cases = [
        ('Counterclockwise', lambda f: assert_close(f([0,0],[4,0],[0,3]), {'signed_area':6.0,'orientation':1})),
        ('Clockwise', lambda f: assert_close(f([0,0],[0,3],[4,0]), {'signed_area':-6.0,'orientation':-1})),
        ('Collinear', lambda f: assert_close(f([0,0],[1,1],[2,2]), {'signed_area':0.0,'orientation':0})),
        ('Translated triangle', lambda f: assert_close(f([2,1],[5,1],[2,3]), {'signed_area':3.0,'orientation':1})),
        ('Repeated point', lambda f: assert_close(f([1,2],[1,2],[4,5]), {'signed_area':0.0,'orientation':0})),
        ('Negative coordinates', lambda f: assert_close(f([-2,-1],[1,-1],[-2,1]), {'signed_area':3.0,'orientation':1})),
        ('Reject wrong shape', lambda f: rejects(f,[0],[1,2],[3,4])),
        ('Reject matrix point', lambda f: rejects(f,[[0,0]],[1,2],[3,4])),
        ('Reject nonfinite', lambda f: rejects(f,[np.inf,0],[1,2],[3,4])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[0,0],[4,0],[0,3]), {'signed_area':6.0,'orientation':1})),
    ]
    return run_cases(namespace, 'triangle_orientation', cases, mode)
