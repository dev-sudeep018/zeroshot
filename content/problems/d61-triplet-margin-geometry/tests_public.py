def run_tests(namespace, mode="all"):
    cases = [
        ('Comfortable separation', lambda f: assert_close(f([[0]],[[1]],[[3]]),0.)),
        ('Wrong ordering', lambda f: assert_close(f([[0]],[[3]],[[1]]),9.)),
        ('Identical distances', lambda f: assert_close(f([[0]],[[1]],[[-1]],2),2.)),
        ('Zero margin', lambda f: assert_close(f([[0]],[[1]],[[1]],0),0.)),
        ('Hinge before average', lambda f: assert_close(f([[0],[0]],[[3],[1]],[[1],[3]]),4.5)),
        ('Sum feature distances', lambda f: assert_close(f([[0,0]],[[2,2]],[[1,1]]),7.)),
        ('Shared translation', lambda f: assert_close(f([[10]],[[13]],[[11]]),9.)),
        ('Reject negative margin', lambda f: rejects(f,[[0]],[[1]],[[2]],-1)),
        ('Reject broadcast positive', lambda f: rejects(f,[[0,0]],[[1]],[[2,2]])),
        ('Reject nonfinite anchor', lambda f: rejects(f,[[np.nan]],[[1]],[[2]])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[[0]],[[1]],[[3]]),0.)),
    ]
    return run_cases(namespace, 'triplet_margin', cases, mode)
