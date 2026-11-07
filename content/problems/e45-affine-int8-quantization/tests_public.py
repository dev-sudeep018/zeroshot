def run_tests(namespace, mode="all"):
    cases = [
        ('Nonzero zero point', lambda f: assert_close(f([-1,0,1], .5, 10), dict(quantized=np.array([8,10,12],dtype=np.int8),reconstructed=np.array([-1.,0.,1.])))),
        ('Round ties to even', lambda f: assert_close(f([.5,1.5,2.5], 1, 0), dict(quantized=np.array([0,2,2],dtype=np.int8),reconstructed=np.array([0.,2.,2.])))),
        ('Saturate extremes', lambda f: assert_close(f([-1000,1000], 1, 0), dict(quantized=np.array([-128,127],dtype=np.int8),reconstructed=np.array([-128.,127.])))),
        ('Promote before subtraction', lambda f: assert_close(f([-200,200], 1, 100), dict(quantized=np.array([-100,127],dtype=np.int8),reconstructed=np.array([-200.,27.])))),
        ('Empty vector', lambda f: assert_close(f([], 1, 0), dict(quantized=np.array([],dtype=np.int8),reconstructed=np.array([])))),
        ('Matrix shape retained', lambda f: assert_close(f([[0,1]], .25, -2), dict(quantized=np.array([[-2,2]],dtype=np.int8),reconstructed=np.array([[0.,1.]])))),
        ('Reject zero scale', lambda f: rejects(f, [1], 0, 0)),
        ('Reject invalid zero point', lambda f: rejects(f, [1], 1, 128)),
        ('Reject overflowing normalized input', lambda f: rejects(f, [1e30], 1e-30, 0)),
        ('Preserve caller inputs', lambda f: assert_close(unchanged(f, [-1,0,1], .5, 10), dict(quantized=np.array([8,10,12],dtype=np.int8),reconstructed=np.array([-1.,0.,1.]))))
        ,('Signed eight-bit storage', lambda f: assert_close(str(f([0,1], .1, 2)["quantized"].dtype), "int8"))
    ]
    return run_cases(namespace, 'affine_quantize', cases, mode)
