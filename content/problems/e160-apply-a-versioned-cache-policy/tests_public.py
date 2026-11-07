def run_tests(namespace, mode="all"):
    cases = [
        ('Fresh matching value', lambda f: assert_close(f({'x':{'timestamp':8,'version':'v1','value':[1]}},10,'v1',3), {'x':[1]})),
        ('Expiry boundary excluded', lambda f: assert_close(f({'x':{'timestamp':7,'version':'v1','value':1}},10,'v1',3), {})),
        ('Future entry excluded', lambda f: assert_close(f({'x':{'timestamp':11,'version':'v1','value':1}},10,'v1',3), {})),
        ('Version mismatch', lambda f: assert_close(f({'x':{'timestamp':10,'version':'v2','value':1}},10,'v1',3), {})),
        ('No entries', lambda f: assert_close(f({},10,'v1',3), {})),
        ('Zero TTL', lambda f: assert_close(f({'x':{'timestamp':10,'version':'v1','value':1}},10,'v1',0), {})),
        ('Reject missing timestamp', lambda f: rejects(f, {'x':{'version':'v1','value':1}},10,'v1',3)),
        ('Reject negative TTL', lambda f: rejects(f, {},10,'v1',-1)),
        ('Reject bool timestamp', lambda f: rejects(f, {'x':{'timestamp':True,'version':'v1','value':1}},10,'v1',3)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, {'x':{'timestamp':8,'version':'v1','value':[1]}},10,'v1',3), {'x':[1]}))
    ]
    return run_cases(namespace, 'valid_cache_entries', cases, mode)
