def run_tests(namespace, mode="all"):
    cases = [
        ('Exact grid is unchanged', lambda f: assert_close(f([0.2,0.5,0.3],[-1,0,1],0,1,0), np.array([0.2,0.5,0.3]))),
        ('Terminal point between bins', lambda f: assert_close(f([0.2,0.5,0.3],[-1,0,1],0.5,1,1), np.array([0.,0.5,0.5]))),
        ('Contract toward the center', lambda f: assert_close(f([0.5,0,0.5],[-1,0,1],0,0.5,0), np.array([0.25,0.5,0.25]))),
        ('Clip high rewards', lambda f: assert_close(f([0.2,0.5,0.3],[-1,0,1],10,1,0), np.array([0.,0.,1.]))),
        ('Clip low rewards', lambda f: assert_close(f([1,0],[0,2],-3,1,0), np.array([1.,0.]))),
        ('Mass accumulates at same target', lambda f: assert_close(f([0.25,0.25,0.5],[0,1,2],1,0,0), np.array([0.,1.,0.]))),
        ('Non-unit support spacing', lambda f: assert_close(f([0.5,0.5],[0,2],0.5,0.5,0), np.array([0.5,0.5]))),
        ('Reject unnormalized probabilities', lambda f: rejects(f, [1,1],[0,1],0,1,0)),
        ('Reject nonuniform support', lambda f: rejects(f, [0.2,0.5,0.3],[0,1,3],0,1,0)),
        ('Reject invalid terminal flag', lambda f: rejects(f, [0.5,0.5],[0,1],0,1,True)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [0.2,0.5,0.3],[-1,0,1],0,1,0), np.array([0.2,0.5,0.3]))),
        ('Near-uniform support keeps exact atom', lambda f: assert_close(f([0,0,1,0],[0,1e-8,2.009e-8,3.018e-8],0,1,0), np.array([0.,0.,1.,0.])))
    ]
    return run_cases(namespace, 'project_value_distribution', cases, mode)
