def run_tests(namespace, mode="all"):
    cases = [
        ('Numeric rather than text', lambda f: assert_close(f('1.10.0', '1.2.9'), 1)),
        ('Equivalent leading zeros', lambda f: assert_close(f('01.2.003', '1.2.3'), 0)),
        ('Major component wins', lambda f: assert_close(f('2.0.0', '1.99.99'), 1)),
        ('Patch comparison', lambda f: assert_close(f('1.0.1', '1.0.2'), -1)),
        ('Whitespace trim', lambda f: assert_close(f(' 0.0.0 ', '0.0.0'), 0)),
        ('Minor comparison', lambda f: assert_close(f('1.0.9', '1.1.0'), -1)),
        ('Reject missing component', lambda f: rejects(f, '1.2', '1.2.0')),
        ('Reject prerelease suffix', lambda f: rejects(f, '1.0.0-rc1', '1.0.0')),
        ('Reject negative component', lambda f: rejects(f, '1.-1.0', '1.0.0')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, '1.10.0', '1.2.9'), 1))
    ]
    return run_cases(namespace, 'compare_versions', cases, mode)
