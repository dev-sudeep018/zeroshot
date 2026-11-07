"""Batch authoring must preserve provenance and never execute upstream snapshots."""
import copy
import hashlib
import importlib.util
import json
import pathlib
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[2]
loader = importlib.util.spec_from_file_location('author_batch',ROOT/'scripts/author-batch.py')
author = importlib.util.module_from_spec(loader)
loader.loader.exec_module(author)


class AuthorBatchTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='mastery-author-')
        self.addCleanup(self.temp.cleanup)
        self.base = pathlib.Path(self.temp.name)
        self.snapshot = self.base/'snapshot'
        self.snapshot.mkdir()
        self.spec = json.loads((ROOT/'scripts/authoring/example.json').read_text(encoding='utf-8'))
        notice=(ROOT/'content/problems/m18-clipped-policy-objective/THIRD_PARTY_NOTICE.md').read_text(encoding='utf-8')
        license_text=notice[notice.index('MIT License'):]
        license_bytes=license_text.encode('utf-8')
        (self.snapshot/'LICENSE').write_bytes(license_bytes)
        self.spec['source']['license_sha256']=hashlib.sha256(license_bytes).hexdigest()
        # A verified snapshot is data, even if its source contains a side effect.
        self.sentinel=self.base/'must-not-exist'
        source=f'from pathlib import Path\nPath({str(self.sentinel)!r}).write_text("executed")\n'.encode()
        item=self.spec['items'][0]
        self.source_path=self.snapshot/item['upstream_path'].replace('/','__')
        self.source_path.write_bytes(source)
        item['upstream_sha256']=hashlib.sha256(source).hexdigest()

    def test_end_to_end_package_is_draft_and_runs_authored_checks(self):
        files=author.render_batch(self.spec,self.snapshot)
        destination=self.base/'review'
        author.write_batch(files,destination)
        folder=destination/'problems/m18-clipped-policy-objective'
        metadata=json.loads((folder/'problem.yaml').read_text())
        self.assertEqual(metadata['status'],'draft')
        self.assertEqual(len(files),8)
        self.assertFalse(self.sentinel.exists())
        evaluator,reference={},{}
        helpers=(ROOT/'content/evaluator_helpers.py').read_text(encoding='utf-8')
        exec(helpers+'\n'+(folder/'tests_public.py').read_text(),evaluator)
        exec((folder/'solution.py').read_text(),reference)
        results=evaluator['run_tests'](reference)
        self.assertEqual(len(results),12)
        self.assertTrue(all(row['passed'] for row in results),results)
        notice=(folder/'THIRD_PARTY_NOTICE.md').read_text()
        for value in ['Copyright (c) 2024 duoan','Copyright (c) 2024 kiren','THE SOFTWARE IS PROVIDED']:
            self.assertIn(value,notice)
            self.assertIn(value,(folder/'solution.py').read_text())
        provenance=json.loads((destination/'provenance.json').read_text())
        self.assertEqual(provenance['items'][0]['status'],'draft')
        self.assertEqual(provenance['items'][0]['upstream_sha256'],self.spec['items'][0]['upstream_sha256'])

    def test_changed_source_or_license_is_rejected(self):
        original=self.source_path.read_bytes()
        self.source_path.write_bytes(original+b'# changed')
        with self.assertRaisesRegex(ValueError,'Source hash mismatch'):
            author.render_batch(self.spec,self.snapshot)
        self.source_path.write_bytes(original)
        (self.snapshot/'LICENSE').write_text('changed license')
        with self.assertRaisesRegex(ValueError,'License hash mismatch'):
            author.render_batch(self.spec,self.snapshot)

    def test_existing_directory_is_never_overwritten(self):
        destination=self.base/'review'
        destination.mkdir()
        sentinel=destination/'learner-work.txt'
        sentinel.write_text('keep this')
        with self.assertRaises(FileExistsError):
            author.write_batch(author.render_batch(self.spec,self.snapshot),destination)
        self.assertEqual(sentinel.read_text(),'keep this')
        self.assertEqual(len(list(destination.iterdir())),1)

    def test_path_traversal_and_unpinned_source_are_rejected(self):
        for key,value in [('slug','../escape'),('upstream_path','../outside.py')]:
            spec=copy.deepcopy(self.spec); spec['items'][0][key]=value
            with self.subTest(field=key),self.assertRaises(ValueError):
                author.render_batch(spec,self.snapshot)
        self.spec['source']['revision']='main'
        with self.assertRaisesRegex(ValueError,'full source commit'):
            author.render_batch(self.spec,self.snapshot)

    def test_bad_later_entry_fails_before_any_output_is_written(self):
        second=copy.deepcopy(self.spec['items'][0])
        second.update(id='m999',slug='another-distinct-objective',code='def broken(')
        self.spec['items'].append(second)
        with self.assertRaises(SyntaxError):
            author.render_batch(self.spec,self.snapshot)
        self.assertEqual([p.name for p in self.base.iterdir()],['snapshot'])
        self.assertFalse(self.sentinel.exists())

    def test_duplicate_objectives_and_misaligned_samples_fail(self):
        duplicate=copy.deepcopy(self.spec)
        duplicate['items'].append(copy.deepcopy(duplicate['items'][0]))
        with self.assertRaisesRegex(ValueError,'Duplicate ID or slug'):
            author.render_batch(duplicate,self.snapshot)
        self.spec['items'][0]['cases'][0][0]='Not the first example'
        with self.assertRaisesRegex(ValueError,'First three cases'):
            author.render_batch(self.spec,self.snapshot)

    def test_unsupported_license_is_not_relabelled(self):
        self.spec['source']['license']='proprietary'
        with self.assertRaisesRegex(ValueError,'reviewed MIT sources only'):
            author.render_batch(self.spec,self.snapshot)


if __name__ == '__main__':
    unittest.main()
