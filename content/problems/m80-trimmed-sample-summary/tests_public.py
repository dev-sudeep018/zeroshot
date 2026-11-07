def run_tests(namespace, mode="all"):
    cases = [
        ('Remove two tails', lambda f: assert_close(f([100,2,3,4,-50],1), {'mean':3.0,'count':3,'retained':np.array([2.0, 3.0, 4.0], dtype=float).reshape((3,))})),
        ('No trimming', lambda f: assert_close(f([3,1,2],0), {'mean':2.0,'count':3,'retained':np.array([1.0, 2.0, 3.0], dtype=float).reshape((3,))})),
        ('Keep one', lambda f: assert_close(f([7,1,9,3,5],2), {'mean':5.0,'count':1,'retained':np.array([5.0], dtype=float).reshape((1,))})),
        ('Ties at cutoff', lambda f: assert_close(f([1,1,1,8,8,8],1), {'mean':4.5,'count':4,'retained':np.array([1.0, 1.0, 8.0, 8.0], dtype=float).reshape((4,))})),
        ('Single sample', lambda f: assert_close(f([4],0), {'mean':4.0,'count':1,'retained':np.array([4.0], dtype=float).reshape((1,))})),
        ('Negative sample', lambda f: assert_close(f([-9,-3,-2,-1],1), {'mean':-2.5,'count':2,'retained':np.array([-3.0, -2.0], dtype=float).reshape((2,))})),
        ('Reject empty result', lambda f: rejects(f,[1,2],1)),
        ('Reject negative trim', lambda f: rejects(f,[1],-1)),
        ('Reject fractional count', lambda f: rejects(f,[1,2,3],.5)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[100,2,3,4,-50],1), {'mean':3.0,'count':3,'retained':np.array([2.0, 3.0, 4.0], dtype=float).reshape((3,))})),
    ]
    return run_cases(namespace, 'trimmed_summary', cases, mode)
