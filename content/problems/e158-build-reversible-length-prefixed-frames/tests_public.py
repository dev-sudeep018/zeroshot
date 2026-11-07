def run_tests(namespace, mode="all"):
    cases = [
        ('Encode empty and ASCII', lambda f: assert_close(f(['a','',':'],'encode'), b'1:a0:1::')),
        ('Decode embedded delimiter', lambda f: assert_close(f(b'3:a:b0:','decode'), ['a:b',''])),
        ('Decode multibyte text', lambda f: assert_close(f(b'2:\xc3\xa9','decode'), ['é'])),
        ('Encode no messages', lambda f: assert_close(f([],'encode'), b'')),
        ('Decode empty stream', lambda f: assert_close(f(b'','decode'), [])),
        ('Encode Unicode', lambda f: assert_close(f(['é'],'encode'), b'2:\xc3\xa9')),
        ('Reject truncated', lambda f: rejects(f, b'3:ab','decode')),
        ('Reject leading zero', lambda f: rejects(f, b'01:a','decode')),
        ('Reject invalid UTF-8', lambda f: rejects(f, b'1:\xff','decode')),
        ('Reject unknown mode', lambda f: rejects(f, [],'other')),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, ['a','',':'],'encode'), b'1:a0:1::'))
    ]
    return run_cases(namespace, 'text_frames', cases, mode)
