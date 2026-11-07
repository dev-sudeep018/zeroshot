def run_tests(namespace, mode="all"):
    cases = [
        ('Right triangle', lambda f: assert_close(f([3,4,5]), {'angles':np.array([0.6435011087932843, 0.9272952180016123, 1.5707963267948966], dtype=float).reshape((3,)),'area':6.0})),
        ('Equilateral', lambda f: assert_close(f([2,2,2]), {'angles':np.array([1.0471975511965979, 1.0471975511965979, 1.0471975511965979], dtype=float).reshape((3,)),'area':1.7320508075688772})),
        ('Isosceles', lambda f: assert_close(f([5,5,6]), {'angles':np.array([0.9272952180016123, 0.9272952180016123, 1.2870022175865687], dtype=float).reshape((3,)),'area':12.0})),
        ('Reordered sides', lambda f: assert_close(f([5,3,4]), {'angles':np.array([1.5707963267948966, 0.6435011087932843, 0.9272952180016123], dtype=float).reshape((3,)),'area':6.0})),
        ('Small triangle', lambda f: assert_close(f([.3,.4,.5]), {'angles':np.array([0.6435011087932841, 0.9272952180016124, 1.5707963267948966], dtype=float).reshape((3,)),'area':0.059999999999999984})),
        ('Obtuse triangle', lambda f: assert_close(f([2,3,4]), {'angles':np.array([0.5053605102841573, 0.8127555613686607, 1.8234765819369754], dtype=float).reshape((3,)),'area':2.9047375096555625})),
        ('Reject flat triangle', lambda f: rejects(f,[1,2,3])),
        ('Reject impossible triangle', lambda f: rejects(f,[1,1,4])),
        ('Reject nonpositive side', lambda f: rejects(f,[0,1,1])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[3,4,5]), {'angles':np.array([0.6435011087932843, 0.9272952180016123, 1.5707963267948966], dtype=float).reshape((3,)),'area':6.0})),
    ]
    return run_cases(namespace, 'triangle_from_sides', cases, mode)
