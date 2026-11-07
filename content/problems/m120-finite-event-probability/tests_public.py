def run_tests(namespace, mode="all"):
    cases = [
        ('Overlapping events', lambda f: assert_close(f([.1,.2,.3,.4],[True,True,False,False],[False,True,True,False]), {'a':0.30000000000000004,'b':0.5,'union':0.6000000000000001,'intersection':0.2,'a_given_b':0.4})),
        ('Disjoint events', lambda f: assert_close(f([.5,.5],[True,False],[False,True]), {'a':0.5,'b':0.5,'union':1.0,'intersection':0.0,'a_given_b':0.0})),
        ('Certain events', lambda f: assert_close(f([1],[True],[True]), {'a':1.0,'b':1.0,'union':1.0,'intersection':1.0,'a_given_b':1.0})),
        ('Empty A', lambda f: assert_close(f([.2,.8],[False,False],[True,True]), {'a':0.0,'b':1.0,'union':1.0,'intersection':0.0,'a_given_b':0.0})),
        ('Zero mass cell', lambda f: assert_close(f([0,1],[True,True],[False,True]), {'a':1.0,'b':1.0,'union':1.0,'intersection':1.0,'a_given_b':1.0})),
        ('A contains B', lambda f: assert_close(f([.2,.3,.5],[True,True,False],[False,True,False]), {'a':0.5,'b':0.3,'union':0.5,'intersection':0.3,'a_given_b':1.0})),
        ('Reject zero conditioning mass', lambda f: rejects(f,[0,1],[True,False],[True,False])),
        ('Reject numeric mask', lambda f: rejects(f,[1],[1],[True])),
        ('Reject invalid masses', lambda f: rejects(f,[.2,.2],[True,False],[True,True])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[.1,.2,.3,.4],[True,True,False,False],[False,True,True,False]), {'a':0.30000000000000004,'b':0.5,'union':0.6000000000000001,'intersection':0.2,'a_given_b':0.4})),
    ]
    return run_cases(namespace, 'event_probabilities', cases, mode)
