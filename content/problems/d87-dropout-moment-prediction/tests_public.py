def run_tests(namespace, mode="all"):
    cases = [
        ('Half retained', lambda f: assert_close(f([2,-3],0.5), dict(mean=np.array([2,-3]),variance=np.array([4,9]),second_moment=np.array([8,18])))),
        ('No dropout', lambda f: assert_close(f([2,3],1), dict(mean=np.array([2,3]),variance=np.zeros(2),second_moment=np.array([4,9])))),
        ('Quarter retained', lambda f: assert_close(f([1],0.25), dict(mean=np.array([1]),variance=np.array([3]),second_moment=np.array([4])))),
        ('Zero activation', lambda f: assert_close(f([0],0.1), dict(mean=np.array([0]),variance=np.array([0]),second_moment=np.array([0])))),
        ('Mostly retained', lambda f: assert_close(f([2],0.8), dict(mean=np.array([2]),variance=np.array([1]),second_moment=np.array([5])))),
        ('Negative activation', lambda f: assert_close(f([-0.5],0.5), dict(mean=np.array([-0.5]),variance=np.array([0.25]),second_moment=np.array([0.5])))),
        ('Reject zero probability', lambda f: rejects(f, [1],0)),
        ('Reject probability above one', lambda f: rejects(f, [1],1.1)),
        ('Reject matrix activations', lambda f: rejects(f, [[1]],0.5)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [2,-3],0.5), dict(mean=np.array([2,-3]),variance=np.array([4,9]),second_moment=np.array([8,18])))),
    ]
    return run_cases(namespace, 'dropout_moments', cases, mode)
