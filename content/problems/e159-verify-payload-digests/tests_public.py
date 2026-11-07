def run_tests(namespace, mode="all"):
    cases = [
        ('Known empty digest', lambda f: assert_close(f([b''],['e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855']), [])),
        ('Known abc digest', lambda f: assert_close(f([b'abc'],['ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad']), [])),
        ('Valid syntax wrong hash', lambda f: assert_close(f([b'abc',b''],['0'*64,'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855']), [0])),
        ('No payloads', lambda f: assert_close(f([],[]), [])),
        ('Two mismatches', lambda f: assert_close(f([b'a',b'b'],['0'*64,'f'*64]), [0,1])),
        ('Repeated payload', lambda f: assert_close(f([b'',b''],['0'*64,'0'*64]), [0,1])),
        ('Reject length mismatch', lambda f: rejects(f, [b''],[])),
        ('Reject uppercase digest', lambda f: rejects(f, [b''],['A'*64])),
        ('Reject nonbytes payload', lambda f: rejects(f, ['abc'],['0'*64])),
        ('Preserve caller data', lambda f: assert_close(unchanged(f, [b''],['e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855']), []))
    ]
    return run_cases(namespace, 'digest_mismatches', cases, mode)
