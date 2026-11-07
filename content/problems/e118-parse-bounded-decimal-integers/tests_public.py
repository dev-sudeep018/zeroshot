def run_tests(namespace, mode="all"):
    cases = [
        ('Signed values', lambda f: assert_close(f([' -2 ','+3','0'], -3, 3), [-2,3,0])),
        ('Leading zeros', lambda f: assert_close(f(['0007','-00'], -10, 10), [7,0])),
        ('Inclusive bounds', lambda f: assert_close(f(['-5','5'], -5, 5), [-5,5])),
        ('Empty input', lambda f: assert_close(f([], 0, 1), [])),
        ('Single bound', lambda f: assert_close(f(['2'], 2, 2), [2])),
        ('Long zero prefix', lambda f: assert_close(f(['0'*5000+'1'], 0, 2), [1])),
        ('Reject floating string', lambda f: rejects(f, ['1.0'], 0, 2)),
        ('Reject underscore syntax', lambda f: rejects(f, ['1_0'], 0, 20)),
        ('Reject outside range', lambda f: rejects(f, ['3'], 0, 2)),
        ('Reject Unicode digit', lambda f: rejects(f, ['١'], 0, 2)),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [' -2 ','+3','0'], -3, 3), [-2,3,0]))
    ]
    return run_cases(namespace, 'parse_decimal_values', cases, mode)
