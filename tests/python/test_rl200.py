"""Independent numerical checks for the rollout and policy lessons d70..d79."""
import pathlib
import unittest
import numpy as np

BASE = pathlib.Path(__file__).resolve().parents[2] / 'content/problems'


def load(identifier, name):
    folder, = BASE.glob(identifier+'-*')
    namespace = {}
    exec((folder/'solution.py').read_text(encoding='utf-8'), namespace)
    return namespace[name]


class ReinforcementLearningLessons(unittest.TestCase):
    def test_returns_match_explicit_discounted_sums_and_episode_boundaries(self):
        f = load('d70', 'episode_returns')
        rng = np.random.default_rng(20070)
        r = rng.normal(size=19)
        done = np.zeros(19); done[[3, 8, 15]] = 1
        for gamma in [0., .3, .95, 1.]:
            expected = []
            for start in range(len(r)):
                terminal = np.flatnonzero(done[start:])
                stop = start+int(terminal[0])+1 if terminal.size else len(r)
                expected.append(np.dot(gamma**np.arange(stop-start),r[start:stop]) +
                                (0 if terminal.size else gamma**(stop-start)*4.25))
            np.testing.assert_allclose(f(r,done,gamma,4.25), expected)
        for bad in [[], [True], [np.nan]]:
            with self.assertRaises(ValueError): f(bad,[0],.9)

    def test_gae_endpoints_and_intermediate_exponential_residual_sum(self):
        f = load('d71', 'generalized_advantages')
        returns = load('d70', 'episode_returns')
        rng = np.random.default_rng(20071)
        r = rng.normal(size=13); v = rng.normal(size=14)
        done = np.zeros(13); done[[4,9]]=1; gamma=.83
        np.testing.assert_allclose(f(r,v,done,gamma,1)['targets'], returns(r,done,gamma,v[-1]))
        delta = r+gamma*(1-done)*v[1:]-v[:-1]
        np.testing.assert_allclose(f(r,v,done,gamma,0)['advantages'],delta)
        lam=.43; expected=[]
        for t in range(len(r)):
            later=np.flatnonzero(done[t:])
            end=t+int(later[0])+1 if later.size else len(r)
            expected.append(np.dot((gamma*lam)**np.arange(end-t),delta[t:end]))
        np.testing.assert_allclose(f(r,v,done,gamma,lam)['advantages'],expected)
        huge=f([1],[1e30,0],[1],.9,1)
        np.testing.assert_array_equal(huge['targets'],[1.])
        local=f([1],[1e30,1e30],[0],1,0)
        np.testing.assert_array_equal(local['advantages'],[1.])

    def test_td_targets_ignore_current_prediction_and_respect_batch_permutation(self):
        f=load('d72','td_value_targets')
        r=np.array([1.,-3,4]); v=np.array([9.,2,-5]); nxt=np.array([2.,30,-8]); done=np.array([0,1,0])
        first=f(r,v,nxt,done,.75); changed=f(r,v+8,nxt,done,.75)
        np.testing.assert_array_equal(first['targets'],[2.5,-3,-2])
        np.testing.assert_array_equal(changed['targets'],first['targets'])
        np.testing.assert_allclose(changed['errors'],first['errors']-8)
        order=np.array([2,0,1]); permuted=f(r[order],v[order],nxt[order],done[order],.75)
        for key in first: np.testing.assert_allclose(permuted[key],first[key][order])

    def test_double_q_selects_online_and_evaluates_target_including_ties(self):
        f=load('d73','double_q_targets')
        online=np.array([[5.,1,0],[2,2,1],[-8,-4,-7]])
        target=np.array([[1.,9,8],[3,50,8],[99,-6,4]])
        out=f([0,1,2],online,target,[0,0,1],.5)
        np.testing.assert_array_equal(out['actions'],[0,0,1])
        self.assertTrue(np.issubdtype(out['actions'].dtype,np.integer))
        np.testing.assert_array_equal(out['targets'],[.5,2.5,2])
        self.assertFalse(np.allclose(out['targets'],np.array([0,1,2])+.5*target.max(axis=1)))

    def test_categorical_projection_preserves_mass_and_clipped_mean(self):
        f=load('d74','project_value_distribution')
        rng=np.random.default_rng(20074)
        for count in [2,5,51]:
            z=np.linspace(-5,8,count); p=rng.dirichlet(np.ones(count))
            np.testing.assert_allclose(f(p,z,0,1,0),p,atol=1e-13)
            for reward,discount,terminal in [(.7,.93,0),(-20,.3,0),(4.1,.8,1)]:
                result=f(p,z,reward,discount,terminal)
                self.assertGreaterEqual(result.min(),0)
                self.assertAlmostEqual(result.sum(),1,places=12)
                moved=np.clip(reward+discount*(1-terminal)*z,z[0],z[-1])
                self.assertAlmostEqual(result@z,p@moved,places=11)
        np.testing.assert_array_equal(f([.1,.2,.7],[-1,0,1],0,0,0),[0,1,0])
        almost_uniform=np.array([0.,1e-8,2.009e-8,3.018e-8])
        np.testing.assert_array_equal(f([0,0,1,0],almost_uniform,0,1,0),[0,0,1,0])

    def test_gumbel_choices_match_categorical_frequencies_and_logit_shift(self):
        f=load('d75','gumbel_choice')
        rng=np.random.default_rng(20075); p=np.array([.1,.3,.6]); logits=np.log(p)
        uniforms=rng.uniform(.000001,.999999,size=(6000,3))
        chosen=np.array([f(logits,u) for u in uniforms])
        np.testing.assert_allclose(np.bincount(chosen,minlength=3)/len(chosen),p,atol=.02,rtol=0)
        for u,choice in zip(uniforms[:20],chosen[:20]): self.assertEqual(f(logits+100,u),choice)
        self.assertEqual(f([0],[np.nextafter(0.,1.)]),0)
        self.assertEqual(f([1e30,1e30],[.01,.99]),1)

    def test_policy_score_gradient_matches_loss_finite_differences(self):
        f=load('d76','policy_score_gradient')
        rng=np.random.default_rng(20076); x=rng.normal(size=(3,4)); actions=np.array([0,2,3]); adv=np.array([2.,-1.,0.])
        result=f(x,actions,adv); eps=1e-5
        for i in range(3):
            for j in range(4):
                step=np.zeros_like(x); step[i,j]=eps
                finite=(f(x+step,actions,adv)['loss']-f(x-step,actions,adv)['loss'])/(2*eps)
                self.assertAlmostEqual(result['gradient'][i,j],finite,places=8)
        np.testing.assert_allclose(result['gradient'].sum(axis=1),0,atol=1e-14)
        shifted=f(x+np.array([100,-1000,3])[:,None],actions,adv)
        self.assertAlmostEqual(shifted['loss'],result['loss'],places=12)
        np.testing.assert_allclose(shifted['gradient'],result['gradient'],atol=1e-13)

    def test_polyak_repeated_update_has_geometric_error_and_no_alias(self):
        f=load('d77','polyak_update'); initial=np.array([2.,-5]); online=np.array([10.,3]); target=initial.copy(); rate=.17
        for _ in range(11): target=f(target,online,rate)
        np.testing.assert_allclose(target,online+(1-rate)**11*(initial-online))
        np.testing.assert_array_equal(initial,[2,-5]); np.testing.assert_array_equal(online,[10,3])
        for rate in [0,1]:
            out=f(initial,online,rate)
            self.assertFalse(np.shares_memory(out,initial)); self.assertFalse(np.shares_memory(out,online))

    def test_potential_shaping_telescopes_with_terminal_and_cutoff_boundaries(self):
        f=load('d78','shape_rewards'); rng=np.random.default_rng(20078)
        r=rng.normal(size=12); potential=rng.normal(size=13); g=.91; weights=g**np.arange(12)
        for terminal in [0,1]:
            done=np.zeros(12); done[-1]=terminal
            shaped=f(r,potential[:-1],potential[1:],done,g)
            expected=-potential[0]+(1-terminal)*g**12*potential[-1]
            self.assertAlmostEqual((shaped-r)@weights,expected,places=12)

    def test_n_step_reduces_to_one_step_and_full_bootstrapped_return(self):
        f=load('d79','n_step_targets'); td=load('d72','td_value_targets'); full=load('d70','episode_returns')
        rng=np.random.default_rng(20079); r=rng.normal(size=17); v=rng.normal(size=18); done=np.zeros(17); done[[3,9]]=1; g=.87
        np.testing.assert_allclose(f(r,v,done,g,1),td(r,v[:-1],v[1:],done,g)['targets'])
        np.testing.assert_allclose(f(r,v,done,g,256),full(r,done,g,v[-1]))
        for horizon in [2,5,8]:
            expected=[]
            for t in range(len(r)):
                end=min(t+horizon,len(r)); flags=np.flatnonzero(done[t:end]); terminal=bool(flags.size)
                if terminal: end=t+int(flags[0])+1
                expected.append(np.dot(g**np.arange(end-t),r[t:end])+(0 if terminal else g**(end-t)*v[end]))
            np.testing.assert_allclose(f(r,v,done,g,horizon),expected)


if __name__ == '__main__': unittest.main()
