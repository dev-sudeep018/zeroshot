"""Independent properties and valid-input counterexamples for platform batch three."""
import json
import math
import pathlib
import unittest

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASE = ROOT / 'content/problems'
HELPERS = (ROOT / 'content/evaluator_helpers.py').read_text(encoding='utf-8')


def load(prefix, filename='solution.py'):
    folder, = BASE.glob(prefix+'-*')
    namespace = {}
    source = HELPERS+'\n' if filename == 'tests_public.py' else ''
    exec(source+(folder/filename).read_text(encoding='utf-8'),namespace)
    return namespace


class PlatformBatch03Tests(unittest.TestCase):
    def test_ppo_clipping_depends_on_advantage_sign(self):
        f = load('m18')['ppo_loss']
        ratios = np.tile([.3,.9,1,1.1,1.7],2)
        advantages = np.array([2]*5+[-3]*5)
        old = np.full(10,-3.)
        for clip in [0,.2,.9]:
            # Independent piecewise form: the bounded side changes with the sign.
            expected = -sum((min(r,1+clip) if a>=0 else max(r,1-clip))*a for r,a in zip(ratios,advantages))/10
            self.assertAlmostEqual(f(old+np.log(ratios),old,advantages,clip),expected)
        # At a saturated beneficial update, increasing the log-ratio has zero slope.
        for ratio,adv in [(2.,1.),(.5,-1.)]:
            x = -3+math.log(ratio)
            self.assertAlmostEqual((f([x+1e-5],[-3],[adv])-f([x-1e-5],[-3],[adv]))/2e-5,0)

    def test_dpo_swap_identity_and_reference_shift(self):
        f = load('m19')['dpo_loss']
        rng = np.random.default_rng(619)
        pc,pr,rc,rr = -rng.uniform(.1,8,size=(4,17))
        beta = .7
        margin = beta*((pc-pr)-(rc-rr))
        self.assertAlmostEqual(f(pc,pr,rc,rr,beta)-f(pr,pc,rr,rc,beta),-margin.mean())
        shifts = rng.uniform(0,20,size=17)
        self.assertAlmostEqual(f(pc-shifts,pr-shifts,rc-4,rr-4,beta),f(pc,pr,rc,rr,beta))
        self.assertAlmostEqual(f(pc,pr,rc,rr,0),math.log(2))
        np.testing.assert_allclose(f([-1e30],[0],[0],[0],1e30),1e60,rtol=1e-15)

    def test_flow_path_derivative_and_translation(self):
        f = load('d33')['flow_matching']
        rng = np.random.default_rng(633)
        x0,x1 = rng.normal(size=(2,7,4)); t=rng.uniform(.1,.9,size=7)
        velocity=x1-x0; prediction=velocity+.3
        out=f(x0,x1,t,prediction)
        derivative=(f(x0,x1,t+1e-5,prediction)['point']-f(x0,x1,t-1e-5,prediction)['point'])/2e-5
        np.testing.assert_allclose(derivative,out['velocity'],atol=1e-10)
        self.assertAlmostEqual(out['loss'],.09)
        translated=f(x0+9,x1+9,t,prediction)
        np.testing.assert_allclose(translated['point'],out['point']+9)
        np.testing.assert_allclose(translated['velocity'],out['velocity'])
        self.assertAlmostEqual(translated['loss'],out['loss'])

    def test_ddim_recovers_a_synthetic_forward_trajectory(self):
        f=load('d34')['ddim_step']; rng=np.random.default_rng(634)
        clean,noise=rng.normal(size=(2,2,3,4))
        retention=.04
        sample=math.sqrt(retention)*clean+math.sqrt(1-retention)*noise
        for previous in [.16,.49,1.]:
            out=f(sample,noise,retention,previous)
            np.testing.assert_allclose(out['predicted_clean'],clean,atol=1e-14)
            np.testing.assert_allclose(out['sample'],math.sqrt(previous)*clean+math.sqrt(1-previous)*noise,atol=1e-14)
            sample=out['sample']; retention=previous
        np.testing.assert_allclose(sample,clean,atol=1e-14)

    def test_alibi_matches_scalar_scores_and_sequence_reversal(self):
        f=load('d35')['alibi_attention']; rng=np.random.default_rng(635)
        q,k=rng.normal(size=(2,3,5,4)); v=rng.normal(size=(3,5,2)); slopes=np.array([0,.2,2.])
        expected=np.empty((3,5,2))
        for h in range(3):
            for i in range(5):
                scores=[sum(q[h,i,d]*k[h,j,d] for d in range(4))/2-slopes[h]*abs(i-j) for j in range(5)]
                weights=[math.exp(s-max(scores)) for s in scores]
                for o in range(2):
                    expected[h,i,o]=sum(w*v[h,j,o] for j,w in enumerate(weights))/sum(weights)
        np.testing.assert_allclose(f(q,k,v,slopes),expected,atol=1e-14)
        np.testing.assert_allclose(f(q[:,::-1],k[:,::-1],v[:,::-1],slopes),expected[:,::-1],atol=1e-14)

    def test_window_attention_excludes_distant_changes(self):
        f=load('d36')['window_attention']; rng=np.random.default_rng(636)
        q,k=rng.normal(size=(2,8,4)); v=rng.normal(size=(8,3))
        scores=q@k.T/2
        allowed=np.abs(np.arange(8)[:,None]-np.arange(8)[None,:])<=2
        scores=np.where(allowed,scores,-np.inf)
        weights=np.exp(scores-scores.max(axis=1,keepdims=True)); weights/=weights.sum(axis=1,keepdims=True)
        out=f(q,k,v,2)
        np.testing.assert_allclose(out,weights@v,atol=1e-14)
        changed_k,changed_v=k.copy(),v.copy(); changed_k[3:]+=999; changed_v[3:]-=999
        np.testing.assert_array_equal(f(q,changed_k,changed_v,2)[0],out[0])
        np.testing.assert_array_equal(f(q,k,v,0),v)

    def test_depthwise_matches_equivalent_dense_kernel(self):
        f=load('d37')['depthwise_separable']; rng=np.random.default_rng(637)
        x=rng.normal(size=(2,3,4,5)); dw=rng.normal(size=(3,2,3)); pw=rng.normal(size=(4,3))
        dense=pw[:,:,None,None]*dw[None,:,:,:]
        expected=np.zeros((2,4,3,3))
        for b in range(2):
            for o in range(4):
                for y in range(3):
                    for z in range(3):
                        expected[b,o,y,z]=sum(x[b,c,y+u,z+v]*dense[o,c,u,v] for c in range(3) for u in range(2) for v in range(3))
        np.testing.assert_allclose(f(x,dw,pw),expected,atol=1e-14)
        order=[2,0,1]
        np.testing.assert_allclose(f(x[:,order],dw[order],pw[:,order]),expected,atol=1e-14)

    def test_gin_follows_node_relabeling_and_scalar_mlp(self):
        f=load('d38')['gin_layer']; rng=np.random.default_rng(638)
        a=rng.uniform(0,2,size=(5,5)); np.fill_diagonal(a,0)
        x=rng.normal(size=(5,3)); w1=rng.normal(size=(3,4)); b1=rng.normal(size=4)
        w2=rng.normal(size=(4,2)); b2=rng.normal(size=2); epsilon=-.4
        expected=np.empty((5,2))
        for i in range(5):
            aggregate=[(1+epsilon)*x[i,d]+sum(a[i,j]*x[j,d] for j in range(5)) for d in range(3)]
            hidden=[max(0,sum(aggregate[d]*w1[d,h] for d in range(3))+b1[h]) for h in range(4)]
            for o in range(2):
                expected[i,o]=sum(hidden[h]*w2[h,o] for h in range(4))+b2[o]
        np.testing.assert_allclose(f(a,x,w1,b1,w2,b2,epsilon),expected,atol=1e-14)
        order=[3,0,4,2,1]
        np.testing.assert_allclose(f(a[np.ix_(order,order)],x[order],w1,b1,w2,b2,epsilon),expected[order],atol=1e-14)

    def test_linear_attention_matches_explicit_kernel_not_softmax(self):
        f=load('d39')['linear_attention']; rng=np.random.default_rng(639)
        q=rng.normal(size=(4,3)); k=rng.normal(size=(7,3)); v=rng.normal(size=(7,2))
        phi=lambda x: np.array([[z+1 if z>0 else math.exp(z) for z in row] for row in x])
        kernel=phi(q)@phi(k).T
        expected=(kernel@v)/(kernel.sum(axis=1,keepdims=True)+1e-6)
        np.testing.assert_allclose(f(q,k,v),expected,atol=1e-14)
        order=rng.permutation(7)
        np.testing.assert_allclose(f(q,k[order],v[order]),expected,atol=1e-14)
        soft=np.exp(q@k.T/np.sqrt(3)); soft/=soft.sum(axis=1,keepdims=True)
        self.assertFalse(np.allclose(expected,soft@v))
        # The epsilon is additive, so a constant value is slightly attenuated.
        self.assertLess(f([[0]],[[0]],[[1]])[0,0],1)

    def test_graph_decoder_preserves_geometry_and_pair_complements(self):
        f=load('d40')['decode_graph']; rng=np.random.default_rng(640)
        x=rng.normal(size=(7,4)); rotation,_=np.linalg.qr(rng.normal(size=(4,4)))
        probabilities=f(x)
        np.testing.assert_allclose(f(x@rotation),probabilities,atol=1e-14)
        np.testing.assert_array_equal(probabilities,probabilities.T)
        self.assertTrue(np.all(np.diag(probabilities)>=.5))
        order=rng.permutation(7)
        np.testing.assert_allclose(f(x[order]),probabilities[np.ix_(order,order)])
        opposite=f(np.array([x[0],-x[0]]))
        self.assertAlmostEqual(opposite[0,0]+opposite[0,1],1)

    def test_load_balance_oracle_and_distribution_invariances(self):
        f=load('e21')['load_balance']; rng=np.random.default_rng(621)
        logits=rng.normal(size=(13,4))
        selected=[max(range(4),key=lambda e:row[e]) for row in logits]
        fractions=np.array([selected.count(e)/13 for e in range(4)])
        soft=[]
        for row in logits:
            weights=[math.exp(z-max(row)) for z in row]; soft.append([w/sum(weights) for w in weights])
        expected=np.mean(soft,axis=0); out=f(logits)
        np.testing.assert_allclose(out['fractions'],fractions)
        np.testing.assert_allclose(out['probabilities'],expected)
        self.assertAlmostEqual(out['loss'],4*sum(fractions*expected))
        self.assertAlmostEqual(f(np.repeat(logits,3,axis=0))['loss'],out['loss'])
        self.assertAlmostEqual(f(logits[:,[2,0,3,1]])['loss'],out['loss'])
        self.assertLess(f([[math.log(1.5),0],[math.log(1.5),0],[-1000,0]])['loss'],1)

    def test_expert_mixture_matches_scalar_dispatch_and_ignores_unused_outputs(self):
        f=load('e22')['mix_experts']; rng=np.random.default_rng(622)
        logits=rng.normal(size=(5,4)); logits[0]=0
        experts=rng.normal(size=(5,4,3)); result=f(logits,experts,2)
        expected=np.zeros((5,3)); changed=experts.copy()
        for n in range(5):
            indices=sorted(range(4),key=lambda e:(-logits[n,e],e))[:2]
            weights=[math.exp(logits[n,e]-logits[n,indices[0]]) for e in indices]
            weights=[w/sum(weights) for w in weights]
            np.testing.assert_array_equal(result['indices'][n],indices)
            np.testing.assert_allclose(result['weights'][n],weights)
            for o in range(3):
                expected[n,o]=sum(w*experts[n,e,o] for e,w in zip(indices,weights))
            for e in set(range(4))-set(indices):
                changed[n,e]+=1000
        np.testing.assert_allclose(result['output'],expected,atol=1e-14)
        np.testing.assert_array_equal(f(logits,changed,2)['output'],result['output'])
        self.assertIn(result['indices'].dtype.kind,'iu')

    def test_public_checks_reject_twelve_valid_input_misconceptions(self):
        def wrong_ppo(new,old,adv,clip_ratio=.2):
            return float(-np.mean(np.clip(np.exp(np.asarray(new)-old),1-clip_ratio,1+clip_ratio)*adv))

        def wrong_flow(a,b,t,pred):
            out=load('d33')['flow_matching'](a,b,t,pred)
            out['velocity']=-out['velocity']
            return out

        def wrong_ddim(x,noise,a,previous):
            out=load('d34')['ddim_step'](x,noise,a,previous)
            out['sample']=out['predicted_clean']
            return out

        def wrong_linear(q,k,v):
            q,k,v=np.asarray(q),np.asarray(k),np.asarray(v)
            phi=lambda x: np.where(x>0,x+1,np.exp(x))
            kernel=phi(q)@phi(k).T
            return (kernel@v)/np.maximum(kernel.sum(axis=1,keepdims=True),1e-6)

        def wrong_balance(x):
            out=load('e21')['load_balance'](x)
            out['loss']=len(out['probabilities'])*sum(out['probabilities']**2)
            return out

        def wrong_mix(logits,outputs,k):
            out=load('e22')['mix_experts'](logits,outputs,k)
            x=np.asarray(logits); weights=np.exp(x-x.max(axis=1,keepdims=True)); weights/=weights.sum(axis=1,keepdims=True)
            out['weights']=np.take_along_axis(weights,out['indices'],axis=1)
            selected=np.take_along_axis(np.asarray(outputs),out['indices'][:,:,None],axis=1)
            out['output']=np.sum(out['weights'][:,:,None]*selected,axis=1)
            return out

        mistakes={
            'm18':('ppo_loss',wrong_ppo),
            'm19':('dpo_loss',lambda pc,pr,rc,rr,beta=.1:load('m19')['dpo_loss'](pc,pr,np.zeros_like(rc),np.zeros_like(rr),beta)),
            'd33':('flow_matching',wrong_flow),
            'd34':('ddim_step',wrong_ddim),
            'd35':('alibi_attention',lambda q,k,v,s:load('d35')['alibi_attention'](q,k,v,np.zeros_like(s))),
            'd36':('window_attention',lambda q,k,v,r:load('d36')['window_attention'](q,k,v,len(q)-1)),
            'd37':('depthwise_separable',lambda x,dw,pw:load('d37')['depthwise_separable'](x,np.asarray(dw)[:,::-1,::-1],pw)),
            'd38':('gin_layer',lambda a,x,w1,b1,w2,b2,epsilon=0:np.maximum(load('d38')['gin_layer'](a,x,w1,b1,w2,b2,epsilon),0)),
            'd39':('linear_attention',wrong_linear),
            'd40':('decode_graph',lambda x:load('d40')['decode_graph'](x)*(1-np.eye(len(x)))),
            'e21':('load_balance',wrong_balance),
            'e22':('mix_experts',wrong_mix),
        }
        for prefix,(name,wrong) in mistakes.items():
            with self.subTest(activity=prefix),np.errstate(all='ignore'):
                rows=load(prefix,'tests_public.py')['run_tests']({name:wrong})
                self.assertTrue(any(not r['passed'] and r['message'].startswith('AssertionError:') and not r['name'].startswith('Reject') for r in rows),rows)

    def test_provenance_and_notices_cover_every_adaptation(self):
        manifest=json.loads((ROOT/'content/platform-batch-03-provenance.json').read_text(encoding='utf-8'))
        self.assertEqual(len(manifest['items']),12)
        self.assertEqual(sum(item['public_cases'] for item in manifest['items']),144)
        for item in manifest['items']:
            source=(BASE/item['folder']/'solution.py').read_text(encoding='utf-8')
            notice=(ROOT/item['notice']).read_text(encoding='utf-8')
            self.assertIn(manifest['revision'],item['upstream_url'])
            for value in ['Copyright (c) 2024 duoan','Copyright (c) 2024 kiren','Permission is hereby granted','THE SOFTWARE IS PROVIDED',item['upstream_url'],item['changes']]:
                self.assertIn(value,source)
                self.assertIn(value,notice)
            self.assertEqual(len(item['upstream_sha256']),64)


if __name__ == '__main__':
    unittest.main()
