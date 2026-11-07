def run_tests(namespace, mode="all"):
    cases = [
        ('Whitespace and duplicates', lambda f: assert_close(f([' AI ','ai','Data']), ['ai','data'])),
        ('Blank tags', lambda f: assert_close(f([' ', '', 'ML']), ['ml'])),
        ('Order matters', lambda f: assert_close(f(['Z','A','z']), ['z','a'])),
        ('Empty collection', lambda f: assert_close(f([]), [])),
        ('Internal spacing', lambda f: assert_close(f(['A B','a  b']), ['a b','a  b'])),
        ('Unicode case', lambda f: assert_close(f(['CAFÉ','café']), ['café'])),
        ('Reject raw string', lambda f: rejects(f, 'AI')),
        ('Reject nonstring tag', lambda f: rejects(f, [3])),
        ('Reject overlong tag', lambda f: rejects(f, ['x'*10001])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [' AI ','ai','Data']), ['ai','data']))
    ]
    return run_cases(namespace, 'clean_tags', cases, mode)
