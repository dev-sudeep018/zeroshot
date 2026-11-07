"""Independent oracles and invariants for the original D80-D129 lessons."""
from pathlib import Path
import itertools
import math
import runpy
import unittest
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
CACHE = {}


def fn(number, name):
    if number not in CACHE:
        CACHE[number] = runpy.run_path(str(next((ROOT/'content/problems').glob(f'd{number}-*/solution.py'))))
    return CACHE[number][name]


def derivative(objective, value, step=1e-5):
    result = np.zeros_like(value, dtype=float)
    for index in np.ndindex(value.shape):
        left = value.copy(); right = value.copy()
        left[index] -= step; right[index] += step
        result[index] = (objective(right)-objective(left))/(2*step)
    return result


class Deep450Oracles(unittest.TestCase):
    def test_parameter_counts_equal_explicit_connection_enumeration(self):
        widths = [2,5,3,4]; flags = [1,0,1]
        dense = fn(80,'dense_budget')(widths,flags)
        counts = [len(list(itertools.product(range(a),range(b))))+flag*b for a,b,flag in zip(widths,widths[1:],flags)]
        self.assertEqual(dense['total'],sum(counts))
        np.testing.assert_array_equal(dense['per_layer'],counts)
        conv = fn(81,'convolution_budget')(6,8,[2,3],2,[3,5],1)
        connections = list(itertools.product(range(8),range(3),range(2),range(3)))
        self.assertEqual(conv['weights'],len(connections))
        self.assertEqual(conv['macs'],len(connections)*15)

    def test_receptive_field_matches_explicit_dependency_sets(self):
        kernels=[2,3,2]; strides=[2,1,3]; dilation=[1,2,1]
        def dependency(layer,position):
            if layer<0: return {position}
            return set().union(*(dependency(layer-1,position*strides[layer]+j*dilation[layer]) for j in range(kernels[layer])))
        result=fn(82,'receptive_fields')(kernels,strides,dilation)
        for i in range(3):
            positions=dependency(i,0)
            self.assertEqual(result['field'][i],max(positions)-min(positions)+1)
            self.assertEqual(result['jump'][i],min(dependency(i,1))-min(positions))

    def test_freezing_and_initialization_variance(self):
        f=fn(83,'frozen_sgd'); w=np.array([2.,3.,4.]); g=np.array([10.,-2.,4.])
        result=f(w,g,[0,1,0],.25)
        np.testing.assert_allclose(result['weights'],[2,3.5,4])
        np.testing.assert_array_equal(w,[2,3,4])
        budget=fn(84,'initialization_budget')(8,4,3)
        self.assertAlmostEqual(budget[0,1],4)
        self.assertAlmostEqual(budget[1,1],6)
        self.assertAlmostEqual(budget[1,0]*8/2,1)

    def test_activation_audits_reduce_examples_not_neurons(self):
        result=fn(85,'relu_activity')([[-2,0,1],[0,-1,2],[4,-3,-1]])
        np.testing.assert_allclose(result['active_fraction'],[1/3,0,2/3])
        np.testing.assert_allclose(result['mean_output'],[4/3,0,1])
        np.testing.assert_array_equal(result['inactive'],[False,True,False])
        audit=fn(86,'sigmoid_audit')([[-1000,0],[1000,0]],.1)
        np.testing.assert_array_equal(audit['probabilities'],[[0,.5],[1,.5]])
        np.testing.assert_allclose(audit['mean_derivative'],[0,.25])
        np.testing.assert_array_equal(audit['saturated_fraction'],[1,0])

    def test_dropout_moments_by_exact_mask_enumeration(self):
        x=np.array([2.,-3.,.5]); probability=.25
        outcomes=[]; weights=[]
        for mask in itertools.product([0,1],repeat=len(x)):
            outcomes.append(x*np.array(mask)/probability)
            weights.append(math.prod(probability if m else 1-probability for m in mask))
        outcomes=np.array(outcomes); weights=np.array(weights)
        result=fn(87,'dropout_moments')(x,probability)
        expected=weights@outcomes
        np.testing.assert_allclose(result['mean'],expected)
        np.testing.assert_allclose(result['variance'],weights@((outcomes-expected)**2))
        np.testing.assert_allclose(result['second_moment'],weights@(outcomes**2))

    def test_margin_ties_and_probability_vote_disagreement(self):
        z=np.array([[3,7,7,-1],[-3,-4,2,1.]])
        margins=fn(88,'logit_margins')(z)
        np.testing.assert_array_equal(margins['winner'],[1,2])
        np.testing.assert_array_equal(margins['runner_up'],[2,3])
        np.testing.assert_allclose(fn(88,'logit_margins')(z+100)['margin'],margins['margin'])
        # Two weak votes for class zero are outweighed by a confident minority.
        ensemble=fn(89,'ensemble_audit')([[[.51,.49]],[[.51,.49]],[[0,1]]])
        np.testing.assert_array_equal(ensemble['prediction'],[1])
        np.testing.assert_allclose(ensemble['vote_disagreement'],[1/3])

    def test_neuron_contribution_and_saliency_finite_difference(self):
        x=np.array([[.2,-.3,2.],[1.,4.,-2.]])
        w=np.array([[1.,2.],[-2.,3.],[.5,-1.]])
        result=fn(90,'neuron_contributions')(x,w[:,0],.7)
        np.testing.assert_allclose(result['score'],x@w[:,0]+.7)
        classes=[1,0]; saliency=fn(91,'linear_saliency')(x,w,classes)
        numeric=derivative(lambda data:sum((data@w)[i,c] for i,c in enumerate(classes)),x)
        np.testing.assert_allclose(saliency['gradient'],numeric,atol=1e-9)
        np.testing.assert_allclose(saliency['input_times_gradient'],x*numeric,atol=1e-9)

    def test_per_example_clipping_and_conflict_geometry(self):
        gradients=np.array([[3.,4.],[0.,0.],[-6.,-8.]])
        clip=fn(92,'clip_example_gradients')(gradients,2)
        np.testing.assert_allclose(np.linalg.norm(clip['clipped'],axis=1),[2,0,2])
        np.testing.assert_allclose(clip['mean'],[0,0],atol=1e-15)
        np.testing.assert_allclose(clip['scale'],[.4,1,.2])
        conflict=fn(93,'gradient_conflicts')(gradients)
        np.testing.assert_allclose(conflict['cosine'],[[1,0,-1],[0,0,0],[-1,0,1]])
        np.testing.assert_array_equal(conflict['conflict'],[[False,False,True],[False,False,False],[True,False,False]])

    def test_conflict_zero_band_and_extreme_scale_are_portable(self):
        audit = fn(93, 'gradient_conflicts')
        mixed = audit([[1,1], [1,-1], [-2,-1]])
        self.assertEqual(mixed['cosine'][0,1], 0)
        self.assertFalse(mixed['conflict'][0,1])
        near = audit([[1,0], [-1e-13,1], [-1e-8,1]])
        self.assertFalse(near['conflict'][0,1])
        self.assertTrue(near['conflict'][0,2])
        original = np.array([[1.,0], [-1.,0], [0,1.]])
        baseline = audit(original)
        for scales in ([1e-200, 1e-150, 1e-100], [1e6, 1e-100, 1]):
            actual = audit(original * np.array(scales)[:,None])
            np.testing.assert_allclose(actual['cosine'], baseline['cosine'])
            np.testing.assert_array_equal(actual['conflict'], baseline['conflict'])

    def test_ratios_and_stopping_ignore_unprocessed_epochs(self):
        ratios=fn(94,'update_ratios')([[3,4],[0,0]],[[.3,.4],[0,.2]],.1)
        np.testing.assert_allclose(ratios['ratio'],[.1,2])
        stop=fn(95,'early_stopping')([5,4,3.9,3.8,0],2,.2)
        self.assertEqual(stop['best_epoch'],1)
        self.assertEqual(stop['stop_epoch'],3)
        np.testing.assert_array_equal(stop['stall_counts'],[0,0,1,2])

    def test_plateau_decay_nesterov_distinct_update_conventions(self):
        rates=fn(96,'plateau_rates')([3,2,2,2,1,1,1,1,1],.8,.5,2,.15)
        np.testing.assert_allclose(rates,[.8,.8,.8,.4,.4,.4,.2,.2,.15])
        decay=fn(97,'decoupled_decay')([10],[-2],.1,.3)
        np.testing.assert_allclose(decay['weights'],[9.9])
        self.assertAlmostEqual(decay['decay_delta'][0],-.3)
        result=fn(98,'nesterov_step')([2],[.4],[3],.5,.1)
        np.testing.assert_allclose(result['lookahead'],[2.2])
        np.testing.assert_allclose(result['velocity'],[-.1])
        np.testing.assert_allclose(result['weights'],[1.9])

    def test_quadratic_line_minimum_has_zero_slope(self):
        h=np.array([[3.,1.],[1.,2.]]); point=np.array([2.,-1.]); direction=np.array([-.5,2.])
        probe=fn(99,'quadratic_probe')(h,point,direction)
        optimum=point+probe['step']*direction
        self.assertAlmostEqual(float(direction@h@optimum),0,places=12)
        for offset in [-.2,.2]:
            other=point+(probe['step']+offset)*direction
            self.assertLess(float(optimum@h@optimum),float(other@h@other))

    def test_language_shift_and_masked_loss_ignore_padding(self):
        shifted=fn(100,'shift_language_batch')([[1,2,3,99],[4,5,98,97]],[3,2],0)
        np.testing.assert_array_equal(shifted['inputs'],[[1,2,0],[4,0,0]])
        np.testing.assert_array_equal(shifted['targets'],[[2,3,0],[5,0,0]])
        np.testing.assert_array_equal(shifted['mask'],[[True,True,False],[True,False,False]])
        logits=np.array([[[0.,math.log(3)],[100.,-100.]]])
        result=fn(101,'masked_token_nll')(logits,[[1,1]],[[1,0]])
        self.assertAlmostEqual(result['loss'],-math.log(.75))
        self.assertEqual(result['count'],1)
        changed=logits.copy(); changed[0,1]=[-500,500]
        self.assertAlmostEqual(fn(101,'masked_token_nll')(changed,[[1,1]],[[1,0]])['loss'],result['loss'])

    def test_teacher_forcing_ctc_and_empty_hidden_rows(self):
        forced=fn(102,'teacher_forcing_inputs')([[1,2,3,4]],[[5,6,7,8]],[[.1,.5,.9,0]],.5,9)
        np.testing.assert_array_equal(forced,[[9,1,6,7]])
        np.testing.assert_array_equal(fn(103,'collapse_ctc_path')([0,1,1,0,1,2,2,0],0),[1,1,2])
        np.testing.assert_array_equal(fn(103,'collapse_ctc_path')([0,0],0),[])
        hidden=np.arange(24).reshape(3,4,2)
        np.testing.assert_array_equal(fn(104,'last_valid_state')(hidden,[0,2,4]),[[0,0],hidden[1,1],hidden[2,3]])

    def test_attention_entropy_and_rollout_path_enumeration(self):
        audit=fn(105,'attention_support')([[1,0,0,0],[.25,.25,.25,.25]])
        np.testing.assert_allclose(audit['effective_support'],[1,4])
        np.testing.assert_allclose(audit['entropy'],[0,math.log(4)])
        a=np.array([[[.8,.2],[.3,.7]],[[.1,.9],[.6,.4]]])
        r=fn(106,'attention_rollout')(a,.5)
        transitions=[(layer+.5*np.eye(2))/1.5 for layer in a]
        expected=np.array([[sum(transitions[1][i,k]*transitions[0][k,j] for k in range(2)) for j in range(2)] for i in range(2)])
        np.testing.assert_allclose(r[-1],expected)
        np.testing.assert_allclose(r.sum(-1),1)

    def test_streaming_convolution_chunking_and_patch_multiplication(self):
        f=fn(107,'causal_convolution_chunk'); signal=np.array([1.,3.,2.,-1.,4.]); kernel=np.array([.5,2.,-1.])
        complete=f(signal,kernel,[0,0]); first=f(signal[:2],kernel,[0,0]); second=f(signal[2:],kernel,first['state'])
        np.testing.assert_allclose(complete['output'],np.convolve(signal,kernel)[:len(signal)])
        np.testing.assert_allclose(np.r_[first['output'],second['output']],complete['output'])
        image=np.arange(30.).reshape(5,6); filt=np.array([[1,2,3],[-1,0,2.]])
        patches=fn(108,'image_patch_matrix')(image,[2,3],[2,2])
        expected=np.array([np.sum(image[r:r+2,c:c+3]*filt) for r,c in patches['positions']])
        np.testing.assert_allclose(patches['patches']@filt.ravel(),expected)

    def test_pixel_shuffle_inverse_and_label_resize_classes(self):
        source=np.arange(24).reshape(8,1,3); shuffled=fn(109,'pixel_shuffle')(source,2)
        restored=np.empty_like(source)
        for c,h,w,dy,dx in itertools.product(range(2),range(1),range(3),range(2),range(2)):
            restored[c*4+dy*2+dx,h,w]=shuffled[c,h*2+dy,w*2+dx]
        np.testing.assert_array_equal(restored,source)
        labels=np.array([[2,5,9],[3,7,11]])
        resized=fn(110,'resize_segmentation')(labels,[3,5])
        np.testing.assert_array_equal(resized,[[2,2,5,5,9],[2,2,5,5,9],[3,3,7,7,11]])
        self.assertTrue(set(resized.ravel())<=set(labels.ravel()))

    def test_bilinear_affine_surface_and_unpool_switches(self):
        plane=np.array([[2,5,8],[6,9,12.]])
        resized=fn(111,'bilinear_resize')(plane,[4,5])
        expected=np.array([[2+4*(i/3)+6*(j/4) for j in range(5)] for i in range(4)])
        np.testing.assert_allclose(resized,expected)
        values=np.array([[3,4],[-2,8.]])
        switches=np.array([[0,5],[7,11]])
        unpooled=fn(112,'max_unpool')(values,switches,[3,4])
        np.testing.assert_allclose(unpooled.ravel()[switches],values)
        self.assertEqual(np.count_nonzero(unpooled),4)

    def test_adaptive_pool_and_boundary_neighbor_oracles(self):
        # 3-to-2 bins overlap in the middle; disjoint partitioning is incorrect.
        pooled=fn(113,'adaptive_average_pool')([[1,2,9],[4,5,12],[7,8,15]],[2,2])
        np.testing.assert_allclose(pooled,[[3,7],[6,10]])
        labels=np.array([[1,1,2],[1,3,2],[1,1,1]])
        expected=np.zeros(labels.shape,dtype=bool)
        for row,col in np.ndindex(labels.shape):
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                r,c=row+dr,col+dc
                if 0<=r<3 and 0<=c<3 and labels[r,c]!=labels[row,col]: expected[row,col]=True
        np.testing.assert_array_equal(fn(114,'segmentation_boundaries')(labels),expected)

    def test_heatmap_mass_scaling_and_peak_ties(self):
        heat=np.array([[[0.,1.,0.],[0.,0.,3.]]])
        center=fn(115,'heatmap_centers')(heat)
        np.testing.assert_allclose(center['centers'],[[.75,1.75]])
        np.testing.assert_allclose(fn(115,'heatmap_centers')(heat*7)['centers'],center['centers'])
        peaks=fn(116,'heatmap_peaks')([[[0,5,5],[5,0,0]]])
        np.testing.assert_array_equal(peaks['coordinates'],[[0,1]])
        np.testing.assert_allclose(peaks['score'],[5])

    def test_erasure_cutmix_area_and_mixup_batch_conservation(self):
        image=np.arange(12.).reshape(3,4)
        erased=fn(117,'erase_rectangle')(image,[-4,2,2,9],-1)
        self.assertEqual(int(erased['mask'].sum()),4)
        np.testing.assert_array_equal(erased['image'][~erased['mask']],image[~erased['mask']])
        cut=fn(118,'cutmix_pair')(image,np.ones((3,4))*100,[1,0],[0,1],[-4,2,2,9])
        self.assertAlmostEqual(cut['replaced_fraction'],1/3)
        np.testing.assert_allclose(cut['label'],[2/3,1/3])
        mixed=fn(119,'mixup_batch')(image,np.eye(3),[2,0,1],.3)
        np.testing.assert_allclose(mixed['features'].sum(0),image.sum(0))
        np.testing.assert_allclose(mixed['labels'].sum(0),1)

    def test_patch_restore_and_masked_reconstruction_gradient(self):
        restored=fn(120,'restore_patches')([[4,5],[1,2]],[3,0],[-2,-3],5)
        np.testing.assert_array_equal(restored['tokens'][[3,0]],[[4,5],[1,2]])
        np.testing.assert_array_equal(restored['masked'],[False,True,True,False,True])
        p=np.array([[[.2,.5],[3.,-2.]],[[1.,2.],[4.,3.]]]); t=np.zeros_like(p); mask=np.array([[1,0],[0,1]])
        f=fn(121,'masked_reconstruction'); result=f(p,t,mask)
        # Independent selected-coordinate objective, including feature normalization.
        oracle=lambda data:float(np.mean([data[b,k,j]**2 for b,k,j in np.ndindex(data.shape) if mask[b,k]]))
        self.assertAlmostEqual(result['loss'],oracle(p))
        np.testing.assert_allclose(result['gradient'],derivative(oracle,p),atol=1e-9)

    def test_vq_stop_gradient_and_spectral_gain(self):
        e=np.array([[.2,.7],[2.,-1.]]); c=np.array([[1.,0.],[.3,.8]]); beta=.3
        result=fn(122,'vq_losses')(e,c,beta)
        np.testing.assert_allclose(result['encoder_gradient'],derivative(lambda v:beta*np.mean((v-c)**2),e),atol=1e-9)
        np.testing.assert_allclose(result['code_gradient'],derivative(lambda v:np.mean((v-e)**2),c),atol=1e-9)
        np.testing.assert_allclose(fn(122,'vq_losses')(e,c,0)['encoder_gradient'],0)
        w=np.array([[1.,2.,-1.],[3.,.4,2.]])
        normalized=fn(123,'spectral_normalize')(w,1.7)
        largest=math.sqrt(float(np.linalg.eigvalsh(normalized['weights']@normalized['weights'].T)[-1]))
        self.assertAlmostEqual(largest,1.7,places=12)

    def test_orthogonality_and_distillation_gradients(self):
        w=np.array([[1.,.2],[-.4,.8],[.3,-.2]])
        penalty=fn(124,'orthogonality_penalty')(w)
        def objective(data):
            return sum((sum(data[r,i]*data[r,j] for r in range(3))-(i==j))**2 for i in range(2) for j in range(2))
        np.testing.assert_allclose(penalty['gradient'],derivative(objective,w),atol=1e-8)
        student=np.array([[.2,.7,-.4],[1.,-.3,.4]]); teacher=np.array([[1.,2.,3.],[.1,.2,.3]]); temp=2.3
        f=fn(125,'distillation_kl'); actual=f(student,teacher,temp)
        np.testing.assert_allclose(actual['gradient'],derivative(lambda z:f(z,teacher,temp)['loss'],student),atol=1e-8)
        np.testing.assert_allclose(actual['gradient'].sum(1),0,atol=1e-15)
        self.assertAlmostEqual(f(student+100,teacher-50,temp)['loss'],actual['loss'],places=12)

    def test_batchnorm_folding_and_hidden_permutation_preserve_network(self):
        rng=np.random.default_rng(126)
        x=rng.normal(size=(5,3)); w=rng.normal(size=(3,4)); b=rng.normal(size=4); m=rng.normal(size=4); v=rng.uniform(.1,2,size=4); g=rng.normal(size=4); beta=rng.normal(size=4)
        folded=fn(126,'fold_batchnorm')(w,b,m,v,g,beta,1e-5)
        expected=((x@w+b)-m)/np.sqrt(v+1e-5)*g+beta
        np.testing.assert_allclose(x@folded['weights']+folded['bias'],expected)
        out=rng.normal(size=(4,2)); perm=fn(127,'permute_hidden')(w,b,out,[2,0,3,1])
        for activate in [np.tanh,lambda z:np.maximum(z,0)]:
            np.testing.assert_allclose(activate(x@w+b)@out,activate(x@perm['input_weights']+perm['hidden_bias'])@perm['output_weights'],atol=1e-14)

    def test_temperature_and_huber_derivatives(self):
        z=np.array([[.2,.7,-.5],[1.,-.3,.4]]); targets=[2,0]; temp=1.7; step=1e-5
        f=fn(128,'temperature_nll'); result=f(z,targets,temp)
        numeric=(f(z,targets,temp+step)['loss']-f(z,targets,temp-step)['loss'])/(2*step)
        self.assertAlmostEqual(result['temperature_gradient'],numeric,places=9)
        self.assertAlmostEqual(f(z+300,targets,temp)['temperature_gradient'],result['temperature_gradient'],places=12)
        residual=np.array([-3.,-.4,.2,2.]); huber=fn(129,'huber_residuals')(residual,1.3)
        objective=lambda r:sum(.5*x*x if abs(x)<=1.3 else 1.3*(abs(x)-.65) for x in r)/len(r)
        np.testing.assert_allclose(huber['mean_gradient'],derivative(objective,residual),atol=1e-9)
        np.testing.assert_allclose(fn(129,'huber_residuals')([-1.3,1.3],1.3)['derivative'],[-1.3,1.3])

    def test_numeric_input_helpers_reject_mixed_booleans(self):
        for number in range(80,130):
            fn(number,'_a')  # Load the batch-local validator for every package.
            with self.subTest(lesson=number):
                with self.assertRaises(ValueError): CACHE[number]['_a']([[1,True]],2)
                with self.assertRaises(ValueError): CACHE[number]['_a']([[1,float('inf')]],2)


if __name__ == '__main__':
    unittest.main()
