def run_tests(namespace, mode="all"):
    cases = [
        ('Shared kernel', lambda f: assert_close(f(3,4,[3,3],1,[2,2],1), dict(weights=108,biases=4,parameters=112,macs=432))),
        ('Depthwise channels', lambda f: assert_close(f(4,4,[3,3],4,[2,3],0), dict(weights=36,biases=0,parameters=36,macs=216))),
        ('Grouped pointwise', lambda f: assert_close(f(4,6,[1,1],2,[5,5],1), dict(weights=12,biases=6,parameters=18,macs=300))),
        ('Single pixel', lambda f: assert_close(f(1,1,[1,1],1,[1,1],0), dict(weights=1,biases=0,parameters=1,macs=1))),
        ('Rectangular kernel', lambda f: assert_close(f(2,2,[2,3],1,[1,2],1), dict(weights=24,biases=2,parameters=26,macs=48))),
        ('Channel multiplier', lambda f: assert_close(f(2,4,[2,2],2,[3,1],1), dict(weights=16,biases=4,parameters=20,macs=48))),
        ('Reject indivisible groups', lambda f: rejects(f, 3,4,[3,3],2,[2,2],1)),
        ('Reject three spatial axes', lambda f: rejects(f, 2,2,[1,2,3],1,[2,2],1)),
        ('Reject boolean flag', lambda f: rejects(f, 2,2,[1,1],1,[2,2],True)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, 3,4,[3,3],1,[2,2],1), dict(weights=108,biases=4,parameters=112,macs=432))),
    ]
    return run_cases(namespace, 'convolution_budget', cases, mode)
