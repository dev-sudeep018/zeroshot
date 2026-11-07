"""Cross-batch checks for the 119 lessons added to the 200-lesson catalog."""
import copy
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTENT = ROOT / 'content/problems'
HELPERS = (ROOT / 'content/evaluator_helpers.py').read_text(encoding='utf-8')
NEW_IDS = ({f'm{i}' for i in range(20, 60)} |
           {f'd{i}' for i in range(41, 80)} |
           {f'e{i}' for i in range(23, 63)})


class CatalogExpansionTests(unittest.TestCase):
    def packages(self):
        folders = {p.name.split('-', 1)[0]: p for p in CONTENT.iterdir() if p.is_dir()}
        self.assertTrue(NEW_IDS <= folders.keys(), sorted(NEW_IDS - folders.keys()))
        return [folders[identifier] for identifier in sorted(NEW_IDS)]

    def test_worked_examples_are_the_three_executed_samples(self):
        for folder in self.packages():
            with self.subTest(lesson=folder.name):
                lesson = json.loads((folder / 'lesson.json').read_text(encoding='utf-8'))
                evaluator, reference = {}, {}
                exec(HELPERS + '\n' + (folder / 'tests_public.py').read_text(encoding='utf-8'), evaluator)
                source = (folder / 'solution.py').read_text(encoding='utf-8')
                self.assertLessEqual(len(source), 32000, 'Reference must fit the browser editor protocol')
                exec(source, reference)
                samples = evaluator['run_tests'](reference, 'sample')
                self.assertEqual([row['name'] for row in samples],
                                 [example['name'] for example in lesson['examples'][:3]])
                self.assertTrue(all(row['passed'] for row in samples), samples)

    def test_evaluators_reject_a_canned_example_on_valid_input(self):
        # A check that only rejects invalid shapes can look complete while
        # accepting a hard-coded example for every valid input. Test that threat
        # independently of the reference's own public-case success.
        for folder in self.packages():
            with self.subTest(lesson=folder.name):
                evaluator, reference = {}, {}
                exec(HELPERS + '\n' + (folder / 'tests_public.py').read_text(encoding='utf-8'), evaluator)
                exec((folder / 'solution.py').read_text(encoding='utf-8'), reference)
                lesson = json.loads((folder / 'lesson.json').read_text(encoding='utf-8'))
                name = lesson['signature'].split('(')[0]
                observed = []

                def record(*args, **kwargs):
                    value = reference[name](*args, **kwargs)
                    observed.append(copy.deepcopy(value))
                    return value

                evaluator['run_tests']({name: record}, 'sample')
                self.assertTrue(observed, 'Samples must actually call the learner function')
                canned = lambda *args, **kwargs: copy.deepcopy(observed[0])
                results = evaluator['run_tests']({name: canned})
                failures = [row for row in results
                            if not row['passed'] and not row['name'].lower().startswith('reject')]
                self.assertTrue(failures, 'A fixed example answer must fail a valid-behavior case')


if __name__ == '__main__':
    unittest.main()
