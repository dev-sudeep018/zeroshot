def run_tests(namespace, mode="all"):
    cases = [
        ('Three independent fair events', lambda f: assert_close(f(.5,.5,.5,.25,.25,.25,.125), {'union':0.875,'exactly_one':0.375,'exactly_two':0.375,'all_three':0.125,'none':0.125})),
        ('Disjoint events', lambda f: assert_close(f(.2,.3,.1,0,0,0,0), {'union':0.6,'exactly_one':0.6,'exactly_two':0.0,'all_three':0.0,'none':0.4})),
        ('Identical events', lambda f: assert_close(f(.4,.4,.4,.4,.4,.4,.4), {'union':0.4,'exactly_one':0.0,'exactly_two':0.0,'all_three':0.4,'none':0.6})),
        ('No events', lambda f: assert_close(f(0,0,0,0,0,0,0), {'union':0.0,'exactly_one':0.0,'exactly_two':0.0,'all_three':0.0,'none':1.0})),
        ('All certain', lambda f: assert_close(f(1,1,1,1,1,1,1), {'union':1.0,'exactly_one':0.0,'exactly_two':0.0,'all_three':1.0,'none':0.0})),
        ('Two overlapping only', lambda f: assert_close(f(.6,.5,0,.2,0,0,0), {'union':0.8999999999999999,'exactly_one':0.7,'exactly_two':0.2,'all_three':0.0,'none':0.10000000000000003})),
        ('Reject impossible overlap', lambda f: rejects(f,.1,.1,.1,.5,0,0,0)),
        ('Reject excessive disjoint total', lambda f: rejects(f,.5,.5,.5,0,0,0,0)),
        ('Reject triple above pair', lambda f: rejects(f,.5,.5,.5,.1,.1,.1,.2)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,.5,.5,.5,.25,.25,.25,.125), {'union':0.875,'exactly_one':0.375,'exactly_two':0.375,'all_three':0.125,'none':0.125})),
    ]
    return run_cases(namespace, 'three_event_regions', cases, mode)
