def run_tests(namespace, mode="all"):
    cases = [
        ('Correct confident class', lambda f: assert_close(f([[0,2]],[1],1), {'loss':0.1269280110429726,'temperature_gradient':0.23840584404423507})),
        ('Wrong confident class', lambda f: assert_close(f([[0,2]],[0],1), {'loss':2.1269280110429727,'temperature_gradient':-1.7615941559557649})),
        ('Uniform scores', lambda f: assert_close(f([[3,3]],[0],2), {'loss':0.6931471805599453,'temperature_gradient':0.0})),
        ('Two examples', lambda f: assert_close(f([[1,0],[0,2]],[0,1],1), {'loss':0.22009484928059775,'temperature_gradient':0.25367363270711507})),
        ('Higher temperature', lambda f: assert_close(f([[1,2,3]],[1],3), {'loss':1.135311792800908,'temperature_gradient':-0.024244849716761132})),
        ('Extreme scores', lambda f: assert_close(f([[1000,-1000]],[1],0.5), {'loss':4000.0,'temperature_gradient':-8000.0})),
        ('Reject bad target', lambda f: rejects(f, [[1,2]],[2],1)),
        ('Reject low temperature', lambda f: rejects(f, [[1,2]],[0],0.01)),
        ('Reject target count', lambda f: rejects(f, [[1,2],[2,1]],[0],1)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[0,2]],[1],1), {'loss':0.1269280110429726,'temperature_gradient':0.23840584404423507})),
    ]
    return run_cases(namespace, 'temperature_nll', cases, mode)
