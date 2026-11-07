def run_tests(namespace, mode="all"):
    cases = [
        ('Season length two', lambda f: assert_close(f([1,10,3,13,6,17],2), {'initial':np.array([1.0, 10.0], dtype=float).reshape((2,)),'difference':np.array([2.0, 3.0, 3.0, 4.0], dtype=float).reshape((4,)),'reconstructed':np.array([1.0, 10.0, 3.0, 13.0, 6.0, 17.0], dtype=float).reshape((6,))})),
        ('First differences', lambda f: assert_close(f([2,5,4],1), {'initial':np.array([2.0], dtype=float).reshape((1,)),'difference':np.array([3.0, -1.0], dtype=float).reshape((2,)),'reconstructed':np.array([2.0, 5.0, 4.0], dtype=float).reshape((3,))})),
        ('One difference', lambda f: assert_close(f([1,2,3,8],3), {'initial':np.array([1.0, 2.0, 3.0], dtype=float).reshape((3,)),'difference':np.array([7.0], dtype=float).reshape((1,)),'reconstructed':np.array([1.0, 2.0, 3.0, 8.0], dtype=float).reshape((4,))})),
        ('Repeated season', lambda f: assert_close(f([2,7,2,7],2), {'initial':np.array([2.0, 7.0], dtype=float).reshape((2,)),'difference':np.array([0.0, 0.0], dtype=float).reshape((2,)),'reconstructed':np.array([2.0, 7.0, 2.0, 7.0], dtype=float).reshape((4,))})),
        ('Negative values', lambda f: assert_close(f([-2,-1,0,3],1), {'initial':np.array([-2.0], dtype=float).reshape((1,)),'difference':np.array([1.0, 1.0, 3.0], dtype=float).reshape((3,)),'reconstructed':np.array([-2.0, -1.0, 0.0, 3.0], dtype=float).reshape((4,))})),
        ('Fractional season', lambda f: assert_close(f([.5,2,1.5,4],2), {'initial':np.array([0.5, 2.0], dtype=float).reshape((2,)),'difference':np.array([1.0, 2.0], dtype=float).reshape((2,)),'reconstructed':np.array([0.5, 2.0, 1.5, 4.0], dtype=float).reshape((4,))})),
        ('Reject zero lag', lambda f: rejects(f,[1,2],0)),
        ('Reject lag equals length', lambda f: rejects(f,[1,2],2)),
        ('Reject singleton', lambda f: rejects(f,[1],1)),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[1,10,3,13,6,17],2), {'initial':np.array([1.0, 10.0], dtype=float).reshape((2,)),'difference':np.array([2.0, 3.0, 3.0, 4.0], dtype=float).reshape((4,)),'reconstructed':np.array([1.0, 10.0, 3.0, 13.0, 6.0, 17.0], dtype=float).reshape((6,))})),
    ]
    return run_cases(namespace, 'seasonal_differences', cases, mode)
