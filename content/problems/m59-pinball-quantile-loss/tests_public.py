def run_tests(namespace, mode="all"):
    cases = [
        ('Median loss', lambda f: assert_close(f([0,2],[1,1],.5), {"loss":.5,"gradient":np.array([.25,-.25])})),
        ('Asymmetric penalty', lambda f: assert_close(f([3],[1],.9), {"loss":1.8,"gradient":np.array([-.9])})),
        ('Overprediction', lambda f: assert_close(f([1],[3],.9), {"loss":.2,"gradient":np.array([.1])})),
        ('Exact prediction', lambda f: assert_close(f([2],[2],.3), {"loss":0,"gradient":np.array([0.])})),
        ('Lower endpoint', lambda f: assert_close(f([0,2],[1,1],0), {"loss":.5,"gradient":np.array([.5,0])})),
        ('Upper endpoint', lambda f: assert_close(f([0,2],[1,1],1), {"loss":.5,"gradient":np.array([0.,-.5])})),
        ('Reject quantile outside interval', lambda f: rejects(f,[1],[0],1.1)),
        ('Reject lengths', lambda f: rejects(f,[1,2],[0],.5)),
        ('Reject boolean quantile', lambda f: rejects(f,[1],[0],True)),
        ('Leave input data unchanged', lambda f: assert_close(unchanged(f,np.array([0.,2]),np.array([1.,1]),.5),{"loss":.5,"gradient":np.array([.25,-.25])})),
    ]
    return run_cases(namespace, 'pinball_loss', cases, mode)
