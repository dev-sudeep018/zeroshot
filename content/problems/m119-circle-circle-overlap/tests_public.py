def run_tests(namespace, mode="all"):
    cases = [
        ('Equal partial overlap', lambda f: assert_close(f(1,1,1), 1.228369698608757)),
        ('Separated disks', lambda f: assert_close(f(1,2,4), 0.0)),
        ('Contained disk', lambda f: assert_close(f(3,1,1), 3.141592653589793)),
        ('Coincident disks', lambda f: assert_close(f(2,2,0), 12.566370614359172)),
        ('External tangency', lambda f: assert_close(f(1,2,3), 0.0)),
        ('Unequal partial overlap', lambda f: assert_close(f(2,3,4), 1.989791818720934)),
        ('Reject zero radius', lambda f: rejects(f,0,1,1)),
        ('Reject negative distance', lambda f: rejects(f,1,1,-1)),
        ('Reject boolean radius', lambda f: rejects(f,True,1,1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,1,1,1), 1.228369698608757)),
    ]
    return run_cases(namespace, 'disk_overlap', cases, mode)
