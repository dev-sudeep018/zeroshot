"""Independent M01 oracles. Set MASTERY_MATH2000_ROOT to inspect staged drafts.

The default checks published content when present and skips an unintegrated batch.
These tests do not import the authoring writer or its fixture expectations.
"""
import ast
import copy
import itertools
import json
import os
from pathlib import Path
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(os.environ.get('MASTERY_MATH2000_ROOT', ROOT / 'content/problems'))
FOLDERS = {int(p.name.split('-')[0][1:]): p for p in BASE.glob('m1[67][0-9]-*') if p.is_dir()}
HELPERS = (ROOT / 'content/evaluator_helpers.py').read_text(encoding='utf8')


def function(number):
    folder = FOLDERS[number]
    metadata = json.loads((folder / 'problem.yaml').read_text(encoding='utf8'))
    namespace = {}
    exec((folder / 'solution.py').read_text(encoding='utf8'), namespace)
    return namespace[metadata['evaluation']['entrypoint']]


def close(a, b):
    np.testing.assert_allclose(a, b, atol=1e-9, rtol=1e-9)


@unittest.skipUnless(FOLDERS, 'M01 is not integrated; set MASTERY_MATH2000_ROOT for staged checks')
class Math2000Batch01Tests(unittest.TestCase):
    def test_fixture_contract_examples_starter_and_canned_answers(self):
        self.assertIn(len(FOLDERS), (5,10,15,20))
        for number, folder in FOLDERS.items():
            with self.subTest(lesson=number):
                metadata = json.loads((folder / 'problem.yaml').read_text(encoding='utf8'))
                lesson = json.loads((folder / 'lesson.json').read_text(encoding='utf8'))
                evaluator, reference, starter = {}, {}, {}
                exec(HELPERS + '\n' + (folder / 'tests_public.py').read_text(encoding='utf8'), evaluator)
                source = (folder / 'solution.py').read_text(encoding='utf8')
                self.assertLess(len(source), 32000)
                exec(source, reference)
                exec((folder / 'starter.py').read_text(encoding='utf8'), starter)
                cases = evaluator['run_tests'](reference)
                self.assertGreaterEqual(len(cases),10)
                self.assertEqual(len(cases),lesson['test_count'])
                self.assertTrue(all(c['passed'] for c in cases), cases)
                samples = evaluator['run_tests'](reference,'sample')
                self.assertEqual([c['name'] for c in samples], [e['name'] for e in lesson['examples']])
                self.assertFalse(any(c['passed'] for c in evaluator['run_tests'](starter)))
                fn = metadata['evaluation']['entrypoint']
                canned_result = eval(lesson['examples'][0]['input'], reference)
                canned = lambda *a, **kw: copy.deepcopy(canned_result)
                results = evaluator['run_tests']({fn:canned})
                self.assertTrue(any(not c['passed'] for c in results[:6]))
                for example in lesson['examples']:
                    displayed = ast.literal_eval(example['output'].split('\n(',1)[0])
                    actual = eval(example['input'], reference)
                    def plain(x):
                        if isinstance(x,np.ndarray): return plain(x.tolist())
                        if isinstance(x,np.generic): return x.item()
                        if isinstance(x,dict): return {k:plain(v) for k,v in x.items()}
                        if isinstance(x,(tuple,list)): return [plain(v) for v in x]
                        return x
                    evaluator['assert_close'](plain(actual),displayed)

    def test_gain_enumerated_hypercube_vertices(self):
        rng = np.random.default_rng(260160)
        f = function(160)
        for m,n in [(1,1),(2,4),(5,3),(3,5)]:
            for _ in range(8):
                a = rng.integers(-8,9,size=(m,n)).astype(float)
                out = f(a)
                all_outputs = [a @ np.array(v) for v in itertools.product([-1.,1.],repeat=n)]
                best = max(max(abs(y)) for y in all_outputs)
                self.assertEqual(out['gain'], best)
                self.assertEqual(max(abs(out['output'])), best)
                close(a @ out['witness'],out['output'])
                self.assertEqual(out['row'],next(i for i in range(m) if sum(abs(v) for v in a[i])==best))
                close(f(-3*a)['gain'],3*best)

    def test_symmetry_reconstruction_and_energy_cancellation(self):
        rng = np.random.default_rng(260161)
        for n in [1,2,5,9]:
            a,x = rng.normal(size=(n,n)),rng.normal(size=n)
            out = function(161)(a,x)
            close(out['symmetric']+out['skew'],a)
            close(out['symmetric'],out['symmetric'].T)
            close(out['skew'],-out['skew'].T)
            close(out['energy'],sum(x[i]*a[i,j]*x[j] for i in range(n) for j in range(n)))
            close(x@out['skew']@x,0)
            close(np.sum(out['symmetric']*out['skew']),0)

    def test_dominance_minimality(self):
        rng = np.random.default_rng(260162)
        for n in [1,3,7]:
            a = rng.integers(-4,5,size=(n,n)).astype(float)
            np.fill_diagonal(a,rng.integers(0,8,size=n))
            for target in [0,0.5,4]:
                out = function(162)(a,target)
                for i in range(n):
                    off = sum(abs(a[i,j]) for j in range(n) if i!=j)
                    self.assertEqual(out['margins'][i],a[i,i]-off)
                    self.assertGreaterEqual(out['repaired'][i,i]-off,target)
                    if out['loading'][i] > 0:
                        close(out['repaired'][i,i]-off,target)
                close(out['repaired']-a,np.diag(out['loading']))
                close(function(162)(out['repaired'],target)['loading'],0)

    def test_permutation_coordinate_identity(self):
        rng = np.random.default_rng(260163)
        for m,n in [(2,5),(7,3),(1,4),(4,1)]:
            a,x = rng.normal(size=(m,n)),rng.normal(size=n)
            r,c = rng.permutation(m),rng.permutation(n)
            out = function(163)(a,x,r,c)
            expected = np.array([[a[i,j] for j in c] for i in r])
            close(out['matrix'],expected)
            close(out['output'],(a@x)[r])
            close(out['restored'],a@x)

    def test_band_unpack_and_dense_product(self):
        rng = np.random.default_rng(260164)
        for m,n,lo,up in [(4,6,2,1),(6,3,1,2),(5,5,0,0),(2,3,7,5)]:
            a = rng.normal(size=(m,n))
            for i in range(m):
                for j in range(n):
                    if not -up<=i-j<=lo: a[i,j]=0
            x = rng.normal(size=n)
            out = function(164)(a,x,lo,up)
            rebuilt = np.zeros_like(a)
            for k,j in np.ndindex(out['storage'].shape):
                i=j+k-up
                if 0<=i<m: rebuilt[i,j]=out['storage'][k,j]
                else: self.assertEqual(out['storage'][k,j],0)
            close(rebuilt,a)
            close(out['product'],a@x)

    def test_rejection_and_no_mutation_first_group(self):
        arguments = {160: [[[2.,-1.],[3.,4.]]],161: [[[2.,-1.],[3.,4.]],[1.,2.]],162: [[[2.,-1.],[3.,4.]],1.],163: [[[2.,-1.],[3.,4.]],[1.,2.],[1,0],[1,0]],164: [[[2.,-1.],[3.,4.]],[1.,2.],1,1]}
        for number,args in arguments.items():
            args = [np.array(x) if isinstance(x,list) else x for x in args]
            before = copy.deepcopy(args)
            function(number)(*args)
            for a,b in zip(args,before): close(a,b)
            for bad in [[], [1,2], [[True]], [[complex(1,1)]], [[np.inf]], [[10001]], [['1']], np.zeros((65,1))]:
                with self.subTest(number=number,bad=repr(bad)[:50]), self.assertRaises(ValueError):
                    function(number)(bad,*args[1:])


if __name__ == '__main__':
    unittest.main()
