def run_tests(namespace, mode="all"):
    cases = [
        ('Unique corpus coverage', lambda f: assert_close(f([['a','a'],['b','x']], ['a','b','c']), dict(retrieved_corpus_ids=['a','b'],out_of_corpus_ids=['x'],coverage=2/3))),
        ('Empty corpus', lambda f: assert_close(f([['x']], []), dict(retrieved_corpus_ids=[],out_of_corpus_ids=['x'],coverage=0.0))),
        ('No rankings', lambda f: assert_close(f([], ['a']), dict(retrieved_corpus_ids=[],out_of_corpus_ids=[],coverage=0.0))),
        ('Full coverage', lambda f: assert_close(f([['b','a']], ['a','b']), dict(retrieved_corpus_ids=['a','b'],out_of_corpus_ids=[],coverage=1.0))),
        ('Out-of-corpus dedup', lambda f: assert_close(f([['z'],['z','x']], []), dict(retrieved_corpus_ids=[],out_of_corpus_ids=['x','z'],coverage=0.0))),
        ('Empty queries', lambda f: assert_close(f([[],[]], ['a']), dict(retrieved_corpus_ids=[],out_of_corpus_ids=[],coverage=0.0))),
        ('Reject duplicate corpus', lambda f: rejects(f, [], ['a','a'])),
        ('Reject raw ranking', lambda f: rejects(f, ['abc'], [])),
        ('Reject empty retrieved ID', lambda f: rejects(f, [['']], [])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [['a','a'],['b','x']], ['a','b','c']), dict(retrieved_corpus_ids=['a','b'],out_of_corpus_ids=['x'],coverage=2/3)))
    ]
    return run_cases(namespace, 'ranking_coverage', cases, mode)
