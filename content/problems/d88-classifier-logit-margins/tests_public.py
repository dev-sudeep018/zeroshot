def run_tests(namespace, mode="all"):
    cases = [
        ('Unequal scores', lambda f: assert_close(f([[1,4,2]]), dict(winner=np.array([1]),runner_up=np.array([2]),margin=np.array([2])))),
        ('Tied leaders', lambda f: assert_close(f([[3,3,1]]), dict(winner=np.array([0]),runner_up=np.array([1]),margin=np.array([0])))),
        ('Negative scores', lambda f: assert_close(f([[-5,-2,-3]]), dict(winner=np.array([1]),runner_up=np.array([2]),margin=np.array([1])))),
        ('Separate examples', lambda f: assert_close(f([[1,0],[0,2]]), dict(winner=np.array([0,1]),runner_up=np.array([1,0]),margin=np.array([1,2])))),
        ('Tied runners-up', lambda f: assert_close(f([[0,2,0]]), dict(winner=np.array([1]),runner_up=np.array([0]),margin=np.array([2])))),
        ('All tied', lambda f: assert_close(f([[0,0,0,0]]), dict(winner=np.array([0]),runner_up=np.array([1]),margin=np.array([0])))),
        ('Reject one class', lambda f: rejects(f, [[1]])),
        ('Reject vector scores', lambda f: rejects(f, [1,2])),
        ('Reject nonfinite scores', lambda f: rejects(f, [[1,np.inf]])),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[1,4,2]]), dict(winner=np.array([1]),runner_up=np.array([2]),margin=np.array([2])))),
    ]
    return run_cases(namespace, 'logit_margins', cases, mode)
