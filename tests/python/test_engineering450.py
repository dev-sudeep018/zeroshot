"""Independent oracles and composition checks for engineering lessons e63-e162."""
import ast
import copy
import hashlib
import itertools
import json
import pathlib
import unittest
from collections import Counter
from functools import lru_cache

ROOT = pathlib.Path(__file__).resolve().parents[2]


@lru_cache(None)
def lesson(number):
    folder = next((ROOT / 'content/problems').glob(f'e{number}-*'))
    meta = json.loads((folder / 'lesson.json').read_text(encoding='utf-8'))
    ns = {}
    exec((folder / 'solution.py').read_text(encoding='utf-8'), ns)
    return ns[meta['signature'].split('(')[0]]


class Engineering450Tests(unittest.TestCase):
    def test_full_batch_public_cases_starters_and_displayed_examples(self):
        helpers = (ROOT / 'content/evaluator_helpers.py').read_text(encoding='utf-8')
        for number in range(63, 163):
            with self.subTest(number=number):
                folder = next((ROOT / 'content/problems').glob(f'e{number}-*'))
                metadata = json.loads((folder / 'lesson.json').read_text(encoding='utf-8'))
                ns = {}
                exec(helpers, ns)
                exec((folder / 'solution.py').read_text(encoding='utf-8'), ns)
                exec((folder / 'tests_public.py').read_text(encoding='utf-8'), ns)
                results = ns['run_tests'](ns)
                self.assertEqual(len(results), metadata['test_count'])
                self.assertTrue(all(r['passed'] for r in results), results)
                starter = {}
                exec((folder / 'starter.py').read_text(encoding='utf-8'), starter)
                self.assertFalse(any(r['passed'] for r in ns['run_tests'](starter)))
                for example in metadata['examples']:
                    ns['assert_close'](eval(example['input'], ns), ast.literal_eval(example['output']))

    def test_stock_conservation_and_request_accounting(self):
        f = lesson(65)
        for quantities in itertools.product(range(3), repeat=3):
            requests = [['a', n] for n in quantities]
            result = f({'a': 3}, requests)
            self.assertEqual(result['remaining']['a'] + sum(result['filled']), 3)
            self.assertEqual([a+b for a, b in zip(result['filled'], result['unfilled'])], list(quantities))
            self.assertEqual(sum(result['filled']), min(3, sum(quantities)))

    def test_record_presence_and_deep_copy_are_distinct(self):
        records = [{'x': None}, {'x': False}, {'x': 0}, {}]
        self.assertEqual(lesson(69)(records, 'x', 'missing'), [None, False, 0, 'missing'])
        value = {'nested': [1]}
        projected = lesson(70)([{'x': value}], ['x', 'absent'])
        projected[0]['x']['nested'].append(2)
        self.assertEqual(value, {'nested': [1]})
        renamed = lesson(71)({'a': 1, 'b': 2}, {'a': 'b', 'b': 'a'})
        self.assertEqual(renamed, {'b': 1, 'a': 2})

    def test_batches_pages_and_round_robin_preserve_every_item(self):
        items = list(range(23))
        for size in range(1, 8):
            batches = lesson(80)(items, size)
            self.assertEqual(lesson(83)(batches), items)
            self.assertTrue(all(0 < len(b) <= size for b in batches))
            page_items = []; offset = 0
            while offset is not None:
                page = lesson(81)(items, offset, size)
                page_items.extend(page['items']); offset = page['next_offset']
            self.assertEqual(page_items, items)
        jobs = [str(i) for i in items]
        for workers in range(1, 6):
            queues = lesson(79)(jobs, workers)
            self.assertEqual(lesson(82)(queues), jobs)

    def test_adjacent_transition_counts_and_streak_oracle(self):
        for n in range(6):
            for seq in itertools.product('ab', repeat=n):
                self.assertEqual(lesson(85)(seq), dict(Counter(zip(seq, seq[1:]))))
                expected = {}
                for key, group in itertools.groupby(seq):
                    expected[key] = max(expected.get(key, 0), len(list(group)))
                self.assertEqual(lesson(86)(seq), expected)

    def test_sorted_event_merge_has_left_first_ties(self):
        for a in itertools.combinations_with_replacement(range(3), 3):
            for b in itertools.combinations_with_replacement(range(3), 2):
                left = [[t, 'L'+str(i)] for i, t in enumerate(a)]
                right = [[t, 'R'+str(i)] for i, t in enumerate(b)]
                self.assertEqual(lesson(101)(left, right), sorted(left+right, key=lambda row: row[0]))

    def test_quantity_histogram_partitions_at_inclusive_bounds(self):
        values = list(range(13)) + [3, 3, 7]
        bounds = [0, 3, 7, 12]
        expected = [sum(sum(v>b for b in bounds) == i for v in values) for i in range(5)]
        self.assertEqual(lesson(97)(values, bounds), expected)
        self.assertEqual(sum(expected), len(values))

    def test_text_spans_redaction_and_byte_boundaries(self):
        text = 'é🙂 Hello, AI!'
        spans = lesson(104)(text)
        for word, start, end in spans:
            self.assertEqual(text[start:end], word)
        offsets = lesson(111)(text)
        self.assertEqual(offsets, [len(text[:i].encode('utf-8')) for i in range(len(text)+1)])
        redacted = lesson(106)(text, [[1, 5], [3, 9]], '*')
        self.assertEqual(redacted, ''.join('*' if 1 <= i < 9 else c for i, c in enumerate(text)))

    def test_vocabulary_roundtrip_and_training_only_fit(self):
        vocab = {'red': 2, 'blue': 5, 'green': 9}
        tokens = ['red', 'unknown', 'blue', 'red']
        encoded = lesson(112)(tokens, vocab, 0)
        decoded = lesson(113)(encoded['ids'], vocab, '?')
        self.assertEqual(decoded['tokens'], ['red', '?', 'blue', 'red'])
        first = lesson(136)(['b', 'a', 'b'], ['a', 'unseen'])
        second = lesson(136)(['b', 'a', 'b'], ['different', 'new'])
        self.assertEqual(first['vocabulary'], second['vocabulary'])
        self.assertEqual(first['train_codes'], [0, 1, 0])
        self.assertEqual(first['heldout_codes'], [1, -1])

    def test_bio_raw_previous_tag_and_parser_boundaries(self):
        self.assertEqual(lesson(115)(['I-X', 'I-X', 'O', 'I-X', 'B-Y', 'I-X']), [0, 3, 5])
        self.assertEqual(lesson(116)('x=1=2\ny=\n'), {'x': '1=2', 'y': ''})
        self.assertEqual(lesson(118)(['+0002', '-0', ' -3 '], -3, 3), [2, 0, -3])
        with self.assertRaises(ValueError): lesson(118)(['１２'], 0, 99)
        self.assertEqual(lesson(120)('2.9.99', '2.10.0'), -1)

    def test_csv_query_and_json_roundtrips(self):
        records = [{'a': 'hello,\n"world"', 'b': 'é'}, {'a': '', 'b': 'x=y&z'}]
        csv = lesson(122)(records, ['a', 'b'])
        self.assertEqual(lesson(121)(csv), records)
        mapping = {'a&b': ['x=y', '', '🙂+'], 'empty': []}
        self.assertEqual(lesson(127)(lesson(128)(mapping)), {k: v for k, v in mapping.items() if v})
        value = {'b': [True, None, 1.0], 'a': {'z': 'é'}}
        self.assertEqual(json.loads(lesson(124)(value)), value)
        self.assertEqual(lesson(123)('{}\n{bad\n\n{"ok":true}')['rejected_lines'], [2])

    def test_forward_fill_limit_is_not_reset_by_filled_values(self):
        source = [None, 1, None, None, None, 2, None, None]
        self.assertEqual(lesson(134)(source, 1), [None, 1, 1, None, None, 2, 2, None])
        self.assertEqual(lesson(134)(source, 0), source)
        self.assertEqual(lesson(134)(source, 99), [None, 1, 1, 1, 1, 2, 2, 2])

    def test_multilabel_error_matches_indicator_vectors(self):
        vocabulary = ['a', 'b', 'c']
        subsets = [list(s) for n in range(4) for s in itertools.combinations(vocabulary, n)]
        for expected in subsets:
            for predicted in subsets:
                result = lesson(138)([expected], [predicted], vocabulary)
                mismatch = sum((v in expected) != (v in predicted) for v in vocabulary)
                self.assertEqual(result['total_errors'], mismatch)
                self.assertAlmostEqual(result['loss'], mismatch/3)

    def test_retrieval_counts_duplicates_as_slots_not_extra_hits(self):
        result = lesson(140)(['a', 'a', 'b', 'c'], ['a', 'b'], 3)
        self.assertEqual(result, {'hits': 2, 'precision': 2/3})
        self.assertEqual(lesson(140)(['a'], ['a'], 4)['precision'], 0.25)
        coverage = lesson(141)([['a', 'x', 'a'], ['b', 'x']], ['a', 'b', 'c'])
        self.assertAlmostEqual(coverage['coverage'], 2/3)
        self.assertEqual(coverage['out_of_corpus_ids'], ['x'])

    def test_hash_membership_has_nontrivial_known_buckets_and_extension_invariance(self):
        ids = ['a', 'b', 'abc', 'é', 'customer-19']
        # Hex conversion supplies an independent spelling of the documented first-eight-byte bucket.
        buckets = {v: int(hashlib.sha256(v.encode()).hexdigest()[:16], 16) % 10000 for v in ids}
        for threshold in [1, 2500, 5000, 9999]:
            result = lesson(143)(ids, threshold)
            self.assertEqual(result['holdout'], [v for v in ids if buckets[v] < threshold])
            expanded = lesson(143)(ids+['new-id'], threshold)
            self.assertEqual(set(result['holdout']), set(expanded['holdout']) & set(ids))

    def test_windows_partition_integer_time_and_sessions_partition_events(self):
        times = list(range(-12, 13))
        for width in range(1, 7):
            windows = lesson(144)(times, width, 2)
            self.assertEqual(sum(count for _, count in windows), len(times))
            for start, count in windows:
                self.assertEqual((start-2) % width, 0)
                self.assertEqual(count, sum(start <= t < start+width for t in times))
        times = [-4, -4, -1, 2, 9, 9, 15]
        for timeout in range(8):
            groups = lesson(145)(times, timeout)
            self.assertEqual(sum(groups, []), list(range(len(times))))
            for group in groups:
                self.assertTrue(all(times[b]-times[a] <= timeout for a, b in zip(group, group[1:])))

    def test_retry_and_queue_conservation(self):
        for retries in range(8):
            result = lesson(147)(retries, 0.25, 3)
            self.assertEqual(result['total'], sum(result['delays']))
            self.assertTrue(all(0 <= d <= 3 for d in result['delays']))
        ops = [['put', 'a', 2], ['put', 'b', 4], ['put', 'c', 4], ['take'], ['take']]
        result = lesson(150)(ops, 2)
        self.assertEqual(result, {'served': ['b', 'a'], 'rejected': [2], 'pending': []})
        self.assertEqual(lesson(149)([['take'], ['put', 'a'], ['take']])['served'], [None, 'a'])
        self.assertEqual(lesson(146)(['a', 'b', 'a', 'c', 'a'], 2)['accepted'], [0, 1, 3, 4])

    def test_worker_load_accounting_and_topological_minimal_order(self):
        durations = [4, 0, 2, 7, 1, 3]
        for workers in range(1, 5):
            result = lesson(151)(durations, workers)
            expected = [sum(d for d, a in zip(durations, result['assignments']) if a == w) for w in range(workers)]
            self.assertEqual(result['loads'], expected)
            self.assertEqual(result['makespan'], max(expected))
        graph = {'d': ['b', 'c'], 'b': ['a'], 'c': ['a'], 'a': [], 'z': []}
        permutations = itertools.permutations(graph)
        valid = [order for order in permutations if all(order.index(d) < order.index(k) for k, deps in graph.items() for d in deps)]
        indices = {k: i for i, k in enumerate(graph)}
        expected = min(valid, key=lambda order: tuple(indices[k] for k in order))
        self.assertEqual(lesson(152)(graph), list(expected))

    def test_rebuild_and_downstream_closure(self):
        graph = {'out': ['mid'], 'mid': ['in'], 'in': [], 'unrelated': []}
        old = {k: 'same' for k in graph}; new = dict(old, **{'in': 'changed'})
        self.assertEqual(lesson(153)(graph, ['in']), ['out', 'mid'])
        self.assertEqual(lesson(162)(graph, old, new), ['in', 'mid', 'out'])
        self.assertEqual(lesson(162)(graph, old, old), [])
        with self.assertRaises(ValueError): lesson(162)({'a': ['a']}, {'a': 'x'}, {'a': 'x'})

    def test_prefix_and_phrase_search_match_direct_predicates(self):
        terms = ['car', 'cat', 'cat', 'é', 'abc']
        index = lesson(154)(terms)
        for prefix, matches in index.items():
            self.assertEqual(matches, sorted({term for term in terms if term.startswith(prefix)}))
        for tokens in itertools.product('ab', repeat=5):
            for phrase in itertools.product('ab', repeat=2):
                expected = [i for i in range(4) if all(tokens[i+j] == phrase[j] for j in range(2))]
                self.assertEqual(lesson(155)(tokens, phrase), expected)

    def test_message_budget_maximal_prefix_and_frames_roundtrip(self):
        messages = ['', 'é', '🙂', 'a:b', 'tail']
        for budget in range(21):
            result = lesson(157)(messages, budget, '|')
            count = len(result['kept'])
            self.assertEqual(result['used_bytes'], len('|'.join(messages[:count]).encode()))
            if count < len(messages): self.assertGreater(len('|'.join(messages[:count+1]).encode()), budget)
        frames = lesson(158)
        encoded = frames(messages, 'encode')
        self.assertEqual(frames(encoded, 'decode'), messages)
        for blob in [b'01:a', b'-1:a', b'1:\xff', b'2:a', b'1', b':']:
            with self.assertRaises(ValueError): frames(blob, 'decode')

    def test_framed_stream_total_limit_is_symmetric(self):
        frames = lesson(158)
        messages = ['a'*10000]*999 + ['b'*4001]
        encoded = frames(messages, 'encode')
        self.assertEqual(len(encoded), 10000000)
        self.assertEqual(frames(encoded, 'decode'), messages)
        with self.assertRaises(ValueError): frames(messages[:-1]+['b'*4002], 'encode')
        with self.assertRaises(ValueError): frames(encoded+b'x', 'decode')

    def test_cache_copies_values_and_checkpoint_is_gap_free(self):
        entries = {'x': {'timestamp': 10, 'version': 'v', 'value': [1]}}
        result = lesson(160)(entries, 10, 'v', 1)
        result['x'].append(2)
        self.assertEqual(entries['x']['value'], [1])
        self.assertEqual(lesson(160)(entries, 11, 'v', 1), {})
        for subset_size in range(6):
            for ids in itertools.combinations(range(5), subset_size):
                result = lesson(161)(-1, ids)
                missing = next((i for i in range(6) if i not in ids), 5)
                self.assertEqual(result['committed'], missing-1)
                self.assertEqual(result['pending'], [i for i in ids if i > missing])


if __name__ == '__main__':
    unittest.main()
