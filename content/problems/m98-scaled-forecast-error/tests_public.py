def run_tests(namespace, mode="all"):
    cases = [
        ('Trend baseline', lambda f: assert_close(f([1,2,3,4],[5,6],[4,8],1), {'scale':1.0,'mae':1.5,'mase':1.5})),
        ('Seasonal baseline', lambda f: assert_close(f([1,3,2,5],[3,6],[2,8],2), {'scale':1.5,'mae':1.5,'mase':1.0})),
        ('Perfect constant', lambda f: assert_close(f([4,4,4],[4],[4],1), {'scale':0.0,'mae':0.0,'mase':0.0})),
        ('Perfect nonconstant', lambda f: assert_close(f([1,3],[2],[2],1), {'scale':2.0,'mae':0.0,'mase':0.0})),
        ('Long lag', lambda f: assert_close(f([1,2,5,8],[9],[10],3), {'scale':7.0,'mae':1.0,'mase':0.14285714285714285})),
        ('Scaled units', lambda f: assert_close(f([10,20,30],[40],[50],1), {'scale':10.0,'mae':10.0,'mase':1.0})),
        ('Reject zero-scale error', lambda f: rejects(f,[2,2],[2],[3],1)),
        ('Reject too-large lag', lambda f: rejects(f,[1,2],[3],[3],2)),
        ('Reject mismatched evaluation', lambda f: rejects(f,[1,2],[1,2],[1],1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,2,3,4],[5,6],[4,8],1), {'scale':1.0,'mae':1.5,'mase':1.5})),
    ]
    return run_cases(namespace, 'scaled_forecast_error', cases, mode)
