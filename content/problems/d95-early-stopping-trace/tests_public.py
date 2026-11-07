def run_tests(namespace, mode="all"):
    cases = [
        ('Stop after two stalls', lambda f: assert_close(f([5,4,4,4,1],2,0), {'best_epoch':1,'stop_epoch':3,'stall_counts':np.array([0, 0, 1, 2], dtype='int64')})),
        ('Improvement resets patience', lambda f: assert_close(f([5,5,4,4,3],2,0), {'best_epoch':4,'stop_epoch':-1,'stall_counts':np.array([0, 1, 0, 1, 0], dtype='int64')})),
        ('Minimum change boundary', lambda f: assert_close(f([5,4.5,4,4],2,0.5), {'best_epoch':2,'stop_epoch':-1,'stall_counts':np.array([0, 1, 0, 1], dtype='int64')})),
        ('Single epoch', lambda f: assert_close(f([2],1,0), {'best_epoch':0,'stop_epoch':-1,'stall_counts':np.array([0], dtype='int64')})),
        ('Always improving', lambda f: assert_close(f([5,4,3,2],1,0), {'best_epoch':3,'stop_epoch':-1,'stall_counts':np.array([0, 0, 0, 0], dtype='int64')})),
        ('First stall stops', lambda f: assert_close(f([2,3,1],1,0), {'best_epoch':0,'stop_epoch':1,'stall_counts':np.array([0, 1], dtype='int64')})),
        ('Reject zero patience', lambda f: rejects(f, [1,2],0,0)),
        ('Reject negative loss', lambda f: rejects(f, [-1,2],1,0)),
        ('Reject negative delta', lambda f: rejects(f, [1,2],1,-0.1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [5,4,4,4,1],2,0), {'best_epoch':1,'stop_epoch':3,'stall_counts':np.array([0, 0, 1, 2], dtype='int64')})),
    ]
    return run_cases(namespace, 'early_stopping', cases, mode)
