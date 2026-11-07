def run_tests(namespace, mode="all"):
    cases = [
        ('Correlated missingness', lambda f: assert_close(f(np.array([[True,True],[False,False]])), dict(feature_rates=np.array([.5,.5]),row_counts=np.array([2,0]),co_missing=np.full((2,2),.5)))),
        ('Disjoint missingness', lambda f: assert_close(f(np.array([[True,False],[False,True]])), dict(feature_rates=np.array([.5,.5]),row_counts=np.array([1,1]),co_missing=np.eye(2)*.5))),
        ('No missing values', lambda f: assert_close(f(np.zeros((2,2),dtype=bool)), dict(feature_rates=np.zeros(2),row_counts=np.zeros(2,dtype=int),co_missing=np.zeros((2,2))))),
        ('All missing values', lambda f: assert_close(f(np.ones((1,2),dtype=bool)), dict(feature_rates=np.ones(2),row_counts=np.array([2]),co_missing=np.ones((2,2))))),
        ('One feature', lambda f: assert_close(f(np.array([[True],[False],[False]])), dict(feature_rates=np.array([1/3]),row_counts=np.array([1,0,0]),co_missing=np.array([[1/3]])))),
        ('Unequal rates', lambda f: assert_close(f(np.array([[True,True],[True,False]])), dict(feature_rates=np.array([1.,.5]),row_counts=np.array([2,1]),co_missing=np.array([[1.,.5],[.5,.5]])))),
        ('Reject numeric mask', lambda f: rejects(f, np.array([[0,1]]))),
        ('Reject vector mask', lambda f: rejects(f, np.array([True]))),
        ('Reject empty matrix', lambda f: rejects(f, np.zeros((0,2),dtype=bool))),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, np.array([[True,True],[False,False]])), dict(feature_rates=np.array([.5,.5]),row_counts=np.array([2,0]),co_missing=np.full((2,2),.5))))
    ]
    return run_cases(namespace, 'missingness_audit', cases, mode)
