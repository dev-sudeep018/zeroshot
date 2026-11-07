def run_tests(namespace, mode="all"):
    cases = [
        ('Punctuation boundaries', lambda f: assert_close(f('Hi, ML!'), [['Hi',0,2],['ML',4,6]])),
        ('Non-ASCII separator', lambda f: assert_close(f('éAI café'), [['AI',1,3],['caf',4,7]])),
        ('Numbers separate', lambda f: assert_close(f('r2d2'), [['r',0,1],['d',2,3]])),
        ('Empty text', lambda f: assert_close(f(''), [])),
        ('No words', lambda f: assert_close(f('123_!'), [])),
        ('Emoji offset', lambda f: assert_close(f('🙂go'), [['go',1,3]])),
        ('Reject nonstring', lambda f: rejects(f, [])),
        ('Reject oversized', lambda f: rejects(f, 'a'*10001)),
        ('Reject surrogate', lambda f: rejects(f, '\ud800')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, 'Hi, ML!'), [['Hi',0,2],['ML',4,6]]))
    ]
    return run_cases(namespace, 'word_spans', cases, mode)
