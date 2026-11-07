def run_tests(namespace, mode="all"):
    cases = [
        ('Stable rule order', lambda f: assert_close(f([{}, {'x':3},{'x':1}], [['present','required','x'],['bounded','range','x',0,2]]), [['present','bounded'],['bounded'],[]])),
        ('False present but not numeric', lambda f: assert_close(f([{'x':False}], [['p','required','x'],['r','range','x',0,1]]), [['r']])),
        ('Inclusive limits', lambda f: assert_close(f([{'x':0},{'x':2}], [['r','range','x',0,2]]), [[],[]])),
        ('No rules', lambda f: assert_close(f([{},{}], []), [[],[]])),
        ('No records', lambda f: assert_close(f([], [['r','required','x']]), [])),
        ('Blank string counts present', lambda f: assert_close(f([{'x':''}], [['r','required','x']]), [[]])),
        ('Reject duplicate rule name', lambda f: rejects(f, [], [['r','required','x'],['r','required','y']])),
        ('Reject reversed range', lambda f: rejects(f, [], [['r','range','x',2,1]])),
        ('Reject unknown rule', lambda f: rejects(f, [], [['r','mystery','x']])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [{}, {'x':3},{'x':1}], [['present','required','x'],['bounded','range','x',0,2]]), [['present','bounded'],['bounded'],[]]))
    ]
    return run_cases(namespace, 'quality_violations', cases, mode)
