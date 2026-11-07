def run_tests(namespace, mode="all"):
    cases = [
        ('Same relative preference', lambda f: assert_close(f([-1],[-3],[-2],[-4],1),np.log(2))),
        ('Improved preference', lambda f: assert_close(f([-1],[-3],[-2],[-2],1),np.logaddexp(0,-2))),
        ('Strongly wrong preference', lambda f: assert_close(f([-1000],[0],[0],[0],1),1000)),
        ('Reference matters', lambda f: assert_close(f([-1],[-3],[-1],[-5],1),np.logaddexp(0,2))),
        ('Zero beta', lambda f: assert_close(f([-1000],[0],[0],[-1000],0),np.log(2))),
        ('Batch mean', lambda f: assert_close(f([-1,-3],[-3,-1],[-2,-2],[-2,-2],1),(np.logaddexp(0,-2)+np.logaddexp(0,2))/2)),
        ('Shared log-probability shifts', lambda f: assert_close(f([-11],[-13],[-22],[-22],1),np.logaddexp(0,-2))),
        ('Reject positive log probability', lambda f: rejects(f,[-1],[-2],[1],[-2])),
        ('Reject broadcast shape', lambda f: rejects(f,[-1,-2],[-2],[-1,-2],[-2,-3])),
        ('Reject invalid beta', lambda f: [rejects(f,[-1],[-2],[-1],[-2],v) for v in (-.1,True,2**4096)]),
        ('Reject empty input', lambda f: rejects(f,[],[],[],[])),
        ('No mutation', lambda f: assert_close(unchanged(f,np.array([-1.]),np.array([-3.]),np.array([-2.]),np.array([-2.]),1),np.logaddexp(0,-2)))
    ]
    return run_cases(namespace, 'dpo_loss', cases, mode)
