def run_tests(namespace, mode="all"):
    cases = [
        ('A wider beam rescues a better finish', lambda f: assert_close(f([[-2,-.1,-.2],[-2,-2,-2],[-1,-1,-1]], 0, 2, 2, 2), dict(tokens=[0,2],score=-.2))),
        ('Width one follows the greedy branch', lambda f: assert_close(f([[-2,-.1,-.2],[-2,-2,-2],[-1,-1,-1]], 0, 2, 1, 2), dict(tokens=[0,1,0],score=-2.1))),
        ('No generation steps', lambda f: assert_close(f([[-1,-1],[-1,-1]], 0, 1, 2, 0), dict(tokens=[0],score=0.))),
        ('Start already complete', lambda f: assert_close(f([[-1,-1],[-1,-1]], 1, 1, 2, 4), dict(tokens=[1],score=0.))),
        ('Lexicographic score tie', lambda f: assert_close(f([[-1,-1],[-1,-1]], 0, 1, 2, 1), dict(tokens=[0,0],score=-1.))),
        ('EOS stops extension', lambda f: assert_close(f([[-5,-.1],[-1,-1]], 0, 1, 1, 5), dict(tokens=[0,1],score=-.1))),
        ('Reject positive log score', lambda f: rejects(f, [[1]], 0, 0, 1, 1)),
        ('Reject zero beam width', lambda f: rejects(f, [[-1]], 0, 0, 0, 1)),
        ('Reject invalid token', lambda f: rejects(f, [[-1]], 1, 0, 1, 1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[-2,-.1,-.2],[-2,-2,-2],[-1,-1,-1]], 0, 2, 2, 2), dict(tokens=[0,2],score=-.2)))
    ]
    return run_cases(namespace, 'beam_search', cases, mode)
