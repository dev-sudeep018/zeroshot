def run_tests(namespace, mode="all"):
    cases = [
        ('One matched code', lambda f: assert_close(f([[2,4]],[[1,2]],0.25), {'codebook_loss':2.5,'commitment_loss':0.625,'encoder_gradient':np.array([[0.25, 0.5]], dtype='float64'),'code_gradient':np.array([[-1.0, -2.0]], dtype='float64')})),
        ('No commitment', lambda f: assert_close(f([[2]],[[0]],0), {'codebook_loss':4.0,'commitment_loss':0.0,'encoder_gradient':np.array([[0.0]], dtype='float64'),'code_gradient':np.array([[-4.0]], dtype='float64')})),
        ('Full commitment', lambda f: assert_close(f([[1],[3]],[[0],[1]],1), {'codebook_loss':2.5,'commitment_loss':2.5,'encoder_gradient':np.array([[1.0], [2.0]], dtype='float64'),'code_gradient':np.array([[-1.0], [-2.0]], dtype='float64')})),
        ('Exact match', lambda f: assert_close(f([[2,3]],[[2,3]],0.5), {'codebook_loss':0.0,'commitment_loss':0.0,'encoder_gradient':np.array([[0.0, 0.0]], dtype='float64'),'code_gradient':np.array([[-0.0, -0.0]], dtype='float64')})),
        ('Opposite residuals', lambda f: assert_close(f([[1,-1]],[[0,0]],0.2), {'codebook_loss':1.0,'commitment_loss':0.2,'encoder_gradient':np.array([[0.2, -0.2]], dtype='float64'),'code_gradient':np.array([[-1.0, 1.0]], dtype='float64')})),
        ('Two feature rows', lambda f: assert_close(f([[1,2],[3,4]],[[0,2],[1,5]],0.5), {'codebook_loss':1.5,'commitment_loss':0.75,'encoder_gradient':np.array([[0.25, 0.0], [0.5, -0.25]], dtype='float64'),'code_gradient':np.array([[-0.5, -0.0], [-1.0, 0.5]], dtype='float64')})),
        ('Reject shape mismatch', lambda f: rejects(f, [[1,2]],[[1]],0.25)),
        ('Reject negative commitment', lambda f: rejects(f, [[1]],[[0]],-0.1)),
        ('Reject nonfinite code', lambda f: rejects(f, [[1]],[[np.inf]],0.5)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [[2,4]],[[1,2]],0.25), {'codebook_loss':2.5,'commitment_loss':0.625,'encoder_gradient':np.array([[0.25, 0.5]], dtype='float64'),'code_gradient':np.array([[-1.0, -2.0]], dtype='float64')})),
    ]
    return run_cases(namespace, 'vq_losses', cases, mode)
