def run_tests(namespace, mode="all"):
    cases = [
        ('Resolve dot segments', lambda f: assert_close(f('a/./b/../c'), 'a/c')),
        ('Repeated separators', lambda f: assert_close(f('a//b/'), 'a/b')),
        ('Return root', lambda f: assert_close(f('a/..'), '')),
        ('Empty path', lambda f: assert_close(f(''), '')),
        ('Literal multi-dot name', lambda f: assert_close(f('.../x'), '.../x')),
        ('Unicode name', lambda f: assert_close(f('資料/part'), '資料/part')),
        ('Reject above root', lambda f: rejects(f, 'a/../../b')),
        ('Reject absolute path', lambda f: rejects(f, '/a')),
        ('Reject Windows separator', lambda f: rejects(f, 'a\\b')),
        ('Reject drive separator', lambda f: rejects(f, 'C:a')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, 'a/./b/../c'), 'a/c'))
    ]
    return run_cases(namespace, 'normalize_resource_path', cases, mode)
