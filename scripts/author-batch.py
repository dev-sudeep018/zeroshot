"""Package locally authored JSON into reviewable drafts. Never execute source snapshots."""
import argparse
import ast
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value, minimum=1):
    return isinstance(value, str) and len(value.strip()) >= minimum


def render_batch(spec, snapshot):
    """Validate all entries before returning any file content; no writes or execution."""
    require(spec.get('schema_version') == 1, 'Unsupported batch schema')
    source = spec['source']
    revision, repository = source['revision'], source['repository']
    require(re.fullmatch(r'[0-9a-f]{40}', revision), 'Pin a full source commit')
    require(re.fullmatch(r'https://github\.com/[\w.-]+/[\w.-]+', repository), 'Use a GitHub repository URL')
    require(source['license'] == 'MIT', 'This adapter handles reviewed MIT sources only')
    snapshot = pathlib.Path(snapshot).resolve(strict=True)
    license_bytes = (snapshot/'LICENSE').read_bytes()
    require(hashlib.sha256(license_bytes).hexdigest() == source['license_sha256'], 'License hash mismatch')
    license_text = license_bytes.decode('utf-8')
    require('Permission is hereby granted' in license_text and 'THE SOFTWARE IS PROVIDED' in license_text, 'Missing full MIT notice')
    helpers = (ROOT/'scripts/authoring/numpy_helpers.py').read_text(encoding='utf-8')
    items = spec['items']
    require(isinstance(items,list) and len(items)>0, 'An authored batch must not be empty')
    files, ids, slugs, records = {}, set(), set(), []
    for item in items:
        identifier, slug = item['id'], item['slug']
        require(re.fullmatch(r'[mde][0-9]{2,5}',identifier), 'Invalid lesson ID')
        require(re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug), 'Invalid lesson slug')
        require(identifier not in ids and slug not in slugs, 'Duplicate ID or slug in batch')
        ids.add(identifier); slugs.add(slug)
        source_path = item['upstream_path']
        require(isinstance(source_path,str) and re.fullmatch(r'[\w./-]+\.py',source_path), 'Invalid upstream path')
        parts = pathlib.PurePosixPath(source_path)
        require(not parts.is_absolute() and '..' not in parts.parts, 'Upstream path must stay inside snapshot')
        # Support normal checkouts and the existing flat source-text cache.
        upstream = snapshot.joinpath(*parts.parts)
        if not upstream.is_file():
            upstream = snapshot/source_path.replace('/','__')
        require(upstream.resolve().is_relative_to(snapshot), 'Source escapes snapshot')
        digest = hashlib.sha256(upstream.read_bytes()).hexdigest()
        require(digest == item['upstream_sha256'], f'Source hash mismatch: {source_path}')
        require(text(item['title'],5) and len(item['title'])<=100, 'Invalid title')
        require(text(item['intro'],20) and len(item['intro'])<=300, 'Intro must fit the catalog summary')
        require(text(item['task'],20), 'Missing original learning task')
        require(text(item['changes'],20), 'Describe the changes from upstream')
        require(isinstance(item['skills'],list) and item['skills'] and all(text(s) for s in item['skills']), 'Missing skills')
        require(isinstance(item['prerequisites'],list) and all(re.fullmatch(r'[mde][0-9]{2,5}',p) for p in item['prerequisites']), 'Invalid prerequisite IDs')
        require(len(item['requirements'])>=3 and all(text(v,10) for v in item['requirements']), 'Need three explicit requirements')
        require(len(item['examples'])==3 and all(all(text(e.get(k)) for k in ('name','input','output')) for e in item['examples']), 'Need three complete worked examples')
        require(len(item['hints'])>=2 and all(text(h.get('title')) and text(h.get('body'),10) for h in item['hints']), 'Need progressive hints')
        require(len(item['explanation'])>=2 and all(text(v,20) for v in item['explanation']), 'Need an explanation of the operation')
        cases = item['cases']
        require(isinstance(cases,list) and 10<=len(cases)<=40, 'Need 10 to 40 public cases')
        require(all(isinstance(c,list) and len(c)==2 and all(text(v) for v in c) for c in cases), 'Cases are name/expression pairs')
        require(len({c[0] for c in cases})==len(cases), 'Public case names must be distinct')
        require([e['name'] for e in item['examples']]==[c[0] for c in cases[:3]], 'First three cases must match the worked examples')
        fn = item['fn']
        require(re.fullmatch(r'[a-z_][a-z_0-9]*',fn), 'Invalid entrypoint')
        signature = ast.parse('def '+item['signature']+':\n    pass\n')
        require(len(signature.body)==1 and isinstance(signature.body[0],ast.FunctionDef) and signature.body[0].name==fn, 'Signature must define only the entrypoint')
        code = ast.parse(item['code'])
        require(any(isinstance(node,ast.FunctionDef) and node.name==fn for node in code.body), 'Reference must define the entrypoint')
        compile(helpers+'\n'+item['code'],identifier,'exec')
        for _, expression in cases:
            compile(expression,identifier,'eval')
        url = f'{repository}/blob/{revision}/{source_path}'
        notice = f'Adapted from {source["name"]}. Source: {url}\nChanges: {item["changes"]}\n\n{license_text}'
        header = '\n'.join('# '+line if line else '#' for line in notice.splitlines())+'\n\n'
        folder = identifier+'-'+slug
        prefix = 'problems/'+folder+'/'
        problem = dict(schema_version=1,id=identifier,kind='lesson',slug=slug,version=1,title=item['title'],summary=item['intro'],domain={'m':'foundations','d':'deep-learning','e':'engineering'}[identifier[0]],difficulty='intermediate',skills=item['skills'],prerequisites=item['prerequisites'],assumed_knowledge=['Python functions','NumPy array shapes and broadcasting'],runtime=dict(engine='pyodide',packages=['numpy']),evaluation=dict(entrypoint=fn,absolute_tolerance=1e-7,relative_tolerance=1e-6),estimated_minutes=30,status='draft',author='ZeroShot contributors',license='CC-BY-SA-4.0',code_license='Apache-2.0',attribution=[f'Adapted MIT implementation: {url}', 'Upstream terms and full copyright notices remain in solution.py and THIRD_PARTY_NOTICE.md. Original additions: Apache-2.0; original prose: CC-BY-SA-4.0.'])
        lesson = {key:item[key] for key in ('intro','task','signature','requirements','examples','hints','explanation')}
        lesson.update(formula=None,test_count=len(cases),sample_count=3)
        files[prefix+'problem.yaml'] = json.dumps(problem,indent=2)+'\n'
        files[prefix+'lesson.json'] = json.dumps(lesson,indent=2)+'\n'
        files[prefix+'solution.py'] = header+helpers+'\n'+item['code'].rstrip()+'\n'
        files[prefix+'starter.py'] = 'import numpy as np\n\ndef '+item['signature']+':\n    """Implement the documented operation; leave inputs unchanged."""\n    raise NotImplementedError("Start with the worked examples")\n'
        expressions = ',\n'.join('        ('+repr(name)+', lambda f: '+expression+')' for name,expression in cases)
        files[prefix+'tests_public.py'] = 'def run_tests(namespace, mode="all"):\n    cases = [\n'+expressions+'\n    ]\n    return run_cases(namespace, '+repr(fn)+', cases, mode)\n'
        files[prefix+'explanation.md'] = '# '+item['title']+'\n\n'+'\n\n'.join(item['explanation'])+'\n\nAdapted code source: '+url+'\n'
        files[prefix+'THIRD_PARTY_NOTICE.md'] = notice.rstrip()+'\n'
        records.append(dict(id=identifier,folder=folder,upstream_path=source_path,upstream_url=url,upstream_sha256=digest,use='code-adaptation',status='draft',public_cases=len(cases),changes=item['changes'],notice=prefix+'THIRD_PARTY_NOTICE.md'))
    manifest = dict(schema_version=1,source=repository,revision=revision,license='MIT',upstream_license_sha256=source['license_sha256'],items=records)
    files['provenance.json'] = json.dumps(manifest,indent=2)+'\n'
    return files


def write_batch(files, destination):
    # Never merge with an existing directory, even if it appears empty.
    destination = pathlib.Path(destination)
    destination.mkdir(parents=True,exist_ok=False)
    for name, contents in files.items():
        target = destination/name
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(contents,encoding='utf-8',newline='\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('spec',type=pathlib.Path)
    parser.add_argument('--snapshot',required=True,type=pathlib.Path)
    parser.add_argument('--output',required=True,type=pathlib.Path,help='New review directory, outside content/problems')
    parser.add_argument('--dry-run',action='store_true')
    args = parser.parse_args()
    require(not args.output.resolve().is_relative_to((ROOT/'content/problems').resolve()), 'Author into a review directory, not the published catalog')
    spec = json.loads(args.spec.read_text(encoding='utf-8'))
    files = render_batch(spec,args.snapshot)
    require(not args.output.exists(),'Output directory already exists; no files replaced')
    if not args.dry_run:
        write_batch(files,args.output)
    count = len(spec['items'])
    print(f'{"Validated" if args.dry_run else "Staged"} {count} draft lessons / {sum(len(i["cases"]) for i in spec["items"])} public cases / {len(files)} files. Publication still requires editorial, native and browser checks.')


if __name__ == '__main__':
    main()
