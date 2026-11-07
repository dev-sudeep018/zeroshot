def run_tests(namespace, mode="all"):
    cases = [
        ('Shrinking edges', lambda f: assert_close(f([1,2,6,3],1), {'mean':np.array([1.5, 3.0, 3.6666666666666665, 4.5], dtype=float).reshape((4,)),'count':np.array([2, 3, 3, 2], dtype=float).reshape((4,))})),
        ('Zero radius', lambda f: assert_close(f([3,-1,5],0), {'mean':np.array([3.0, -1.0, 5.0], dtype=float).reshape((3,)),'count':np.array([1, 1, 1], dtype=float).reshape((3,))})),
        ('Large radius', lambda f: assert_close(f([1,3],8), {'mean':np.array([2.0, 2.0], dtype=float).reshape((2,)),'count':np.array([2, 2], dtype=float).reshape((2,))})),
        ('Singleton', lambda f: assert_close(f([7],2), {'mean':np.array([7.0], dtype=float).reshape((1,)),'count':np.array([1], dtype=float).reshape((1,))})),
        ('Constant signal', lambda f: assert_close(f([4,4,4],1), {'mean':np.array([4.0, 4.0, 4.0], dtype=float).reshape((3,)),'count':np.array([2, 3, 2], dtype=float).reshape((3,))})),
        ('Symmetric impulse', lambda f: assert_close(f([0,0,6,0,0],1), {'mean':np.array([0.0, 2.0, 2.0, 2.0, 0.0], dtype=float).reshape((5,)),'count':np.array([2, 3, 3, 3, 2], dtype=float).reshape((5,))})),
        ('Reject negative radius', lambda f: rejects(f,[1],-1)),
        ('Reject boolean radius', lambda f: rejects(f,[1],True)),
        ('Reject empty data', lambda f: rejects(f,[],1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,2,6,3],1), {'mean':np.array([1.5, 3.0, 3.6666666666666665, 4.5], dtype=float).reshape((4,)),'count':np.array([2, 3, 3, 2], dtype=float).reshape((4,))})),
    ]
    return run_cases(namespace, 'centered_smoothing', cases, mode)
