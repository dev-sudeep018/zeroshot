def run_tests(namespace, mode="all"):
    cases = [
        ('Horizontal pair', lambda f: assert_close(f([[-1,0],[1,0]],[1,1]), {'center':np.array([0.0, 0.0], dtype=float).reshape((2,)),'inertia':np.array([[0.0, -0.0], [-0.0, 2.0]], dtype=float).reshape((2, 2)),'polar':2.0})),
        ('Unequal masses', lambda f: assert_close(f([[0,0],[3,0]],[2,1]), {'center':np.array([1.0, 0.0], dtype=float).reshape((2,)),'inertia':np.array([[0.0, -0.0], [-0.0, 6.0]], dtype=float).reshape((2, 2)),'polar':6.0})),
        ('Square corners', lambda f: assert_close(f([[-1,-1],[-1,1],[1,-1],[1,1]],[1,1,1,1]), {'center':np.array([0.0, 0.0], dtype=float).reshape((2,)),'inertia':np.array([[4.0, -0.0], [-0.0, 4.0]], dtype=float).reshape((2, 2)),'polar':8.0})),
        ('Single mass', lambda f: assert_close(f([[2,3]],[4]), {'center':np.array([2.0, 3.0], dtype=float).reshape((2,)),'inertia':np.array([[0.0, -0.0], [-0.0, 0.0]], dtype=float).reshape((2, 2)),'polar':0.0})),
        ('Zero mass point', lambda f: assert_close(f([[0,0],[9,9],[2,0]],[1,0,1]), {'center':np.array([1.0, 0.0], dtype=float).reshape((2,)),'inertia':np.array([[0.0, -0.0], [-0.0, 2.0]], dtype=float).reshape((2, 2)),'polar':2.0})),
        ('Diagonal pair', lambda f: assert_close(f([[0,0],[2,2]],[1,1]), {'center':np.array([1.0, 1.0], dtype=float).reshape((2,)),'inertia':np.array([[2.0, -2.0], [-2.0, 2.0]], dtype=float).reshape((2, 2)),'polar':4.0})),
        ('Reject zero total', lambda f: rejects(f,[[0,0]],[0])),
        ('Reject negative mass', lambda f: rejects(f,[[0,0]],[-1])),
        ('Reject length mismatch', lambda f: rejects(f,[[0,0],[1,1]],[1])),
        ('Leave all inputs unchanged', lambda f: assert_close(unchanged(f,[[-1,0],[1,0]],[1,1]), {'center':np.array([0.0, 0.0], dtype=float).reshape((2,)),'inertia':np.array([[0.0, -0.0], [-0.0, 2.0]], dtype=float).reshape((2, 2)),'polar':2.0})),
    ]
    return run_cases(namespace, 'planar_mass_moments', cases, mode)
