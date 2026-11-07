def run_tests(namespace, mode="all"):
    cases = [
        ('One-state survival', lambda f: assert_close(f([1],[[.5]],3), {'survival':np.array([1.0, 0.5, 0.25, 0.125], dtype=float).reshape((4,)),'absorbed':np.array([0.5, 0.25, 0.125], dtype=float).reshape((3,)),'remaining':np.array([0.125], dtype=float).reshape((1,))})),
        ('Two transient states', lambda f: assert_close(f([1,0],[[.5,.25],[0,.5]],3), {'survival':np.array([1.0, 0.75, 0.5, 0.3125], dtype=float).reshape((4,)),'absorbed':np.array([0.25, 0.25, 0.1875], dtype=float).reshape((3,)),'remaining':np.array([0.125, 0.1875], dtype=float).reshape((2,))})),
        ('No absorption', lambda f: assert_close(f([.2,.8],[[1,0],[0,1]],2), {'survival':np.array([1.0, 1.0, 1.0], dtype=float).reshape((3,)),'absorbed':np.array([0.0, 0.0], dtype=float).reshape((2,)),'remaining':np.array([0.2, 0.8], dtype=float).reshape((2,))})),
        ('Immediate absorption', lambda f: assert_close(f([.3,.7],[[0,0],[0,0]],2), {'survival':np.array([1.0, 0.0, 0.0], dtype=float).reshape((3,)),'absorbed':np.array([1.0, 0.0], dtype=float).reshape((2,)),'remaining':np.array([0.0, 0.0], dtype=float).reshape((2,))})),
        ('Zero steps', lambda f: assert_close(f([1],[[.2]],0), {'survival':np.array([1.0], dtype=float).reshape((1,)),'absorbed':np.array([], dtype=float).reshape((0,)),'remaining':np.array([1.0], dtype=float).reshape((1,))})),
        ('Transition before absorbing', lambda f: assert_close(f([1,0],[[0,1],[0,0]],3), {'survival':np.array([1.0, 1.0, 0.0, 0.0], dtype=float).reshape((4,)),'absorbed':np.array([0.0, 1.0, 0.0], dtype=float).reshape((3,)),'remaining':np.array([0.0, 0.0], dtype=float).reshape((2,))})),
        ('Reject row sum above one', lambda f: rejects(f,[1],[[1.1]],1)),
        ('Reject negative entry', lambda f: rejects(f,[1,0],[[1,-.1],[0,1]],1)),
        ('Reject size mismatch', lambda f: rejects(f,[1],[[.5,0],[0,.5]],1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1],[[.5]],3), {'survival':np.array([1.0, 0.5, 0.25, 0.125], dtype=float).reshape((4,)),'absorbed':np.array([0.5, 0.25, 0.125], dtype=float).reshape((3,)),'remaining':np.array([0.125], dtype=float).reshape((1,))})),
    ]
    return run_cases(namespace, 'absorption_trace', cases, mode)
