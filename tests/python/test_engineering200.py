"""Independent invariants and small exhaustive oracles for engineering lessons e23-e62."""
import itertools
import math
import pathlib
import unittest
from fractions import Fraction
from functools import lru_cache

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]


@lru_cache(None)
def lesson(number, name):
    folder = next((ROOT / 'content/problems').glob(f'e{number}-*'))
    namespace = {}
    exec((folder / 'solution.py').read_text(encoding='utf-8'), namespace)
    return namespace[name]


class Engineering200Tests(unittest.TestCase):
    def test_ngram_window_mass_and_posting_positions(self):
        words = ['a', 'b', 'a', 'c', 'a', 'b']
        for n in range(1, 9):
            counts = lesson(23, 'ngram_counts')(words, n)
            self.assertEqual(sum(counts.values()), max(0, len(words)-n+1))
        postings = lesson(28, 'posting_index')([words, [], words[::-1]])
        for token, entries in postings.items():
            for document, positions in entries:
                original = [words, [], words[::-1]][document]
                self.assertEqual(positions, [i for i, value in enumerate(original) if value == token])
        self.assertEqual(postings['a'][0][1], [0, 2, 4])

    def test_multiset_jaccard_symmetry_and_duplication_invariance(self):
        f = lesson(24, 'multiset_jaccard')
        a, b = ['a', 'a', 'b'], ['a', 'c', 'c']
        self.assertAlmostEqual(f(a, b), 1/5)
        self.assertEqual(f(a, b), f(b, a))
        self.assertEqual(f(a*3, b*3), f(a, b))

    def test_edit_distance_metric_and_nonunit_transposition(self):
        f = lesson(25, 'edit_distance')
        sequences = [list(s) for n in range(4) for s in itertools.product('ab', repeat=n)]
        for a in sequences:
            self.assertEqual(f(a, a), 0)
            for b in sequences:
                self.assertEqual(f(a, b), f(b, a))
                self.assertGreaterEqual(f(a, b), abs(len(a)-len(b)))
                self.assertLessEqual(f(a, b), max(len(a), len(b)))
        self.assertEqual(f(list('abc'), list('acb')), 2)
        self.assertEqual(f(list('kitten'), list('sitting')), 3)

    def test_rouge_l_against_exhaustive_subsequences(self):
        f = lesson(26, 'rouge_l')
        sequences = [list(s) for n in range(4) for s in itertools.product('ab', repeat=n)]
        def subsequences(sequence):
            return {tuple(sequence[i] for i in range(len(sequence)) if mask & (1 << i)) for mask in range(1 << len(sequence))}
        for a in sequences:
            for b in sequences:
                expected = max(map(len, subsequences(a) & subsequences(b)))
                self.assertEqual(f(a, b)['lcs'], expected)

    def test_bleu_clipping_and_brevity_are_separate(self):
        f = lesson(27, 'bleu_one')
        self.assertAlmostEqual(f(['x']*5, ['x', 'y']), .2)
        self.assertAlmostEqual(f(['x'], ['x', 'y', 'z']), math.exp(-2))
        self.assertEqual(f(['y', 'x'], ['x', 'y']), 1)
        self.assertEqual(f(['z'], ['x', 'y']), 0)

    def test_boolean_query_matches_document_predicates(self):
        documents = [{'a', 'b'}, {'b'}, {'a', 'c'}, {'a', 'b', 'c'}]
        postings = {term: [i for i, doc in enumerate(documents) if term in doc] for term in 'abc'}
        result = lesson(29, 'boolean_query')(postings, ['a', 'b'], ['c'])
        self.assertEqual(result, [i for i, doc in enumerate(documents) if {'a', 'b'} <= doc and 'c' not in doc])

    def test_group_split_is_disjoint_exhaustive_and_leakage_free(self):
        groups = ['a', 'b', 'a', 'c', 'd', 'b']
        result = lesson(30, 'group_split')(groups, ['a', 'd'])
        train, test = result['train'], result['test']
        self.assertTrue(np.issubdtype(train.dtype, np.integer))
        self.assertFalse(set(train) & set(test))
        self.assertEqual(sorted([*train, *test]), list(range(len(groups))))
        self.assertFalse({groups[i] for i in train} & {groups[i] for i in test})

    def test_temporal_split_boundary_partition(self):
        times = np.array([3., -1., 1., 2., 0., 4.])
        result = lesson(31, 'temporal_split')(times, 2, 1)
        self.assertEqual(sorted(np.concatenate(list(result.values())).tolist()), list(range(6)))
        self.assertTrue(np.all(times[result['train']] < 1))
        self.assertTrue(np.all(times[result['test']] >= 3))
        self.assertTrue(np.all((times[result['gap']] >= 1) & (times[result['gap']] < 3)))

    def test_imputation_training_only_and_masked_placeholder_invariance(self):
        f = lesson(32, 'median_impute')
        train = np.array([[1., 10.], [3., 99.], [5., 30.]])
        mask = np.array([[False, False], [False, True], [False, False]])
        query = np.array([[1000., 2000.], [0., 0.]])
        missing = np.array([[False, False], [True, True]])
        result = f(train, query, mask, missing)
        np.testing.assert_allclose(result['medians'], [3, 20])
        np.testing.assert_allclose(result['filled'], [[1000, 2000], [3, 20]])
        train[mask] = -1e20
        np.testing.assert_array_equal(f(train, query, mask, missing)['medians'], result['medians'])

    def test_missingness_joint_counts_match_enumeration(self):
        mask = np.array([[True, True, False], [False, True, True], [True, False, False]])
        result = lesson(33, 'missingness_audit')(mask)
        for a in range(3):
            for b in range(3):
                self.assertEqual(result['co_missing'][a, b], sum(bool(row[a] and row[b]) for row in mask)/3)
        np.testing.assert_allclose(np.diag(result['co_missing']), result['feature_rates'])

    def test_psi_symmetric_and_nonnegative(self):
        f = lesson(34, 'population_stability')
        a, b = [0, 4, 7], [3, 2, 9]
        r = f(a, b, .25)
        self.assertAlmostEqual(r['psi'], f(b, a, .25)['psi'])
        self.assertTrue(np.all(r['contributions'] >= 0))
        self.assertAlmostEqual(sum(r['reference']), 1)
        self.assertAlmostEqual(sum(r['current']), 1)
        self.assertAlmostEqual(r['psi'], sum(r['contributions']))

    def test_ks_against_exact_fraction_oracle_including_ties(self):
        f = lesson(35, 'ks_distance')
        for a in ([0, 0, 1], [0, 2, 4], [0, 1], [1, 1]):
            for b in ([0, 1, 1], [1, 3, 5], [0], [2, 2, 2]):
                points = sorted(set(a) | set(b))
                gaps = [abs(Fraction(sum(v <= x for v in a), len(a))-Fraction(sum(v <= x for v in b), len(b))) for x in points]
                index = gaps.index(max(gaps))
                result = f(a, b)
                self.assertEqual(result['location'], points[index])
                self.assertAlmostEqual(result['statistic'], float(gaps[index]))

    def test_conformal_rank_and_interval_translation(self):
        f = lesson(36, 'conformal_interval')
        residuals = [8, 1, 6, 2, 7, 3, 5, 4, 9]
        result = f(residuals, [-1, 5], .2)
        self.assertEqual(result['radius'], 8)
        np.testing.assert_array_equal(result['upper']-result['lower'], [16, 16])
        shifted = f(residuals, [99, 105], .2)
        np.testing.assert_allclose(shifted['lower']-result['lower'], [100, 100])
        with self.assertRaises(ValueError):
            f([1, 2], [0], .01)

    def test_interval_coverage_monotonic_under_expansion(self):
        f = lesson(37, 'interval_audit')
        y = [-2, 0, 2, 5]
        narrow = f(y, [-1]*4, [1]*4)
        wide = f(y, [-3]*4, [3]*4)
        self.assertLessEqual(narrow['coverage'], wide['coverage'])
        self.assertLess(narrow['mean_width'], wide['mean_width'])
        self.assertEqual(wide['covered'].dtype, bool)

    def test_sign_test_against_exhaustive_fair_signs(self):
        f = lesson(38, 'paired_sign_test')
        for n in range(1, 8):
            for wins in range(n+1):
                tail = sum(sum(signs) <= min(wins, n-wins) for signs in itertools.product((0, 1), repeat=n)) / 2**n
                result = f([1]*wins+[-1]*(n-wins)+[0, 0])
                self.assertEqual(result['p_value'], min(1, 2*tail))
                self.assertEqual(result['ties'], 2)

    def test_cost_decisions_minimize_both_actions(self):
        result = lesson(39, 'cost_sensitive_predict')([.1, .4, .7], 2, 5)
        for i, p in enumerate([.1, .4, .7]):
            losses = [5*p, 2*(1-p)]
            self.assertEqual(result['predictions'][i], 1 if losses[1] <= losses[0] else 0)
            self.assertAlmostEqual(result['expected_cost'][i], min(losses))

    def test_group_rates_recover_overall_positive_predictions(self):
        y = [1, 0, 1, 0, 1, 0]
        p = [1, 1, 0, 0, 1, 1]
        groups = ['a', 'a', 'b', 'b', 'c', 'c']
        result = lesson(40, 'group_error_rates')(y, p, groups)
        self.assertEqual(sum(v['count'] for v in result.values()), len(y))
        self.assertEqual(sum(v['selection_rate']*v['count'] for v in result.values()), sum(p))
        self.assertEqual(sum(v['tpr']*v['positives'] for v in result.values()), sum(a*b for a, b in zip(y, p)))

    def test_precision_recall_points_are_achievable_with_ties(self):
        y, scores = [1, 0, 1, 1, 0], [4, 4, 2, 1, 1]
        result = lesson(41, 'precision_recall_points')(y, scores)
        self.assertEqual(len(result['thresholds']), len(set(scores)))
        for threshold, precision, recall in zip(*result.values()):
            selected = [i for i, score in enumerate(scores) if score >= threshold]
            true_positives = sum(y[i] for i in selected)
            self.assertEqual(precision, true_positives/len(selected))
            self.assertEqual(recall, true_positives/sum(y))

    def test_box_iou_geometry_and_nms_retained_pair_invariant(self):
        f = lesson(42, 'box_iou')
        boxes = np.array([[0., 0., 2., 2.], [1., 0., 3., 2.], [5., 5., 6., 6.]])
        overlap = f(boxes, boxes)
        np.testing.assert_allclose(np.diag(overlap), 1)
        np.testing.assert_allclose(overlap, overlap.T)
        np.testing.assert_allclose(f(boxes*3+17, boxes*3+17), overlap)
        self.assertAlmostEqual(overlap[0, 1], 1/3)
        kept = lesson(43, 'non_max_suppression')(boxes, [3, 2, 1], .3)
        self.assertEqual(kept, [0, 2])
        for a, b in itertools.combinations(kept, 2):
            self.assertLessEqual(overlap[a, b], .3)

    def test_run_length_roundtrip_and_maximal_runs(self):
        rng = np.random.default_rng(440)
        values = rng.integers(0, 4, 200)
        result = lesson(44, 'run_length_encode')(values)
        np.testing.assert_array_equal(np.repeat(result['values'], result['lengths']), values)
        self.assertTrue(np.all(result['values'][1:] != result['values'][:-1]))
        np.testing.assert_array_equal(result['starts'], np.r_[0, np.cumsum(result['lengths'])[:-1]])

    def test_affine_quantization_dtype_and_rounding_bound(self):
        f = lesson(45, 'affine_quantize')
        x = np.linspace(-5, 5, 101)
        result = f(x, .1, 15)
        self.assertEqual(result['quantized'].dtype, np.int8)
        self.assertLessEqual(np.max(np.abs(x-result['reconstructed'])), .05+1e-12)
        np.testing.assert_array_equal(f([0], .1, -100)['quantized'], [-100])
        np.testing.assert_array_equal(f([1000], 1, 100)['reconstructed'], [27])

    def test_kv_page_gather_tail_and_aliasing(self):
        pages = np.arange(24.).reshape(3, 2, 4)
        result = lesson(46, 'gather_kv_pages')(pages, [[2, 0]], [3])[0]
        np.testing.assert_array_equal(result, np.vstack([pages[2], pages[0, :1]]))
        original = pages.copy()
        result[:] = -1
        np.testing.assert_array_equal(pages, original)

    def test_beam_search_wide_beam_matches_exhaustive_sequences(self):
        table = np.array([[-1., -.3, -.7], [-.2, -.5, -.1], [-1., -1., -1.]])
        candidates = []
        def visit(sequence, score, steps):
            if sequence[-1] == 2 or steps == 0:
                candidates.append((sequence, score))
                return
            for token in range(3):
                visit(sequence+[token], score+table[sequence[-1], token], steps-1)
        visit([0], 0, 3)
        expected = sorted(candidates, key=lambda item: (-item[1], item[0]))[0]
        result = lesson(47, 'beam_search')(table, 0, 2, 100, 3)
        self.assertEqual(result['tokens'], expected[0])
        self.assertAlmostEqual(result['score'], expected[1])

    def test_speculative_verification_recovers_target_probability_mass(self):
        f = lesson(48, 'verify_draft')
        q, p = np.array([.6, .3, .1]), np.array([.2, .3, .5])
        mass = np.zeros(3)
        for proposed in range(3):
            for step in range(60):
                result = f(q[None, :], p[None, :], [proposed], [(step+.5)/60])
                if result['accepted']:
                    mass[proposed] += q[proposed]/60
                else:
                    mass += q[proposed]*result['correction']/60
        np.testing.assert_allclose(mass, p, atol=1e-12)

    def test_gradient_accumulation_matches_per_example_mean(self):
        rng = np.random.default_rng(490)
        examples = rng.normal(size=(11, 2, 3))
        partitions = [examples[:2], examples[2:7], examples[7:]]
        means = np.stack([part.mean(0) for part in partitions])
        result = lesson(49, 'accumulate_gradients')(means, [2, 5, 4])
        np.testing.assert_allclose(result, examples.mean(0))
        self.assertFalse(np.allclose(means.mean(0), examples.mean(0)))

    def test_unscaling_overflow_skips_whole_step_without_mutation(self):
        f = lesson(50, 'unscale_gradients')
        gradients = np.array([4., np.nan, -np.inf])
        original = gradients.copy()
        result = f(gradients, 2)
        self.assertTrue(result['skip_step'])
        np.testing.assert_array_equal(result['gradients'], np.zeros(3))
        np.testing.assert_array_equal(gradients, original)
        valid = f([4., -2.], 2)
        np.testing.assert_allclose(valid['gradients'], [2, -1])
        self.assertFalse(valid['skip_step'])

    def test_reservoir_small_exhaustive_draws_give_uniform_subsets(self):
        f = lesson(51, 'reservoir_sample')
        frequencies = {}
        for draws in itertools.product(range(3), range(4)):
            sample = tuple(sorted(f([0, 1, 2, 3], 2, list(draws)).tolist()))
            frequencies[sample] = frequencies.get(sample, 0)+1
        self.assertEqual(set(frequencies), set(itertools.combinations(range(4), 2)))
        self.assertEqual(set(frequencies.values()), {2})

    def test_streaming_and_merged_moments_match_raw_batch_statistics(self):
        update = lesson(52, 'welford_update')
        merge = lesson(53, 'merge_moments')
        values = np.array([1000001., 999999., 1000002., 1000000., 999998.])
        first = update(0, 0, 0, values[:2])
        result = update(first['count'], first['mean'], first['m2'], values[2:])
        self.assertEqual(result['count'], len(values))
        self.assertAlmostEqual(result['mean'], values.mean())
        self.assertAlmostEqual(result['m2'], np.sum((values-values.mean())**2), places=6)
        parts = [values[:1], values[1:3], values[3:]]
        states = [update(0, 0, 0, part) for part in parts]
        merged = merge([s['count'] for s in states], [s['mean'] for s in states], [s['m2'] for s in states])
        self.assertAlmostEqual(merged['m2'], result['m2'], places=6)
        reversed_states = states[::-1]
        reversed_result = merge([s['count'] for s in reversed_states], [s['mean'] for s in reversed_states], [s['m2'] for s in reversed_states])
        self.assertAlmostEqual(reversed_result['m2'], result['m2'], places=6)

    def test_weighted_keys_match_power_priorities_and_weight_rescaling(self):
        f = lesson(54, 'weighted_sample_keys')
        weights = np.array([1., 3., 2., 5.])
        uniforms = np.array([.2, .4, .8, .6])
        expected = np.argsort(-(uniforms**(1/weights)), kind='stable')[:3]
        np.testing.assert_array_equal(f(weights, uniforms, 3)['indices'], expected)
        np.testing.assert_array_equal(f(weights*7, uniforms, 3)['indices'], expected)

    def test_hash_features_are_additive_with_explicit_unicode_policy(self):
        f = lesson(55, 'hashed_features')
        left, right = ['alpha', 'beta', 'alpha'], ['gamma', '\u03b1']
        np.testing.assert_array_equal(f(left+right, 13), f(left, 13)+f(right, 13))
        h = (31*ord('a')+ord('b')) % 2**32
        expected = np.zeros(7)
        expected[(h//2)%7] = 1 if h%2 == 0 else -1
        np.testing.assert_array_equal(f(['ab'], 7), expected)

    def test_count_min_never_underestimates_nonnegative_updates(self):
        hashes = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
        counts = np.array([3, 1, 4, 2])
        result = lesson(56, 'count_min_sketch')(hashes, counts, hashes, 2)
        self.assertTrue(np.issubdtype(result['sketch'].dtype, np.integer))
        self.assertTrue(np.all(result['estimates'] >= counts))
        np.testing.assert_array_equal(result['sketch'].sum(1), [counts.sum(), counts.sum()])

    def test_bloom_filter_no_false_negatives_and_constructed_false_positive(self):
        f = lesson(57, 'bloom_filter')
        inserts = [[0, 2], [1, 3]]
        result = f(inserts, inserts+[[0, 3], [0, 4]], 5)
        np.testing.assert_array_equal(result['maybe_present'], [True, True, True, False])
        self.assertEqual(result['bits'].dtype, bool)
        np.testing.assert_array_equal(f(inserts*3, inserts, 5)['bits'], result['bits'])

    def test_lru_matches_last_occurrence_order_without_eviction(self):
        requests = ['a', 'b', 'c', 'a', 'c', 'd']
        result = lesson(58, 'lru_trace')(requests, 10)
        expected = sorted(set(requests), key=lambda key: max(i for i, value in enumerate(requests) if value == key), reverse=True)
        self.assertEqual(result['keys'], expected)
        self.assertEqual(result['evicted'], [])
        np.testing.assert_array_equal(result['hits'], [False, False, False, True, True, False])

    def test_token_bucket_conservation_without_capacity_clipping(self):
        times = np.array([0., .1, .2, .3])
        costs = np.array([2., 1., 10., 1.])
        result = lesson(59, 'token_bucket')(times, costs, 5, 1)
        spent = np.cumsum(costs*result['allowed'])
        np.testing.assert_allclose(result['remaining'], 5+times-spent)
        self.assertTrue(np.all(result['remaining'] >= 0))
        self.assertTrue(np.all(result['remaining'] <= 5))

    def test_padding_batches_cover_indices_and_enforce_padded_budget(self):
        lengths = [2, 8, 1, 3, 3, 5, 2]
        result = lesson(60, 'padding_batches')(lengths, 12, 3)
        self.assertEqual([i for batch in result['batches'] for i in batch], list(range(len(lengths))))
        for batch, cost in zip(result['batches'], result['padded_tokens']):
            self.assertLessEqual(len(batch), 3)
            self.assertEqual(cost, max(lengths[i] for i in batch)*len(batch))
            self.assertLessEqual(cost, 12)

    def test_interleaving_ownership_is_valid_and_deduplicated(self):
        left, right = [1, 2, 1, 5], [2, 3, 4, 5]
        result = lesson(61, 'interleave_rankings')(left, right, 100)
        self.assertEqual(set(result['documents']), set(left) | set(right))
        self.assertEqual(len(result['documents']), len(set(result['documents'])))
        for document, owner in zip(result['documents'], result['owners']):
            self.assertIn(document, [left, right][owner])

    def test_asof_join_matches_bruteforce_latest_available_event(self):
        times = [5., 1., 3., 3., 7.]
        values = np.arange(10.).reshape(5, 2)
        queries = [-1., 1., 2., 3., 6., 9.]
        result = lesson(62, 'asof_features')(times, values, queries)
        for i, query in enumerate(queries):
            eligible = [j for j, time in enumerate(times) if time <= query]
            expected = max(eligible, key=lambda j: (times[j], j)) if eligible else -1
            self.assertEqual(result['indices'][i], expected)
            self.assertEqual(result['matched'][i], expected >= 0)
            np.testing.assert_array_equal(result['values'][i], values[expected] if expected >= 0 else [0, 0])


if __name__ == '__main__':
    unittest.main()
