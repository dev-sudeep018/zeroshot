"""Independent numerical identities for the forty foundation lessons m20..m59."""
import itertools
import math
from pathlib import Path
import unittest

import numpy as np

BASE = Path(__file__).resolve().parents[2] / 'content/problems'


def function(number, name):
    folder, = BASE.glob(f'm{number}-*')
    namespace = {}
    exec((folder / 'solution.py').read_text(encoding='utf8'), namespace)
    return namespace[name]


class Foundation200Tests(unittest.TestCase):
    def test_bayes_sequential_evidence_and_entropy_chain_rule(self):
        update = function(20, 'bayes_update')
        entropy = function(21, 'categorical_entropy')
        prior = np.array([.2, .3, .5]); a = np.array([.4, .8, .1]); b = np.array([.3, .2, .9])
        first = update(prior, a); second = update(first['posterior'], b); joint = update(prior, a*b)
        np.testing.assert_allclose(second['posterior'], joint['posterior'])
        self.assertAlmostEqual(first['evidence']*second['evidence'], joint['evidence'])
        self.assertAlmostEqual(entropy([.1, .3, .6]), entropy([.4, .6])+.4*entropy([.25, .75]))
        self.assertAlmostEqual(entropy([.25]*4), 2*entropy([.5, .5]))

    def test_divergences_and_joint_information_identities(self):
        kl = function(22, 'relative_entropy'); js = function(23, 'js_divergence'); mi = function(24, 'mutual_information')
        p = np.array([.1, .3, .6]); q = np.array([.5, .2, .3])
        cross_entropy = -sum(float(a)*math.log(float(b)) for a,b in zip(p,q))
        entropy = -sum(float(a)*math.log(float(a)) for a in p)
        self.assertAlmostEqual(kl(p,q), cross_entropy-entropy)
        self.assertNotAlmostEqual(kl(p,q), kl(q,p))
        self.assertAlmostEqual(js(p,q), js(q,p)); self.assertGreaterEqual(js(p,q), 0); self.assertLessEqual(js(p,q), math.log(2))
        self.assertTrue(math.isfinite(js([5e-324,1],[0,1])))
        table = np.array([[.1,.2],[.3,.4]])
        h = lambda x: -sum(float(z)*math.log(float(z)) for z in np.ravel(x) if z)
        self.assertAlmostEqual(mi(table), h(table.sum(axis=0))+h(table.sum(axis=1))-h(table))
        self.assertAlmostEqual(mi(table.T), mi(table))
        self.assertTrue(math.isfinite(mi([[1e-300,0],[0,1]])))

    def test_quantiles_affine_equivariance_and_order(self):
        f = function(25, 'empirical_quantiles'); x = np.array([7.,-2,4,4,10]); q = np.linspace(0,1,17)
        out = f(x,q)
        self.assertTrue(np.all(np.diff(out)>=0)); self.assertEqual(out[0], min(x)); self.assertEqual(out[-1], max(x))
        np.testing.assert_allclose(f(3*x+11,q),3*out+11)
        np.testing.assert_allclose(f(x,q[::-1]),out[::-1])
        np.testing.assert_allclose(f(-x,q),-f(x,1-q))

    def test_correlations_against_rank_and_covariance_oracles(self):
        pearson = function(26, 'pearson_correlation'); spearman = function(27, 'spearman_correlation')
        x = np.array([4.,1,1,3,7,2]); y = np.array([2.,8,4,1,6,6])
        self.assertAlmostEqual(pearson(x,y),np.corrcoef(x,y)[0,1])
        def ranks(values):
            return [1+sum(other<v for other in values)+(sum(other==v for other in values)-1)/2 for v in values]
        self.assertAlmostEqual(spearman(x,y),np.corrcoef(ranks(x),ranks(y))[0,1])
        self.assertAlmostEqual(spearman(x**3,y),spearman(x,y))
        self.assertAlmostEqual(spearman(-x,y),-spearman(x,y))

    def test_robust_scaling_train_only_and_whitening_identity(self):
        robust = function(28, 'robust_scale'); whiten = function(29, 'whiten_covariance')
        train=np.array([[0.,3],[2,3],[4,3],[6,3]]); values=np.array([[3.,5],[99,3]])
        out=robust(train,values)
        np.testing.assert_allclose(out['center'],[3,3]); np.testing.assert_allclose(out['scale'],[3,1])
        np.testing.assert_allclose(robust(train,values[:1])['values'],out['values'][:1])
        a=np.array([[2.,1,0],[1,3,1],[0,1,2]]); covariance=a@a.T
        for epsilon in [.1,1,7]:
            w=whiten(covariance,epsilon)
            np.testing.assert_allclose(w,w.T,atol=1e-12)
            np.testing.assert_allclose(w@(covariance+epsilon*np.eye(3))@w.T,np.eye(3),atol=1e-12)

    def test_lowrank_known_spectrum_and_pseudoinverse_identities(self):
        lowrank=function(30,'low_rank_approximation'); pinv=function(31,'svd_pseudoinverse')
        rotation=np.array([[.6,-.8],[.8,.6]]); a=rotation@np.diag([5.,2.])
        out=lowrank(a,1); np.testing.assert_allclose(out['matrix'],rotation@np.diag([5.,0]),atol=1e-12)
        self.assertAlmostEqual(out['squared_error'],4)
        a=np.array([[1.,2,3],[2,4,6],[1,0,1],[3,2,5]]); p=pinv(a)
        np.testing.assert_allclose(a@p@a,a,atol=1e-12); np.testing.assert_allclose(p@a@p,p,atol=1e-12)
        np.testing.assert_allclose(a@p,(a@p).T,atol=1e-12); np.testing.assert_allclose(p@a,(p@a).T,atol=1e-12)
        with self.assertRaises(ValueError): pinv([[1e-320]],0)

    def test_power_iteration_exact_eigenspace_and_qr_reconstruction(self):
        power=function(32,'power_iteration'); qr=function(33,'gram_schmidt')
        a=np.array([[3.,1],[1,3]]); out=power(a,[1,0],30)
        np.testing.assert_allclose(out['vector'],np.ones(2)/np.sqrt(2),atol=1e-8); self.assertAlmostEqual(out['rayleigh'],4)
        np.testing.assert_allclose(power(3*a,[1,0],5)['vector'],power(a,[1,0],5)['vector'])
        matrix=np.array([[1.,2,3],[3,1,2],[2,4,1],[0,1,5]])
        out=qr(matrix); np.testing.assert_allclose(out['q']@out['r'],matrix,atol=1e-12)
        np.testing.assert_allclose(out['q'].T@out['q'],np.eye(3),atol=1e-12)
        self.assertTrue(np.all(np.diag(out['r'])>0))

    def test_cholesky_and_forward_solve_recover_constructed_inputs(self):
        chol=function(34,'cholesky_lower'); solve=function(35,'forward_substitution')
        rng=np.random.default_rng(734); lower=np.tril(rng.normal(size=(8,8))); lower[np.diag_indices(8)]=rng.uniform(.5,2,size=8)
        np.testing.assert_allclose(chol(lower@lower.T),lower,atol=1e-10)
        x=rng.normal(size=8); np.testing.assert_allclose(solve(lower,lower@x),x,atol=1e-10)
        extreme=np.eye(24)*2e-12+np.tril(np.full((24,24),1e6),-1)
        with self.assertRaises(ValueError): solve(extreme,np.ones(24))

    def test_logistic_and_hinge_gradients_by_finite_differences(self):
        x=np.array([[1.,2],[-2,1],[.5,-1]]); w=np.array([.3,-.2]); b=.17; eps=1e-6
        for number,name,y,loss in [
            (36,'logistic_gradient',np.array([0.,1,1]),lambda scores,labels: sum(math.log1p(math.exp(s))-v*s for s,v in zip(scores,labels))/len(labels)),
            (39,'hinge_gradient',np.array([-1.,1,1]),lambda scores,labels: sum(max(0,1-v*s) for s,v in zip(scores,labels))/len(labels)),
        ]:
            f=function(number,name); out=f(x,y,w,b)
            for j in range(2):
                offset=np.eye(2)[j]*eps
                numeric=(loss(x@(w+offset)+b,y)-loss(x@(w-offset)+b,y))/(2*eps)
                self.assertAlmostEqual(out['weights'][j],numeric,places=7)
            numeric=(loss(x@w+b+eps,y)-loss(x@w+b-eps,y))/(2*eps)
            self.assertAlmostEqual(out['bias'],numeric,places=7)

    def test_l1_proximal_optimality_and_perceptron_order(self):
        prox=function(37,'soft_threshold'); perceptron=function(38,'perceptron_pass')
        values=np.linspace(-3,3,21); threshold=.7; optimum=prox(values,threshold)
        def objective(z): return .5*(z-values)**2+threshold*np.abs(z)
        for displacement in [-.5,-.01,.01,.5]: self.assertTrue(np.all(objective(optimum)<=objective(optimum+displacement)+1e-12))
        first=perceptron([[0],[0]],[1,-1],[0],0); reverse=perceptron([[0],[0]],[-1,1],[0],0)
        self.assertEqual(first['bias'],0); self.assertEqual(reverse['bias'],0); self.assertEqual(first['updates'],2)
        first=perceptron([[1],[2]],[1,1],[0],0); reverse=perceptron([[2],[1]],[1,1],[0],0)
        self.assertEqual(first['weights'][0],1); self.assertEqual(reverse['weights'][0],2)

    def test_stump_partition_oracle_and_adjacent_floats(self):
        f=function(40,'gini_split'); x=[4,0,2,2,5,1]; labels=[1,0,0,1,1,0]
        out=f(x,labels); candidates=[]
        unique=sorted(set(x))
        for lo,hi in zip(unique,unique[1:]):
            threshold=(lo+hi)/2; groups=[[y for v,y in zip(x,labels) if (v<=threshold)==side] for side in (True,False)]
            score=sum((len(g)-sum(g.count(c)**2 for c in (0,1))/len(g))/len(labels) for g in groups)
            candidates.append((score,threshold))
        expected=min(candidates); self.assertAlmostEqual(out['impurity'],expected[0]); self.assertEqual(out['threshold'],expected[1])
        lo=np.nextafter(1.,2.); hi=np.nextafter(lo,2.); result=f([lo,hi],[0,1])
        self.assertLess(result['threshold'],hi); self.assertGreaterEqual(result['threshold'],lo); self.assertEqual(result['gain'],.5)

    def test_centroids_minimize_fixed_assignment_error(self):
        f=function(41,'update_centroids'); rng=np.random.default_rng(741); x=rng.normal(size=(12,3)); labels=np.arange(12)%3; previous=rng.normal(size=(4,3))
        updated=f(x,labels,previous)
        for k in range(3):
            rows=x[labels==k]; self.assertLessEqual(np.sum((rows-updated[k])**2),np.sum((rows-previous[k])**2))
            np.testing.assert_allclose(np.sum(rows-updated[k],axis=0),0,atol=1e-12)
        np.testing.assert_array_equal(updated[3],previous[3])

    def test_silhouette_scalar_distance_oracle_and_density(self):
        silhouette=function(42,'silhouette_scores'); density=function(43,'density_neighborhoods')
        points=[[0,0],[1,0],[4,3],[5,3],[10,0]]; labels=[0,0,1,1,2]; expected=[]
        distance=lambda a,b: math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))
        for i,p in enumerate(points):
            own=[distance(p,q) for j,q in enumerate(points) if j!=i and labels[j]==labels[i]]
            if not own: expected.append(0); continue
            a=sum(own)/len(own); competitors=[]
            for group in set(labels)-{labels[i]}:
                ds=[distance(p,q) for j,q in enumerate(points) if labels[j]==group]; competitors.append(sum(ds)/len(ds))
            b=min(competitors); expected.append((b-a)/max(a,b))
        np.testing.assert_allclose(silhouette(points,labels)['scores'],expected)
        out=density(points,1,2); reference=np.array([[distance(a,b)<=1 for b in points] for a in points])
        np.testing.assert_array_equal(out['neighbors'],reference); np.testing.assert_array_equal(out['core'],reference.sum(axis=1)>=2)
        np.testing.assert_array_equal(density([[0],[1e-300]],0,2)['neighbors'],np.eye(2,dtype=bool))
        tiny=np.array([[0.],[0.],[1e-300],[1e-300]])
        np.testing.assert_allclose(silhouette(tiny,[0,0,1,1])['scores'],np.ones(4))

    def test_em_likelihood_improvement_and_component_permutation(self):
        f=function(44,'gaussian_em_step'); values=np.array([-3.,-2,-1,1,2,4]); weights=np.array([.4,.6]); means=np.array([-1.,1.]); variances=np.array([3.,2.])
        first=f(values,weights,means,variances); second=f(values,first['weights'],first['means'],first['variances'])
        self.assertGreaterEqual(second['log_likelihood']+1e-12,first['log_likelihood'])
        permuted=f(values,weights[::-1],means[::-1],variances[::-1])
        for key in ['weights','means','variances']: np.testing.assert_allclose(permuted[key],first[key][::-1])
        self.assertAlmostEqual(sum(first['weights']),1)

    def test_single_linkage_merge_matches_original_member_distances(self):
        f=function(45,'single_linkage_merge'); points=[0.,1,4,10,12]; groups=[{i} for i in range(5)]
        distances=np.abs(np.subtract.outer(points,points))
        while len(groups)>1:
            result=f(distances); i,j=result['pair']; groups[i]|=groups[j]; groups.pop(j)
            expected=np.zeros((len(groups),len(groups)))
            for a,g in enumerate(groups):
                for b,h in enumerate(groups):
                    if a!=b: expected[a,b]=min(abs(points[u]-points[v]) for u in g for v in h)
            np.testing.assert_allclose(result['distances'],expected); distances=result['distances']

    def test_naive_bayes_counts_and_empirical_cdf(self):
        nb=function(46,'fit_multinomial_nb'); cdf=function(47,'empirical_cdf')
        counts=np.array([[1,3,0],[0,2,4],[5,0,1]]); labels=np.array([0,1,0]); result=nb(counts,labels,2,.5)
        np.testing.assert_allclose(np.exp(result['class_log_prior']),[2/3,1/3])
        np.testing.assert_allclose(np.exp(result['feature_log_probability']),[[6.5/11.5,3.5/11.5,1.5/11.5],[.5/7.5,2.5/7.5,4.5/7.5]])
        x=[2,1,1,7,-2]; queries=[-3,1,0,7,2]
        np.testing.assert_allclose(cdf(x,queries),[sum(v<=q for v in x)/len(x) for q in queries])

    def test_resampling_statistics_use_supplied_draws(self):
        bootstrap=function(48,'bootstrap_means'); permutation=function(49,'permutation_mean_test')
        x=[1.,4,7]; draws=list(itertools.product(range(3),repeat=3)); means=[sum(x[i] for i in draw)/3 for draw in draws]
        result=bootstrap(x,draws); np.testing.assert_allclose(result['means'],means)
        expected=math.sqrt(sum((v-sum(means)/len(means))**2 for v in means)/(len(means)-1)); self.assertAlmostEqual(result['standard_error'],expected)
        values=[0.,1,3,4]; orders=list(itertools.permutations(range(4))); out=permutation(values,2,orders)
        null=[(values[a]+values[b]-values[c]-values[d])/2 for a,b,c,d in orders]
        np.testing.assert_allclose(out['null'],null); self.assertAlmostEqual(out['p_value'],(1+sum(abs(v)>=3 for v in null))/25)

    def test_paired_statistic_and_binomial_normalization(self):
        paired=function(50,'paired_t_statistic'); binomial=function(51,'binomial_log_likelihood')
        before=np.array([20.,1,30,2]); difference=np.array([1.,4,-2,3]); out=paired(before,before+difference)
        mean=sum(difference)/4; variance=sum((v-mean)**2 for v in difference)/3
        self.assertAlmostEqual(out['t'],mean/math.sqrt(variance/4)); self.assertEqual(out['degrees_of_freedom'],3)
        for n,p in [(1,.2),(5,.7),(12,.05)]:
            self.assertAlmostEqual(sum(math.exp(binomial(k,n,p)) for k in range(n+1)),1)
            for k in range(n+1): self.assertAlmostEqual(math.exp(binomial(k,n,p)),math.comb(n,k)*p**k*(1-p)**(n-k))

    def test_conjugate_updates_compose_and_predictive_joint_is_exchangeable(self):
        beta=function(52,'beta_update'); sequence=function(53,'categorical_predictive_sequence')
        first=beta(2,3,4,1); sequential=beta(first['alpha'],first['beta'],2,5); combined=beta(2,3,6,6)
        self.assertEqual(sequential,combined)
        a=[.5,2.,3.]; observations=[2,0,2,1,2]; result=sequence(a,observations)
        counts=[observations.count(c) for c in range(3)]
        expected=math.lgamma(sum(a))-math.lgamma(sum(a)+len(observations))+sum(math.lgamma(v+n)-math.lgamma(v) for v,n in zip(a,counts))
        self.assertAlmostEqual(result['log_probability'],expected)
        self.assertAlmostEqual(sequence(a,observations[::-1])['log_probability'],expected)

    def test_mahalanobis_change_of_coordinates_and_transport_invariances(self):
        mahalanobis=function(54,'mahalanobis_squared'); transport=function(55,'empirical_wasserstein')
        points=np.array([[1.,2],[3,-1],[0,4]]); center=np.array([.2,-.3]); transform=np.array([[2.,1],[0,3]]); precision=transform@transform.T
        expected=np.sum(((points-center)@transform)**2,axis=1)
        np.testing.assert_allclose(mahalanobis(points,center,precision),expected)
        a=np.array([0.,3,1,5]); b=np.array([-1.,2,2,6]); self.assertAlmostEqual(transport(a,b),np.abs(np.sort(a)-np.sort(b)).mean())
        self.assertAlmostEqual(transport(a,b),transport(b,a)); self.assertAlmostEqual(transport(a+12,b+12),transport(a,b))
        self.assertAlmostEqual(transport(np.repeat(a,3),b),transport(a,b))

    def test_rbf_gram_and_implicit_centering_equal_explicit_features(self):
        rbf=function(56,'rbf_kernel'); center=function(57,'center_kernel'); rng=np.random.default_rng(756); x=rng.normal(size=(7,3))
        k=rbf(x,x,.7); np.testing.assert_allclose(k,k.T); np.testing.assert_allclose(np.diag(k),1)
        self.assertGreaterEqual(np.linalg.eigvalsh(k).min(),-1e-12)
        np.testing.assert_allclose(rbf(x+20,x+20,.7),k,atol=1e-12)
        gram=x@x.T; centered=x-x.mean(axis=0)
        np.testing.assert_allclose(center(gram),centered@centered.T,atol=1e-12)
        np.testing.assert_allclose(center(gram).sum(axis=1),0,atol=1e-12)

    def test_isotonic_against_exhaustive_contiguous_block_partitions(self):
        f=function(58,'isotonic_fit'); values=np.array([3.,0,4,1,2]); weights=np.array([1.,2,1,3,2]); candidates=[]
        # Enumerate every contiguous partition independently of the PAVA stack.
        for cut_bits in itertools.product([False,True],repeat=len(values)-1):
            boundaries=[0]+[i+1 for i,cut in enumerate(cut_bits) if cut]+[len(values)]; fitted=np.empty(len(values)); block_means=[]
            for start,end in zip(boundaries,boundaries[1:]):
                mean=sum(values[start:end]*weights[start:end])/sum(weights[start:end]); fitted[start:end]=mean; block_means.append(mean)
            if all(a<=b for a,b in zip(block_means,block_means[1:])): candidates.append((sum(weights*(fitted-values)**2),fitted.copy()))
        expected=min(candidates,key=lambda item:item[0])[1]; np.testing.assert_allclose(f(values,weights),expected)

    def test_pinball_gradient_and_empirical_quantile_optimum(self):
        f=function(59,'pinball_loss'); target=np.array([-2.,0,1,4]); prediction=np.array([-1.,2,0,3]); q=.8; eps=1e-6; out=f(target,prediction,q)
        for i in range(4):
            step=np.eye(4)[i]*eps; numeric=(f(target,prediction+step,q)['loss']-f(target,prediction-step,q)['loss'])/(2*eps)
            self.assertAlmostEqual(out['gradient'][i],numeric,places=8)
        # A median minimizes total absolute deviation, hence median pinball loss.
        best=f(target,np.full(4,.5),.5)['loss']
        for value in np.linspace(-3,5,33): self.assertLessEqual(best,f(target,np.full(4,value),.5)['loss']+1e-12)


if __name__ == '__main__':
    unittest.main()
