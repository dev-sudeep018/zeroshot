def run_tests(namespace, mode="all"):
    cases = [
        ('Equal noise follows logits', lambda f: assert_close(f([0,2],[0.5,0.5]), 1)),
        ('Noise changes the winner', lambda f: assert_close(f([0,1],[0.99,0.01]), 0)),
        ('Exact ties choose first', lambda f: assert_close(f([3,3],[0.5,0.5]), 0)),
        ('Single category', lambda f: assert_close(f([-100],[0.2]), 0)),
        ('Third category has strongest noise', lambda f: assert_close(f([0,0,0],[0.1,0.2,0.9]), 2)),
        ('Shifted logits', lambda f: assert_close(f([100,101],[0.99,0.01]), 0)),
        ('Large preference dominates', lambda f: assert_close(f([-1000,1000],[0.99,0.01]), 1)),
        ('Reject closed lower endpoint', lambda f: rejects(f, [0],[0])),
        ('Reject closed upper endpoint', lambda f: rejects(f, [0],[1])),
        ('Reject shape mismatch', lambda f: rejects(f, [0,1],[0.5])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [0,2],[0.5,0.5]), 1)),
        ('Huge common logit shift', lambda f: assert_close(f([1e30,1e30],[.01,.99]),1))
    ]
    return run_cases(namespace, 'gumbel_choice', cases, mode)
