def run_tests(namespace, mode="all"):
    cases = [
        ('Mixed sentence endings', lambda f: assert_close(f('Hello! Ready? Go.'), ['Hello!','Ready?','Go.'])),
        ('Punctuation runs', lambda f: assert_close(f('Wait... really?! yes'), ['Wait...','really?!','yes'])),
        ('Closing bracket retained', lambda f: assert_close(f('A!) B.'), ['A!)','B.'])),
        ('Whitespace only', lambda f: assert_close(f(' \n '), [])),
        ('No delimiter', lambda f: assert_close(f(' final fragment '), ['final fragment'])),
        ('No space required', lambda f: assert_close(f('a.b'), ['a.','b'])),
        ('Reject nontext', lambda f: rejects(f, None)),
        ('Reject oversized', lambda f: rejects(f, 'a'*10001)),
        ('Reject surrogate', lambda f: rejects(f, '\ud800')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, 'Hello! Ready? Go.'), ['Hello!','Ready?','Go.']))
    ]
    return run_cases(namespace, 'split_sentences', cases, mode)
