def run_tests(namespace, mode="all"):
    cases = [
        ('Whole tokens', lambda f: assert_close(f('AI helps AI.', {'AI':'artificial intelligence'}), 'artificial intelligence helps AI.')),
        ('Case-sensitive', lambda f: assert_close(f('ML ml', {'ML':'model'}), 'model ml')),
        ('Whitespace normalized', lambda f: assert_close(f(' x\ty ', {'x':'a'}), 'a y')),
        ('Empty text', lambda f: assert_close(f('', {}), '')),
        ('No substring replacement', lambda f: assert_close(f('cat cats', {'cat':'dog'}), 'dog cats')),
        ('Empty replacement slot', lambda f: assert_close(f('a b', {'a':''}), ' b')),
        ('Reject nontext input', lambda f: rejects(f, 1, {})),
        ('Reject nontext replacement', lambda f: rejects(f, 'a', {'a':1})),
        ('Reject empty glossary key', lambda f: rejects(f, 'a', {'':'b'})),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, 'AI helps AI.', {'AI':'artificial intelligence'}), 'artificial intelligence helps AI.'))
    ]
    return run_cases(namespace, 'replace_tokens', cases, mode)
