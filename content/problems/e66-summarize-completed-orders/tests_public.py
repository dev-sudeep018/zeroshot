def run_tests(namespace, mode="all"):
    cases = [
        ('Sum repeated customers', lambda f: assert_close(f([dict(customer='a',cents=120,cancelled=False),dict(customer='a',cents=80,cancelled=False)]), {'a':200})),
        ('Cancelled order excluded', lambda f: assert_close(f([dict(customer='a',cents=50,cancelled=True)]), {})),
        ('Zero completed order', lambda f: assert_close(f([dict(customer='z',cents=0,cancelled=False)]), {'z':0})),
        ('Empty orders', lambda f: assert_close(f([]), {})),
        ('Separate customers', lambda f: assert_close(f([dict(customer='a',cents=2,cancelled=False),dict(customer='b',cents=3,cancelled=False)]), {'a':2,'b':3})),
        ('Mixed cancellation', lambda f: assert_close(f([dict(customer='a',cents=7,cancelled=True),dict(customer='a',cents=3,cancelled=False)]), {'a':3})),
        ('Reject negative amount', lambda f: rejects(f, [dict(customer='a',cents=-1,cancelled=False)])),
        ('Reject missing customer', lambda f: rejects(f, [dict(cents=1,cancelled=False)])),
        ('Reject nonboolean cancellation', lambda f: rejects(f, [dict(customer='a',cents=1,cancelled=0)])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [dict(customer='a',cents=120,cancelled=False),dict(customer='a',cents=80,cancelled=False)]), {'a':200}))
    ]
    return run_cases(namespace, 'customer_totals', cases, mode)
