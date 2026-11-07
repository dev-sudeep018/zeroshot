def run_tests(namespace, mode="all"):
    cases = [
        ('Perfect separation', lambda f: assert_close(f([0,1,2,3],[0,0,1,1]), {"threshold":1.5,"impurity":0,"gain":.5,"left_class":0,"right_class":1})),
        ('Tie chooses first gap', lambda f: assert_close(f([0,1,2],[0,1,0]), {"threshold":.5,"impurity":1/3,"gain":1/9,"left_class":0,"right_class":0})),
        ('Pure parent', lambda f: assert_close(f([0,2,4],[1,1,1]), {"threshold":1,"impurity":0,"gain":0,"left_class":1,"right_class":1})),
        ('Repeated values', lambda f: assert_close(f([0,0,2,2],[0,0,1,1]), {"threshold":1,"impurity":0,"gain":.5,"left_class":0,"right_class":1})),
        ('Unsorted rows', lambda f: assert_close(f([3,0,2,1],[1,0,1,0]), {"threshold":1.5,"impurity":0,"gain":.5,"left_class":0,"right_class":1})),
        ('Two observations', lambda f: assert_close(f([-4,2],[1,0]), {"threshold":-1,"impurity":0,"gain":.5,"left_class":1,"right_class":0})),
        ('Reject constant feature', lambda f: rejects(f,[1,1],[0,1])),
        ('Reject nonbinary label', lambda f: rejects(f,[0,1],[0,2])),
        ('Reject lengths', lambda f: rejects(f,[0,1],[0])),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([3.,0,2,1]),np.array([1.,0,1,0])),{"threshold":1.5,"impurity":0,"gain":.5,"left_class":0,"right_class":1})),
        ('Adjacent floating-point values still split', lambda f: assert_close(f([np.nextafter(1.,2.),np.nextafter(np.nextafter(1.,2.),2.)],[0,1]),{"threshold":np.nextafter(1.,2.),"impurity":0,"gain":.5,"left_class":0,"right_class":1})),
    ]
    return run_cases(namespace, 'gini_split', cases, mode)
