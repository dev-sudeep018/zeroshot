def run_tests(namespace, mode="all"):
    cases = [
        ('Rectangle', lambda f: assert_close(f([[0,0],[4,0],[4,3],[0,3]]), {'perimeter':14.0,'signed_area':12.0})),
        ('Clockwise triangle', lambda f: assert_close(f([[0,0],[0,3],[4,0]]), {'perimeter':12.0,'signed_area':-6.0})),
        ('Collinear vertices', lambda f: assert_close(f([[0,0],[1,0],[3,0]]), {'perimeter':6.0,'signed_area':0.0})),
        ('Repeated closing point', lambda f: assert_close(f([[0,0],[2,0],[0,2],[0,0]]), {'perimeter':6.82842712474619,'signed_area':2.0})),
        ('Translated square', lambda f: assert_close(f([[2,3],[3,3],[3,4],[2,4]]), {'perimeter':4.0,'signed_area':1.0})),
        ('Crossed polygon', lambda f: assert_close(f([[0,0],[2,2],[0,2],[2,0]]), {'perimeter':9.65685424949238,'signed_area':0.0})),
        ('Reject too few vertices', lambda f: rejects(f,[[0,0],[1,1]])),
        ('Reject 3D coordinates', lambda f: rejects(f,[[0,0,0],[1,0,0],[0,1,0]])),
        ('Reject nonfinite', lambda f: rejects(f,[[0,0],[1,np.inf],[0,1]])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[0,0],[4,0],[4,3],[0,3]]), {'perimeter':14.0,'signed_area':12.0})),
    ]
    return run_cases(namespace, 'polygon_measurements', cases, mode)
