def run_tests(namespace, mode="all"):
    cases = [
        ('Indifferent discriminator', lambda f: assert_close(f([0],[0]),{"discriminator":2*np.log(2),"generator":np.log(2)})),
        ('Confident correct discriminator', lambda f: assert_close(f([1000],[-1000]),{"discriminator":0.,"generator":1000.})),
        ('Confident wrong discriminator', lambda f: assert_close(f([-1000],[1000]),{"discriminator":2000.,"generator":0.})),
        ('Fake confidence rises', lambda f: assert_close(f([0],[np.log(3)]),{"discriminator":np.log(2)+np.log(4),"generator":np.log(4/3)})),
        ('Unequal population sizes', lambda f: assert_close(f([0,0,0],[0]),{"discriminator":2*np.log(2),"generator":np.log(2)})),
        ('Real scores affect discriminator only', lambda f: assert_close(f([np.log(3)],[0]),{"discriminator":np.log(4/3)+np.log(2),"generator":np.log(2)})),
        ('Opposite fake scores average', lambda f: assert_close(f([0],[-1000,1000]),{"discriminator":np.log(2)+500,"generator":500.})),
        ('Reject empty real data', lambda f: rejects(f,[],[0])),
        ('Reject matrix logits', lambda f: rejects(f,[[0]],[0])),
        ('Reject nonfinite fake data', lambda f: rejects(f,[0],[np.nan])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,[0],[0]),{"discriminator":2*np.log(2),"generator":np.log(2)})),
    ]
    return run_cases(namespace, 'adversarial_losses', cases, mode)
