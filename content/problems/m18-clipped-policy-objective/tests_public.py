def run_tests(namespace, mode="all"):
    cases = [
        ('Unchanged policy', lambda f: assert_close(f([-1,-2],[-1,-2],[2,-1]),-.5)),
        ('Rewarded action doubles in probability', lambda f: assert_close(f([-1+np.log(2)],[-1],[1]),-1.2)),
        ('Penalized action doubles in probability', lambda f: assert_close(f([-1+np.log(2)],[-1],[-1]),2)),
        ('Lower boundary with negative advantage', lambda f: assert_close(f([-1-np.log(2)],[-1],[-1]),.8)),
        ('Lower ratio with positive advantage', lambda f: assert_close(f([-1-np.log(2)],[-1],[1]),-.5)),
        ('Inside clipping interval', lambda f: assert_close(f([-1+np.log(1.1)],[-1],[2]),-2.2)),
        ('Zero advantages', lambda f: assert_close(f([-1],[-2],[0]),0)),
        ('Reject shape mismatch', lambda f: rejects(f,[-1],[-1,-2],[1])),
        ('Reject invalid clipping', lambda f: [rejects(f,[-1],[-1],[1],v) for v in (-.1,1,True,2**4096)]),
        ('Reject invalid log probabilities', lambda f: [rejects(f,a,b,[1]) for a,b in (([1],[-1]),([-61.1],[0]),([np.nan],[-1]))]),
        ('Reject empty input', lambda f: rejects(f,[],[],[])),
        ('No mutation', lambda f: assert_close(unchanged(f,np.array([-1.,-2.]),np.array([-1.,-2.]),np.array([2.,-1.])), -.5))
    ]
    return run_cases(namespace, 'ppo_loss', cases, mode)
