def run_tests(namespace, mode="all"):
    cases = [
        ('Only one possible partner', lambda f: assert_close(f(np.zeros((2,2)),[0,0]),0.)),
        ('Three equal positive partners', lambda f: assert_close(f(np.zeros((4,4)),[0,0,0,0]),np.log(3))),
        ('Two classes uniform scores', lambda f: assert_close(f(np.zeros((4,4)),[0,0,1,1]),np.log(3))),
        ('Diagonal excluded', lambda f: assert_close(f(np.eye(4)*1000,[0,0,1,1]),np.log(3))),
        ('All positives are averaged', lambda f: assert_close(f(np.zeros((3,3)),[7,7,7]),np.log(2))),
        ('Favor each same-label partner', lambda f: assert_close(f(np.array([[0,np.log(3),0,0],[np.log(3),0,0,0],[0,0,0,np.log(3)],[0,0,np.log(3),0]]),[0,0,1,1]),np.log(5/3))),
        ('Per-row shifts cancel', lambda f: assert_close(f(np.tile(np.arange(4)[:,None]*1000,(1,4)),[0,0,1,1]),np.log(3))),
        ('Extreme shared shift stays stable', lambda f: assert_close(f(np.full((4,4),1e30),[0,0,1,1]),np.log(3))),
        ('Reject singleton class', lambda f: rejects(f,np.zeros((3,3)),[0,0,1])),
        ('Reject fractional labels', lambda f: rejects(f,np.zeros((2,2)),[0.0,0.0])),
        ('Reject nonsquare scores', lambda f: rejects(f,np.zeros((2,3)),[0,0])),
        ('Inputs remain unchanged', lambda f: assert_close(unchanged(f,np.zeros((2,2)),[0,0]),0.)),
    ]
    return run_cases(namespace, 'supervised_contrastive', cases, mode)
