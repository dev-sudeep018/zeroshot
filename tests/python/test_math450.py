"""Independent oracles and invariants for m60..m159; no generated answers."""
import itertools
import json
import math
from pathlib import Path
import unittest

import numpy as np


BASE = Path(__file__).resolve().parents[2] / 'content/problems'


def function(number):
    folder, = BASE.glob(f'm{number}-*')
    lesson = json.loads((folder / 'lesson.json').read_text(encoding='utf8'))
    namespace = {}
    exec((folder / 'solution.py').read_text(encoding='utf8'), namespace)
    return namespace[lesson['signature'].split('(')[0]]


class Foundation450Tests(unittest.TestCase):
    def test_calibration_masking_and_grid_conservation(self):
        x=np.arange(15.).reshape(3,5)
        out=function(60)(x,[1,-1,2,0,.5],[0,2,1,3,0],[-2]*5,[6]*5)
        raw=np.array([[v*g+o for v,g,o in zip(row,[1,-1,2,0,.5],[0,2,1,3,0])] for row in x])
        np.testing.assert_allclose(out['values'],np.minimum(6,np.maximum(-2,raw)))
        np.testing.assert_array_equal(out['clipped'],out['values']!=raw)
        mask=x%3==0; masked=function(61)(x,mask,-8)
        expected=[np.mean(x[:,i][mask[:,i]]) if mask[:,i].any() else -8 for i in range(5)]
        np.testing.assert_allclose(masked['mean'],expected)
        for br,bc in [(1,2),(2,4),(9,9)]: self.assertEqual(function(62)(x,br,bc).sum(),x.sum())
        coords=[[0,1],[0,1],[1,2],[1,0]]; values=[2,-3,5,7]
        acc=function(63)(2,3,coords,values); self.assertEqual(acc['sum'].sum(),sum(values)); self.assertEqual(acc['count'].sum(),4)
        rev=function(63)(2,3,coords[::-1],values[::-1]); np.testing.assert_array_equal(acc['sum'],rev['sum'])

    def test_triangle_packing_conditionals_diagonal_and_rectangles(self):
        x=np.arange(16.).reshape(4,4); sym=x+x.T; packed=function(64)(sym)
        self.assertEqual(len(packed['packed']),10); np.testing.assert_array_equal(packed['reconstructed'],sym)
        counts=np.array([[1.,3,4],[0,0,0],[6,2,5]])
        out=function(65)(counts); np.testing.assert_allclose(out['row_mass'][:,None]*out['conditional'],counts/counts.sum())
        profile=function(66)(x[:3]); self.assertEqual(profile['count'].sum(),12)
        self.assertAlmostEqual(np.dot(profile['mean'],profile['count']),x[:3].sum())
        queries=[[0,1,3,4],[2,0,4,2],[1,1,1,4],[0,0,4,4]]
        np.testing.assert_allclose(function(67)(x,queries),[x[t:b,l:r].sum() for t,l,b,r in queries])

    def test_tiles_expected_counts_components_and_plateaus(self):
        ids=np.array([0,6,7,17,34]); loc=function(68)(5,7,2,3,ids)
        decoded=loc['tile']*[2,3]+loc['local']; np.testing.assert_array_equal(decoded[:,0]*7+decoded[:,1],ids)
        counts=np.array([[2.,8,1],[5,3,7],[0,0,0]]); out=function(69)(counts)
        np.testing.assert_allclose(out['expected'].sum(axis=0),counts.sum(axis=0)); np.testing.assert_allclose(out['expected'].sum(axis=1),counts.sum(axis=1)); np.testing.assert_allclose(out['residual'].sum(axis=0),0,atol=1e-12)
        mask=np.array([[1,1,0,1],[1,0,0,1],[0,1,1,1]],dtype=bool); regions=function(70)(mask)
        np.testing.assert_array_equal(regions['sizes'],[3,5]); np.testing.assert_array_equal(regions['perimeters'],[8,12]); self.assertEqual(sum(regions['sizes']),int(mask.sum()))
        np.testing.assert_array_equal(function(71)([0,2,2,2,0,3,3,0]),[2,5]); self.assertEqual(len(function(71)([2,2,1,0])),0)

    def test_irregular_rates_smoothing_and_temporal_leakage(self):
        times=np.array([0.,.5,2,5]); positions=3*times-7; out=function(72)(times,positions)
        np.testing.assert_allclose(out['velocity'],3); self.assertAlmostEqual(np.dot(out['velocity'],np.diff(times)),positions[-1]-positions[0])
        x=np.array([2.,-1,5,7,0]); smoothed=function(73)(x,2)
        for i in range(len(x)): self.assertAlmostEqual(smoothed['mean'][i],sum(x[j] for j in range(len(x)) if abs(i-j)<=2)/smoothed['count'][i])
        f=function(74); original=f([2,5,9],.3,1); changed=f([2,5,99],.3,1)
        np.testing.assert_allclose(original['forecast'],changed['forecast']); self.assertNotEqual(original['level'],changed['level'])
        for lag in [1,2,4]: np.testing.assert_allclose(function(75)(x,lag)['reconstructed'],x)

    def test_signal_lags_crossings_integral_and_interpolation(self):
        x=np.array([2.,-3,4,1]); biased=function(76)(x,3,'biased'); overlap=function(76)(x,3,'overlap')
        np.testing.assert_allclose(biased['value']*len(x),overlap['value']*overlap['count']); self.assertEqual(biased['value'][0],np.dot(x,x)/len(x))
        np.testing.assert_array_equal(function(77)([0,-2,0,0,3,0,1,-1,0]),[[1,4],[6,7]])
        t=np.array([-2.,0,1,4]); y=2*t+3; out=function(78)(t,y)
        np.testing.assert_allclose(out['area'],(t[1:]**2+3*t[1:])-(t[:-1]**2+3*t[:-1])); self.assertEqual(out['cumulative'][0],0)
        q=np.array([-3,-1,.5,2,5]); np.testing.assert_allclose(function(79)(t,y,q),2*np.clip(q,-2,4)+3)

    def test_robust_statistics_and_multiplicative_growth(self):
        x=np.array([9.,1,4,8,2,99]); out=function(80)(x,2); np.testing.assert_allclose(out['retained'],[4,8]); self.assertEqual(out['mean'],6)
        out=function(81)([1,1,1,2],3); self.assertEqual(out['mad'],0); np.testing.assert_array_equal(out['outlier'],[False,False,False,True])
        out=function(82)([0,1,2,3,4],0); np.testing.assert_allclose(out['quartiles'],[1,3]); np.testing.assert_array_equal(out['tail'],[-1,0,0,0,1])
        factors=np.array([1.5,.5,2,1.2]); growth=function(83)(factors)
        np.testing.assert_allclose(growth['cumulative'],np.cumprod(factors)); self.assertAlmostEqual(growth['geometric_mean']**4,np.prod(factors))
        self.assertGreater(function(83)([1e-6]*50)['cumulative'][-1],0)

    def test_rates_energy_dispersion_shape_and_density(self):
        out=function(84)([10,20,40],3); self.assertAlmostEqual(out['mean_speed']*out['total_time'],9)
        x=np.array([-2.,1,4,0]); crest=function(85)(x); self.assertAlmostEqual(function(85)(-3*x)['crest'],crest['crest'])
        self.assertAlmostEqual(function(86)([1,3,5])['cv'],function(86)([10,30,50])['cv'])
        shape=function(87)(x); shifted=function(87)(3*x+7); self.assertAlmostEqual(shape['skewness'],shifted['skewness']); self.assertAlmostEqual(shape['excess_kurtosis'],shifted['excess_kurtosis'])
        out=function(88)([0,1,2,5],[1,2,3,4],[0,2,5]); np.testing.assert_allclose(out['mass'],[.3,.7]); self.assertAlmostEqual(np.dot(out['density'],[2,3]),1)

    def test_histograms_inequality_modes_and_jackknife(self):
        out=function(89)([0,2,4],[3,5],[-1,1,3,5]); np.testing.assert_allclose(out,[1.5,4,2.5]); self.assertEqual(out.sum(),8)
        x=np.array([0.,2,3,9]); gini=function(90)(x)['gini']; pair=np.abs(x[:,None]-x[None,:]).sum()/(2*len(x)*x.sum()); self.assertAlmostEqual(gini,pair)
        modes=function(91)([4,1,4,1,7]); np.testing.assert_array_equal(modes['modes'],[1,4]); self.assertEqual(modes['frequency'],2)
        out=function(92)(x); np.testing.assert_allclose(out['estimates'],[np.delete(x,i).mean() for i in range(len(x))]); self.assertAlmostEqual(out['jackknife_se'],np.std(x,ddof=1)/np.sqrt(len(x)))

    def test_variance_partition_weights_and_score_intervals(self):
        a=np.array([1.,3,8]); b=np.array([7.,9]); out=function(93)([len(a),len(b)],[np.var(a,ddof=1),np.var(b,ddof=1)])
        self.assertAlmostEqual(out['variance']*out['degrees_freedom'],np.sum((a-a.mean())**2)+np.sum((b-b.mean())**2))
        out=function(94)([1,3,8,7,9],[0,0,0,1,1],2); self.assertAlmostEqual(out['total'],out['within']+out['between'])
        weights=function(95)([1,2,4]); scaled=function(95)([3,6,12]); self.assertAlmostEqual(weights['effective_size'],scaled['effective_size']); self.assertAlmostEqual(function(95)([2]*5)['effective_size'],5)
        f=function(96); np.testing.assert_allclose(f(3,10,1.96),1-f(7,10,1.96)[::-1]); self.assertGreater(f(0,10,1.96)[1],0); self.assertLess(f(10,10,1.96)[0],1)

    def test_forecast_metrics_splits_and_nearest_segment(self):
        a=np.array([0.,2,-3]); p=np.array([0.,4,1]); f=function(97); np.testing.assert_allclose(f(a,p)['per_item'],f(p,a)['per_item']); np.testing.assert_allclose(f(a,p)['per_item'],f(5*a,5*p)['per_item'])
        f=function(98); base=f([1,3,7,8],[9,10],[8,12],1); scaled=f([3,9,21,24],[27,30],[24,36],1); self.assertAlmostEqual(base['mase'],scaled['mase'])
        splits=function(99)(15,5,3,2); self.assertTrue(np.all(splits[:,1]==splits[:,2])); self.assertTrue(np.all(splits[:,3]-splits[:,2]==3)); self.assertTrue(np.all(splits[:,3]<=15))
        f=function(100); x=f([3,4],[0,0],[5,0]); self.assertAlmostEqual(x['squared_distance'],16); rev=f([3,4],[5,0],[0,0]); self.assertAlmostEqual(x['parameter']+rev['parameter'],1); np.testing.assert_allclose(x['point'],rev['point'])

    def test_planar_area_projection_bounds_rotation_and_polar(self):
        f=function(101); self.assertEqual(f([0,0],[3,0],[0,4])['signed_area'],6); self.assertEqual(f([0,0],[0,4],[3,0])['orientation'],-1)
        p=np.array([[0.,0],[3,0],[3,4],[0,4]]); f=function(102); self.assertEqual(f(p)['perimeter'],14); self.assertEqual(f(p)['signed_area'],-f(p[::-1])['signed_area'])
        out=function(103)([7,3],[2,1],-4); self.assertAlmostEqual(np.dot(out['foot'],[2,1])-4,0)
        bounds=function(104)(p+5); np.testing.assert_allclose(bounds['lengths'],[3,4]); self.assertEqual(bounds['volume'],12)
        pivot=np.array([1.,2]); f=function(105); np.testing.assert_allclose(f(f(p,pivot,.7),pivot,-.7),p,atol=1e-12)
        polar=function(106)(p+[-1,2]); reconstructed=np.column_stack([polar['radius']*np.cos(polar['angle']),polar['radius']*np.sin(polar['angle'])]); np.testing.assert_allclose(reconstructed,p+[-1,2],atol=1e-12)

    def test_barycentric_intersection_reflection_clipping_and_path(self):
        vertices=np.array([[1.,1],[5,1],[2,4]]); q=np.array([2.,2]); out=function(107)(q,vertices); self.assertAlmostEqual(sum(out['weights']),1); np.testing.assert_allclose(out['weights']@vertices,q)
        out=function(108)([0,0],[4,2],[1,3],[3,-1]); t,u=out['parameters']; np.testing.assert_allclose([0,0]+t*np.array([4,2]),[1,3]+u*np.array([2,-4]))
        f=function(109); p=np.array([[1.,5],[-3,2]]); np.testing.assert_allclose(f(f(p,[2,1],3),[2,1],3),p,atol=1e-12)
        clipped=function(110)([-2,2],[6,2],[0,0],[4,4]); np.testing.assert_allclose(clipped['points'],[[0,2],[4,2]]); self.assertTrue(clipped['visible'])
        np.testing.assert_allclose(function(111)([[0,0],[0,0],[3,0],[3,4]],[0,1,3,5,7]),[[0,0],[1,0],[3,0],[3,2],[3,4]])

    def test_vector_geometry_polygon_and_triangle_identities(self):
        v=np.array([3.,4,5]); out=function(112)(v,[2,-1,3]); self.assertAlmostEqual(np.dot(out['parallel'],out['perpendicular']),0); self.assertAlmostEqual(sum(out['squared_lengths']),np.dot(v,v))
        vertices=np.array([[1.,0,2],[3,0,2],[1,4,2]]); plane=function(113)(*vertices); np.testing.assert_allclose(vertices@plane['normal']+plane['offset'],0); self.assertAlmostEqual(np.linalg.norm(plane['normal']),1)
        axis=np.array([1.,2,3]); rotated=function(114)(v,axis,.8); self.assertAlmostEqual(np.linalg.norm(rotated),np.linalg.norm(v)); self.assertAlmostEqual(np.dot(rotated,axis),np.dot(v,axis))
        polygon=[[0,0],[4,0],[4,1],[1,1],[1,4],[0,4]]; queries=[[.5,3],[3,.5],[2,2],[1,2],[0,0]]
        f=function(115); expected=[True,True,False,True,True]; np.testing.assert_array_equal(f(queries,polygon),expected); np.testing.assert_array_equal(f(queries,polygon[::-1]),expected)
        triangle=function(116)([3,4,5]); self.assertAlmostEqual(sum(triangle['angles']),math.pi); self.assertAlmostEqual(triangle['area'],6)

    def test_mass_moments_interval_union_and_disk_overlap(self):
        p=np.array([[0.,0],[2,0],[1,4]]); weights=np.array([1.,2,3]); f=function(117); out=f(p,weights); shifted=f(p+7,weights)
        np.testing.assert_allclose(out['inertia'],shifted['inertia']); self.assertAlmostEqual(out['polar'],np.trace(out['inertia'])); self.assertAlmostEqual(out['polar'],sum(w*np.dot(point-out['center'],point-out['center']) for point,w in zip(p,weights)))
        out=function(118)([[0,2],[1,4],[4,5],[8,9]]); np.testing.assert_allclose(out['intervals'],[[0,5],[8,9]]); self.assertEqual(out['length'],6)
        f=function(119); self.assertAlmostEqual(f(2,3,4),f(3,2,4)); self.assertAlmostEqual(f(4,6,8),4*f(2,3,4)); self.assertAlmostEqual(f(4,1,1),math.pi)

    def test_event_algebra_convolution_and_sampling_counts(self):
        p=np.array([.1,.2,.3,.4]); a=np.array([1,1,0,0],dtype=bool); b=np.array([0,1,1,0],dtype=bool); out=function(120)(p,a,b)
        self.assertAlmostEqual(out['union']+out['intersection'],out['a']+out['b']); self.assertAlmostEqual(out['a_given_b']*out['b'],out['intersection'])
        out=function(121)([.2,.8],-1,[.5,.1,.4],3); self.assertAlmostEqual(sum(out['probabilities']),1); self.assertAlmostEqual(np.dot(np.arange(len(out['probabilities']))+out['start'],out['probabilities']),-.2+3.9)
        n,k,d=7,3,4; counts={i:0 for i in range(d+1)}
        for subset in itertools.combinations(range(n),d): counts[sum(i<k for i in subset)]+=1
        out=function(122)(n,k,d)
        for value,prob in zip(out['support'],out['probabilities']): self.assertAlmostEqual(prob,counts[value]/math.comb(n,d))
        rates=[.2,.6,.4]; out=function(123)(rates); self.assertAlmostEqual(sum(out['first'])+out['none'],1); self.assertAlmostEqual(out['none'],math.prod(1-p for p in rates))

    def test_poisson_cdf_distinct_and_collision_oracles(self):
        out=function(124)(2.5,[0,1,2,3,4]); p=out['probabilities']; np.testing.assert_allclose(p[1:]/p[:-1],2.5/np.arange(1,5)); self.assertAlmostEqual(p[0],math.exp(-2.5))
        out=function(125)([0,.3,0,.7],[0,.3,.999]); np.testing.assert_array_equal(out['indices'],[1,3,3])
        weights=[.2,.3,.5]; expected=0.
        for draw in itertools.product(range(3),repeat=3): expected+=len(set(draw))*math.prod(weights[i] for i in draw)
        self.assertAlmostEqual(function(126)(weights,3)['expected'],expected)
        outcomes=list(itertools.product(range(4),repeat=3)); expected=sum(len(set(t))<3 for t in outcomes)/len(outcomes)
        self.assertAlmostEqual(function(127)(4,3),expected)

    def test_joint_regions_mixtures_and_markov_absorption(self):
        out=function(128)(.5,.5,.5,.25,.25,.25,.125); self.assertAlmostEqual(out['exactly_one'],3/8); self.assertAlmostEqual(out['exactly_two'],3/8); self.assertAlmostEqual(out['union']+out['none'],1)
        table=np.array([[.1,.2],[.3,.4]]); out=function(129)(table,[True,True]); np.testing.assert_allclose(out['rows'],table.sum(axis=1)); self.assertAlmostEqual(out['event'],1)
        mixture=function(130)([.25,.75],[1,5],[2,3]); second=.25*(2+1)+.75*(3+25); self.assertAlmostEqual(mixture['variance'],second-mixture['mean']**2)
        transition=np.array([[.7,.3],[.2,.8]]); initial=np.array([.3,.7]); trajectory=function(131)(initial,transition,5); np.testing.assert_allclose(trajectory[-1],initial@np.linalg.matrix_power(transition,5)); np.testing.assert_allclose(trajectory.sum(axis=1),1)
        q=np.array([[.5,.2],[.1,.6]]); out=function(132)(initial,q,5); self.assertAlmostEqual(sum(out['absorbed'])+out['survival'][-1],1); np.testing.assert_allclose(out['remaining'],initial@np.linalg.matrix_power(q,5))

    def test_count_distributions_dice_and_combination_unranking(self):
        rates=[.1,.4,.8,.6]; distribution=np.zeros(5)
        for outcomes in itertools.product([0,1],repeat=4): distribution[sum(outcomes)]+=math.prod(p if x else 1-p for x,p in zip(outcomes,rates))
        np.testing.assert_allclose(function(133)(rates)['counts'],distribution)
        sums=[sum(x) for x in itertools.product(range(1,5),repeat=3)]; out=function(134)(3,4)
        self.assertEqual(out['counts'],[sums.count(n) for n in out['sums']]); self.assertEqual(sum(out['counts']),4**3)
        f=function(135)
        for rank,subset in enumerate(itertools.combinations(range(7),3)): self.assertEqual(f(7,3,rank),list(subset))

    def test_permutation_parity_paths_derangements_and_occupancy(self):
        for perm in itertools.permutations(range(4)):
            out=function(136)(perm); matrix=np.eye(4)[list(perm)]; self.assertEqual(-1 if out['parity']=='odd' else 1,round(np.linalg.det(matrix)))
        self.assertEqual(function(137)(np.zeros((5,7),dtype=bool)),math.comb(10,4)); self.assertEqual(function(137)([[False,True],[False,False]]),1)
        f=function(138)
        for n in range(7): self.assertEqual(f(n)['count'],sum(all(i!=v for i,v in enumerate(p)) for p in itertools.permutations(range(n))))
        empty=[3-len(set(draw)) for draw in itertools.product(range(3),repeat=4)]; out=function(139)(3,4)
        self.assertAlmostEqual(out['mean'],np.mean(empty)); self.assertAlmostEqual(out['variance'],np.var(empty))

    def test_polynomials_roots_newton_and_simpson(self):
        c=np.array([2.,-1,3,-4]); x=np.array([-2.,0,.5,3]); out=function(140)(c,x)
        np.testing.assert_allclose(out['value'],np.polyval(c,x)); np.testing.assert_allclose(out['slope'],np.polyval(np.polyder(c),x))
        out=function(141)(c,[-2,0],[0,3]); anti=np.polyint(c); np.testing.assert_allclose(out['antiderivative'],anti); self.assertAlmostEqual(sum(out['areas']),np.polyval(anti,3)-np.polyval(anti,-2))
        root=function(142)([1,0,-2],0,2,20); self.assertLessEqual(root['bracket'][0],np.sqrt(2)); self.assertGreaterEqual(root['bracket'][1],np.sqrt(2)); self.assertLessEqual(np.ptp(root['bracket']),2/2**20)
        trace=function(143)(7,1,8); self.assertAlmostEqual(trace[-1],np.sqrt(7)); np.testing.assert_allclose(function(143)(0,8,4),[8,4,2,1,.5])
        x=np.linspace(-2,3,11); self.assertAlmostEqual(function(144)(2*x**3-x+4,.5),(3**4/2-3**2/2+12)-((-2)**4/2-(-2)**2/2-8))

    def test_bisection_tiny_coefficients_keep_sign_information(self):
        f = function(142)
        result = f([1e-200, 0], -1, 2, 20)
        self.assertLessEqual(result['bracket'][0], 0)
        self.assertGreaterEqual(result['bracket'][1], 0)
        self.assertLessEqual(np.ptp(result['bracket']), 3 / 2**20)
        self.assertLessEqual(abs(result['root']), 3 / 2**21)
        with self.assertRaises(ValueError):
            f([1e-200, 0, 1e-200], -1, 1, 3)

    def test_interpolation_cooling_secant_and_linear_solvers(self):
        nodes=np.array([-2.,1,3]); queries=np.array([-.5,0,2,4]); poly=lambda x:2*x*x-3*x+1
        np.testing.assert_allclose(function(145)(nodes,poly(nodes),queries),poly(queries))
        np.testing.assert_allclose(function(146)(100,20,.3,.5,6),20+80*.85**np.arange(7))
        trace=function(147)([1,0,-3],1,2,6); self.assertAlmostEqual(trace[-1],np.sqrt(3),places=10)
        with self.assertRaises(ValueError): function(147)([1,0,1],-1,1,1)
        a=np.array([[5.,1,-1],[2,6,1],[1,-1,4]]); b=np.array([3.,9,2]); solved=np.linalg.solve(a,b)
        np.testing.assert_allclose(function(148)(a,b,[0,0,0],40)['solution'],solved,atol=1e-10)
        pivoted=np.array([[0.,2,1],[3,1,-1],[1,-1,4]]); np.testing.assert_allclose(pivoted@function(149)(pivoted,b),b,atol=1e-10)

    def test_model_scores_ols_r_squared_and_loss_gradient(self):
        features=np.array([[0.,1],[1,0]]); priors=np.array([.3,.7]); probs=np.array([[.2,.8],[.6,.1]])
        out=function(150)(features,priors,probs); oracle=np.array([[math.log(priors[k]*math.prod(probs[k,j] if x else 1-probs[k,j] for j,x in enumerate(row))) for k in range(2)] for row in features]); np.testing.assert_allclose(out,oracle)
        x=np.array([-2.,0,1,4,5]); y=np.array([1.,3,2,8,7]); fit=function(151)(x,y)
        self.assertAlmostEqual(sum(fit['residuals']),0); self.assertAlmostEqual(np.dot(fit['residuals'],x),0); np.testing.assert_allclose([fit['slope'],fit['intercept']],np.linalg.lstsq(np.column_stack([x,np.ones(len(x))]),y,rcond=None)[0])
        score=function(152)(y,np.full(len(y),y.mean())); self.assertAlmostEqual(score['r_squared'],0)
        self.assertEqual(function(152)([1e-200,2e-200],[1e-200,2e-200])['r_squared'],1)
        self.assertAlmostEqual(function(152)([1e-200,2e-200],[1.5e-200,1.5e-200])['r_squared'],0)
        p=np.array([-3.,.2,4]); y=np.array([0.,0,1]); f=function(153); out=f(p,y,.5)
        for j in range(3):
            delta=np.eye(3)[j]*1e-5; estimate=(f(p+delta,y,.5)['loss']-f(p-delta,y,.5)['loss'])/2e-5; self.assertAlmostEqual(out['gradient'][j],estimate)

    def test_agreement_balancing_centroids_bins_and_ridge(self):
        a=[0,0,1,2,2]; b=[0,1,1,2,0]; f=function(154); self.assertEqual(f(a,b,3),f(b,a,3)); self.assertAlmostEqual(f([0,1],[1,0],2)['kappa'],-1)
        labels=np.array([0,0,0,1,2,2]); out=function(155)(labels,3)
        for k in range(3): self.assertAlmostEqual(out['weights'][labels==k].sum(),2)
        train=np.array([[0.,1],[2,1],[8,5],[10,5]]); out=function(156)(train,[0,0,1,1],[[5,3],[9,5]],2); np.testing.assert_allclose(out['centroids'],[[1,1],[9,5]]); np.testing.assert_array_equal(out['predictions'],[0,1])
        out=function(157)([-1,2],[3,5,9],[-5,-1,0,2,8]); np.testing.assert_array_equal(out['indices'],[0,1,1,2,2]); np.testing.assert_allclose(out['predictions'],[3,5,5,9,9])
        x=np.array([[1.,2],[3,1],[2,-1]]); y=np.array([1.,4,3]); w=np.array([2.,-1]); lam=.7; objective=lambda v:.5*np.sum((x@v-y)**2)+.5*lam*np.dot(v,v)
        out=function(158)(x,y,w,1,lam); self.assertEqual(out[0],w[0]); self.assertLessEqual(objective(out),objective(w)); self.assertAlmostEqual((x.T@(x@out-y)+lam*out)[1],0)
        values=np.array([1.,4,7,9]); weights=np.array([1.,3,2,1]); median=function(159)(values,weights); costs=[np.dot(weights,np.abs(values-v)) for v in values]; self.assertEqual(np.dot(weights,np.abs(values-median)),min(costs))

    def test_large_exact_count_evaluators_reject_off_by_one(self):
        helpers=(BASE.parent/'evaluator_helpers.py').read_text(encoding='utf8')
        for number in (134,137,138):
            folder,=BASE.glob(f'm{number}-*'); lesson=json.loads((folder/'lesson.json').read_text(encoding='utf8')); name=lesson['signature'].split('(')[0]
            evaluator={}; exec(helpers+'\n'+(folder/'tests_public.py').read_text(encoding='utf8'),evaluator)
            reference=function(number)
            def wrong(*args, _number=number, _reference=reference):
                out=_reference(*args)
                if _number==134: out['counts'][-1]+=1
                elif _number==138: out['count']+=1
                else: out+=1
                return out
            results=evaluator['run_tests']({name:wrong})
            exact=[r for r in results if r['name'].startswith('Exact large')]
            self.assertEqual(len(exact),1); self.assertFalse(exact[0]['passed'])


if __name__ == '__main__':
    unittest.main()
