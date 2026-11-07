def run_tests(namespace, mode="all"):
    cases = [
        ('Include separator cost', lambda f: assert_close(f(['ab','cd','e'],5,'|'), dict(kept=['ab','cd'],used_bytes=5,remaining_bytes=0))),
        ('UTF-8 bytes', lambda f: assert_close(f(['é','🙂','x'],6,''), dict(kept=['é','🙂'],used_bytes=6,remaining_bytes=0))),
        ('Do not skip long message', lambda f: assert_close(f(['long','x'],1,''), dict(kept=[],used_bytes=0,remaining_bytes=1))),
        ('Empty message prefix', lambda f: assert_close(f(['',''],0,''), dict(kept=['',''],used_bytes=0,remaining_bytes=0))),
        ('Empty collection', lambda f: assert_close(f([],3,'|'), dict(kept=[],used_bytes=0,remaining_bytes=3))),
        ('Separator after empty message', lambda f: assert_close(f(['','a'],1,'|'), dict(kept=[''],used_bytes=0,remaining_bytes=1))),
        ('Reject negative budget', lambda f: rejects(f, [],-1,'')),
        ('Reject nonstring separator', lambda f: rejects(f, [],5,None)),
        ('Reject nontext message', lambda f: rejects(f, [1],5,'')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['ab','cd','e'],5,'|'), dict(kept=['ab','cd'],used_bytes=5,remaining_bytes=0)))
    ]
    return run_cases(namespace, 'budget_messages', cases, mode)
