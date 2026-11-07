"""Independent publication checks for the 250 additions to the 450 catalog."""
import ast
import copy
import json
import pathlib
import unittest
import numpy as np


ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTENT = ROOT / 'content/problems'
HELPERS = (ROOT / 'content/evaluator_helpers.py').read_text(encoding='utf-8')
NEW_IDS = ({f'm{i}' for i in range(60, 160)} |
           {f'd{i}' for i in range(80, 130)} |
           {f'e{i}' for i in range(63, 163)})


class Catalog450Tests(unittest.TestCase):
    def packages(self):
        folders = {p.name.split('-', 1)[0]: p for p in CONTENT.iterdir() if p.is_dir()}
        self.assertTrue(NEW_IDS <= folders.keys(), sorted(NEW_IDS - folders.keys()))
        return [folders[identifier] for identifier in sorted(NEW_IDS)]

    def test_rendered_worked_outputs_match_the_documented_calls(self):
        def plain(value):
            if isinstance(value, np.ndarray):
                return plain(value.tolist())
            if isinstance(value, np.generic):
                return value.item()
            if isinstance(value, dict):
                return {key: plain(item) for key, item in value.items()}
            if isinstance(value, (list, tuple)):
                return type(value)(plain(item) for item in value)
            return value

        assertions = {}
        exec(HELPERS, assertions)
        for folder in self.packages():
            lesson = json.loads((folder / 'lesson.json').read_text(encoding='utf-8'))
            reference = {}
            exec((folder / 'solution.py').read_text(encoding='utf-8'), reference)
            for example in lesson['examples']:
                with self.subTest(lesson=folder.name, example=example['name']):
                    # The trailing display note explains rounded values / arrays as lists.
                    shown = example['output'].split('\n(', 1)[0]
                    try:
                        expected = ast.literal_eval(shown)
                    except (ValueError, SyntaxError):
                        expected = json.loads(shown)
                    actual = plain(eval(example['input'], reference))
                    assertions['assert_close'](actual, expected)

    def test_samples_match_worked_examples_and_references_fit_editor(self):
        for folder in self.packages():
            with self.subTest(lesson=folder.name):
                lesson = json.loads((folder / 'lesson.json').read_text(encoding='utf-8'))
                evaluator, reference = {}, {}
                exec(HELPERS + '\n' + (folder / 'tests_public.py').read_text(encoding='utf-8'), evaluator)
                source = (folder / 'solution.py').read_text(encoding='utf-8')
                self.assertLessEqual(len(source), 32000)
                exec(source, reference)
                samples = evaluator['run_tests'](reference, 'sample')
                self.assertEqual([row['name'] for row in samples],
                                 [example['name'] for example in lesson['examples'][:3]])
                self.assertTrue(all(row['passed'] for row in samples), samples)

    def test_canned_example_answer_fails_a_valid_behavior_case(self):
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
                self.assertTrue(observed)
                canned = lambda *args, **kwargs: copy.deepcopy(observed[0])
                results = evaluator['run_tests']({name: canned})
                self.assertTrue(any(not row['passed'] and not row['name'].lower().startswith('reject')
                                    for row in results), 'Canned answers must fail valid-input cases')


if __name__ == '__main__':
    unittest.main()
