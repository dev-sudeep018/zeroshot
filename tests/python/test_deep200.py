"""Independent numerical and combinatorial oracles for D41-D69."""
from pathlib import Path
import itertools
import math
import runpy
import unittest
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
CACHE = {}

def fn(id, name):
    if id not in CACHE:
        CACHE[id] = runpy.run_path(str(next((ROOT/'content/problems').glob(id+'-*/solution.py'))))
    return CACHE[id][name]


def derivative(objective, value, step=1e-5):
    result=np.zeros_like(value,dtype=float)
    for index in np.ndindex(value.shape):
        left=value.copy(); right=value.copy()
        left[index]-=step; right[index]+=step
        result[index]=(objective(right)-objective(left))/(2*step)
    return result


class Deep200Oracles(unittest.TestCase):
    def test_conditioning_token_and_batch_independence(self):
        f=fn('d41','conditional_gate')
        x=np.array([[[1.,2.,7.],[3.,4.,9.]],[[8.,6.,4.],[0.,1.,2.]]])
        scale=np.array([[1.,2.,3.],[4.,5.,6.]])
        shift=np.array([[2.,1.,0.],[3.,2.,1.]])
        gate=np.array([[1.,0.,-1.],[.5,1.,2.]])
        actual=f(x,scale,shift,gate)
        expected=np.empty_like(x)
        for b,t in itertools.product(range(2),range(2)):
            row=x[b,t]; m=sum(row)/3; var=sum((v-m)**2 for v in row)/3
            for d in range(3): expected[b,t,d]=gate[b,d]*(scale[b,d]*(row[d]-m)/math.sqrt(var+1e-6)+shift[b,d])
        np.testing.assert_allclose(actual,expected)
        np.testing.assert_allclose(f(x+100,scale,shift,gate),actual)

    def test_grouped_heads_match_explicit_expansion(self):
        rng=np.random.default_rng(41); q=rng.normal(size=(6,3,2)); k=rng.normal(size=(2,4,2)); v=rng.normal(size=(2,4,3))
        actual=fn('d42','grouped_attention')(q,k,v)
        expected=[]
        for head in range(6):
            scores=q[head]@np.repeat(k,3,axis=0)[head].T/math.sqrt(2)
            p=np.exp(scores-scores.max(axis=1,keepdims=True)); p/=p.sum(axis=1,keepdims=True)
            expected.append(p@np.repeat(v,3,axis=0)[head])
        np.testing.assert_allclose(actual,expected)

    def test_differential_attention_constant_value_row_sum(self):
        rng=np.random.default_rng(42); q=rng.normal(size=(3,2)); k=rng.normal(size=(4,2))
        v=np.tile([3.,-4.],(4,1))
        f=fn('d43','differential_attention')
        for coefficient in [-2.,0.,.3,1.,2.]:
            np.testing.assert_allclose(f(q,k,-q,k,v,coefficient),np.tile((1-coefficient)*np.array([3.,-4.]),(3,1)),atol=1e-12)

    def test_graph_attention_permutation_and_absent_edges(self):
        f=fn('d44','graph_attention')
        x=np.array([[2.,-1.],[3.,4.],[-2.,1.]])
        adj=np.array([[1.,1.,0.],[0.,0.,1.],[0.,0.,0.]])
        w=np.array([[1.,2.],[-1.,1.]]); a=np.array([.1,-.2,.5,-.3]); order=[2,0,1]
        result=f(x,adj,w,a)
        np.testing.assert_allclose(f(x[order],adj[np.ix_(order,order)],w,a),result[order])
        changed=x.copy(); changed[2]+=100
        np.testing.assert_allclose(f(changed,adj,w,a)[0],result[0])
        np.testing.assert_array_equal(result[2],np.zeros(2))

    def test_edge_message_graph_permutation_and_rectification(self):
        rng=np.random.default_rng(45); f=fn('d45','edge_messages')
        x=rng.normal(size=(3,2)); a=np.array([[1.,2.,0.],[0.,0.,1.],[3.,0.,0.]])
        e=rng.normal(size=(3,3,2)); wm=rng.normal(size=(6,3)); wu=rng.normal(size=(5,2)); order=[1,2,0]
        result=f(x,a,e,wm,wu)
        np.testing.assert_allclose(f(x[order],a[np.ix_(order,order)],e[order][:,order],wm,wu),result[order])
        self.assertTrue(np.all(result>=0))

    def test_state_space_unrolling_geometric_series(self):
        f=fn('d46','state_space_step'); h=np.array([[[2.]]]); outputs=[]
        for step in range(4):
            result=f([[3]],h,[[-math.log(2)]],[[1]],[[2]],[[1]])
            h=result['state']; outputs.append(result['output'][0,0])
        expected=[2*(2*.5**n+3*sum(.5**j for j in range(n))) for n in range(1,5)]
        np.testing.assert_allclose(outputs,expected)

    def test_sharded_mlp_matches_unsharded_and_permuted_shards(self):
        rng=np.random.default_rng(47); f=fn('d47','sharded_mlp')
        x=rng.normal(size=(2,3)); up=rng.normal(size=(3,3,2)); down=rng.normal(size=(3,2,4))
        z=x@np.concatenate(up,axis=1)
        gelu=np.array([[v*.5*(1+math.erf(v/math.sqrt(2))) for v in row] for row in z])
        expected=gelu@np.concatenate(down,axis=0)
        np.testing.assert_allclose(f(x,up,down),expected,atol=1e-12)
        np.testing.assert_allclose(f(x,up[::-1],down[::-1]),expected,atol=1e-12)

    def test_recurrence_continuation_and_gate_limits(self):
        f=fn('d48','recurrent_states'); x=np.array([[.2],[.7],[-.1],[.4]])
        allstates=f(x,[.3],[[.8]],[[.4]],[.1])
        first=f(x[:2],[.3],[[.8]],[[.4]],[.1])
        rest=f(x[2:],first[-1],[[.8]],[[.4]],[.1])
        np.testing.assert_allclose(np.concatenate([first,rest]),allstates)
        lstm=fn('d49','lstm_step')
        result=lstm([[3]],[[1000]],[[-1000]],[[1000]],[[.6]])
        np.testing.assert_allclose(result['cell'],[[math.tanh(.6)]])
        np.testing.assert_allclose(result['hidden'],[[math.tanh(math.tanh(.6))]])
        gru=fn('d50','gru_step')
        np.testing.assert_allclose(gru([[99]],[[-1000]],[[1000]],[[.2]],[[.4]]),[[math.tanh(.6)]])

    def test_residual_gradients_with_finite_differences(self):
        f=fn('d51','residual_backward')
        x=np.array([[.7,-.3],[1.2,.8]]); w=np.array([[.8,-.5],[.2,.6]]); g=np.array([[2.,-.4],[.5,1.1]])
        def loss(a,b): return float(np.sum((a+np.maximum(a@b,0))*g))
        actual=f(x,w,g)
        np.testing.assert_allclose(actual['input'],derivative(lambda v:loss(v,w),x),atol=1e-8)
        np.testing.assert_allclose(actual['weights'],derivative(lambda v:loss(x,v),w),atol=1e-8)

    def test_average_pool_adjoint_identity(self):
        rng=np.random.default_rng(52); f=fn('d52','average_pool_backward')
        for shape,k,s in [((5,7),3,2),((4,5),2,1),((3,6),1,3)]:
            x=rng.normal(size=shape); oh=1+(shape[0]-k)//s; ow=1+(shape[1]-k)//s
            g=rng.normal(size=(oh,ow)); pooled=np.array([[x[i*s:i*s+k,j*s:j*s+k].mean() for j in range(ow)] for i in range(oh)])
            self.assertAlmostEqual(float(np.sum(pooled*g)),float(np.sum(x*f(g,shape,k,s))),places=11)

    def test_convolution_gradients_with_finite_differences(self):
        rng=np.random.default_rng(53); f=fn('d53','convolution_backward')
        x=rng.normal(size=(3,4)); k=rng.normal(size=(2,3)); g=rng.normal(size=(2,2))
        def loss(a,b): return sum(float(np.sum(a[i:i+2,j:j+3]*b))*g[i,j] for i,j in np.ndindex(g.shape))
        actual=f(x,k,g)
        np.testing.assert_allclose(actual['image'],derivative(lambda v:loss(v,k),x),atol=1e-8)
        np.testing.assert_allclose(actual['kernel'],derivative(lambda v:loss(x,v),k),atol=1e-8)

    def test_transposed_convolution_is_matrix_adjoint(self):
        f=fn('d54','transposed_convolution'); k=np.array([.2,-.7,.4]); g=np.array([1.2,-.3,2.])
        for stride in [1,2,4]:
            n=(len(g)-1)*stride+len(k); matrix=np.zeros((len(g),n))
            for i in range(len(g)): matrix[i,i*stride:i*stride+len(k)]=k
            np.testing.assert_allclose(f(g,k,stride),matrix.T@g)

    def test_group_normalization_statistics(self):
        rng=np.random.default_rng(55); f=fn('d55','group_normalize'); x=rng.normal(size=(2,6,4))
        for groups in [1,2,3,6]:
            result=f(x,groups,1e-6).reshape(2,groups,-1)
            np.testing.assert_allclose(result.mean(-1),0,atol=1e-15)
            raw=x.reshape(2,groups,-1); var=raw.var(-1)
            np.testing.assert_allclose(result.var(-1),var/(var+1e-6))
            np.testing.assert_allclose(f(x+5,groups),f(x,groups),atol=1e-14)

    def test_ctc_exhaustive_alignment_enumeration(self):
        rng=np.random.default_rng(56); f=fn('d56','ctc_probability')
        for t in range(1,5):
            p=rng.uniform(.1,1,size=(t,3)); p/=p.sum(1,keepdims=True)
            totals={}
            for path in itertools.product(range(3),repeat=t):
                collapsed=tuple(symbol for symbol,_ in itertools.groupby(path) if symbol!=0)
                totals[collapsed]=totals.get(collapsed,0)+math.prod(p[i,symbol] for i,symbol in enumerate(path))
            for target in [(),(1,),(2,),(1,1),(1,2),(2,1),(2,2)]:
                self.assertAlmostEqual(f(p,list(target)),totals.get(target,0),places=13)

    def test_gaussian_kl_and_reparameterization_gradients(self):
        kl=fn('d57','gaussian_kl'); m=np.array([[.2,-.3],[1.,2.]]); logv=np.log(np.array([[.5,2.],[3.,.2]]))
        expected=np.array([sum(.5*(mu*mu+var-1-math.log(var)) for mu,var in zip(mrow,np.exp(vrow))) for mrow,vrow in zip(m,logv)])
        np.testing.assert_allclose(kl(m,logv),expected)
        f=fn('d58','reparameterization_backward'); noise=np.array([[.8,-.2],[.4,1.1]]); g=np.array([[2.,-1.],[.5,.9]])
        def loss(a,b): return float(np.sum((a+np.exp(b/2)*noise)*g))
        actual=f(m,logv,noise,g)
        np.testing.assert_allclose(actual['mean'],derivative(lambda v:loss(v,logv),m),atol=1e-8)
        np.testing.assert_allclose(actual['log_variance'],derivative(lambda v:loss(m,v),logv),atol=1e-8)

    def test_diffusion_posterior_gaussian_precision_product(self):
        f=fn('d59','diffusion_posterior'); x0=np.array([.2,-1.]); xt=np.array([2.,.4])
        for b,p in [(.1,.8),(.3,.4),(.9,.2)]:
            # q(previous|clean) times likelihood q(current|previous).
            prior_variance=1-p; prior_mean=math.sqrt(p)*x0; alpha=1-b
            variance=1/(1/prior_variance+alpha/b)
            mean=variance*(prior_mean/prior_variance+math.sqrt(alpha)*xt/b)
            actual=f(x0,xt,b,p)
            np.testing.assert_allclose(actual['mean'],mean)
            self.assertAlmostEqual(actual['variance'],variance)

    def test_adversarial_losses_direct_probability_oracle(self):
        f=fn('d60','adversarial_losses'); real=np.array([-.7,.4,1.2]); fake=np.array([.5,-.3])
        pr=1/(1+np.exp(-real)); pf=1/(1+np.exp(-fake)); result=f(real,fake)
        self.assertAlmostEqual(result['discriminator'],float(-np.log(pr).mean()-np.log(1-pf).mean()))
        self.assertAlmostEqual(result['generator'],float(-np.log(pf).mean()))

    def test_triplet_and_dice_geometric_identities(self):
        triplet=fn('d61','triplet_margin'); rng=np.random.default_rng(61)
        a,p,n=rng.normal(size=(3,4)),rng.normal(size=(3,4)),rng.normal(size=(3,4))
        q,_=np.linalg.qr(rng.normal(size=(4,4)))
        self.assertAlmostEqual(triplet(a,p,n),triplet(a@q,p@q,n@q),places=12)
        dice=fn('d63','soft_dice_loss'); probs=np.array([[.2,.7,.8],[.4,.1,.3]]); target=np.array([[0,1,1],[1,0,0]])
        np.testing.assert_allclose(dice(probs,target),dice(probs[:,::-1],target[:,::-1]))
        np.testing.assert_allclose(dice(target,target),np.zeros(2))

    def test_contrastive_positive_average_and_shift_stability(self):
        f=fn('d62','supervised_contrastive'); scores=np.array([[0.,.4,-.3],[.2,0.,.7],[-.1,.5,0.]])
        expected=[]
        for i in range(3):
            row=[scores[i,j] for j in range(3) if j!=i]; denom=sum(math.exp(v) for v in row)
            expected.append(sum(-math.log(math.exp(v)/denom) for v in row)/2)
        self.assertAlmostEqual(f(scores,[1,1,1]),sum(expected)/3)
        self.assertAlmostEqual(f(np.full((4,4),1e30),[0,0,1,1]),math.log(3))

    def test_total_variation_gradient_finite_difference(self):
        f=fn('d64','total_variation'); x=np.array([[.2,1.7,-.3],[2.,.5,1.]])
        def loss(v): return float(np.abs(np.diff(v,axis=0)).sum()+np.abs(np.diff(v,axis=1)).sum())
        result=f(x)
        self.assertAlmostEqual(result['loss'],loss(x))
        np.testing.assert_allclose(result['gradient'],derivative(loss,x),atol=1e-8)
        self.assertAlmostEqual(float(result['gradient'].sum()),0)

    def test_softmax_jvp_finite_difference_and_hutchinson_full_signs(self):
        jvp=fn('d65','softmax_jvp'); x=np.array([[.2,-.5,1.1]]); direction=np.array([[.4,.7,-.2]])
        def sm(v):
            p=np.exp(v-v.max(1,keepdims=True)); return p/p.sum(1,keepdims=True)
        numeric=(sm(x+1e-5*direction)-sm(x-1e-5*direction))/(2e-5)
        np.testing.assert_allclose(jvp(sm(x),direction),numeric,atol=1e-9)
        a=np.array([[2.,-1.,3.],[4.,-2.,7.],[.5,3.,1.]])
        probes=np.array(list(itertools.product([-1.,1.],repeat=3)))
        self.assertAlmostEqual(fn('d66','trace_probes')(a,probes)['mean'],float(np.trace(a)))

    def test_attention_all_operand_gradients(self):
        rng=np.random.default_rng(67); f=fn('d67','attention_backward')
        q=rng.normal(size=(2,3)); k=rng.normal(size=(4,3)); v=rng.normal(size=(4,2)); g=rng.normal(size=(2,2))
        def loss(a,b,c):
            scores=a@b.T/math.sqrt(3); p=np.exp(scores-scores.max(1,keepdims=True)); p/=p.sum(1,keepdims=True)
            return float(np.sum((p@c)*g))
        actual=f(q,k,v,g)
        for key,base,objective in [('queries',q,lambda z:loss(z,k,v)),('keys',k,lambda z:loss(q,z,v)),('values',v,lambda z:loss(q,k,z))]:
            np.testing.assert_allclose(actual[key],derivative(objective,base),atol=1e-8)

    def test_chain_partition_and_viterbi_exhaustive_paths(self):
        rng=np.random.default_rng(68); partition=fn('d68','chain_log_partition'); viterbi=fn('d69','chain_viterbi')
        for t in range(1,5):
            e=rng.integers(-3,4,size=(t,3)).astype(float); a=rng.integers(-2,3,size=(3,3)).astype(float); start=rng.integers(-2,3,size=3); end=rng.integers(-2,3,size=3)
            scored=[]
            for path in itertools.product(range(3),repeat=t):
                score=start[path[0]]+end[path[-1]]+sum(e[i,s] for i,s in enumerate(path))+sum(a[path[i-1],path[i]] for i in range(1,t))
                scored.append((float(score),path))
            logz=math.log(sum(math.exp(score) for score,_ in scored))
            self.assertAlmostEqual(partition(e,a,start,end),logz,places=12)
            best=min(scored,key=lambda z:(-z[0],z[1])); actual=viterbi(e,a,start,end)
            self.assertEqual(actual['score'],best[0]); self.assertEqual(tuple(actual['path']),best[1]); self.assertTrue(np.issubdtype(actual['path'].dtype,np.integer))

if __name__ == '__main__':
    unittest.main()
