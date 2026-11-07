def run_tests(namespace, mode="all"):
    cases = [
        ('Requested order', lambda f: assert_close(f([{'id':'a'},{'id':'b'}], ['b','a']), dict(records=[{'id':'b'},{'id':'a'}],missing_positions=[]))),
        ('Missing alignment', lambda f: assert_close(f([{'id':'a'}], ['z','a']), dict(records=[None,{'id':'a'}],missing_positions=[0]))),
        ('Repeated request', lambda f: assert_close(f([{'id':'a'}], ['a','a']), dict(records=[{'id':'a'},{'id':'a'}],missing_positions=[]))),
        ('No requests', lambda f: assert_close(f([{'id':'a'}], []), dict(records=[],missing_positions=[]))),
        ('No records', lambda f: assert_close(f([], ['a','b']), dict(records=[None,None],missing_positions=[0,1]))),
        ('Both empty', lambda f: assert_close(f([], []), dict(records=[],missing_positions=[]))),
        ('Reject duplicate records', lambda f: rejects(f, [{'id':'a'},{'id':'a'}], [])),
        ('Reject missing record ID', lambda f: rejects(f, [{}], [])),
        ('Reject invalid request ID', lambda f: rejects(f, [], [''])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{'id':'a'},{'id':'b'}], ['b','a']), dict(records=[{'id':'b'},{'id':'a'}],missing_positions=[])))
    ]
    return run_cases(namespace, 'resolve_ids', cases, mode)
