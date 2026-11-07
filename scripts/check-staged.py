"""Executable package contracts for staged authoring; input is schema-checked JSON.

This is a mechanical gate, not an independent mathematical/content review.
"""
import ast
import copy
import json
from numbers import Real
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
HELPERS = (ROOT / "content/evaluator_helpers.py").read_text(encoding="utf-8")


def plain(value):
    if isinstance(value, np.ndarray):
        return plain(value.tolist())
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, dict):
        return {key: plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [plain(item) for item in value]
    return value


def equal(actual, shown):
    actual, shown = plain(actual), plain(shown)
    if isinstance(actual, dict):
        assert isinstance(shown, dict) and actual.keys() == shown.keys()
        for key in actual:
            equal(actual[key], shown[key])
    elif isinstance(actual, list):
        assert isinstance(shown, list) and len(actual) == len(shown)
        for a, b in zip(actual, shown):
            equal(a, b)
    elif isinstance(actual, Real) and not isinstance(actual, bool):
        assert isinstance(shown, Real) and not isinstance(shown, bool)
        np.testing.assert_allclose(actual, shown, atol=1e-9, rtol=1e-8)
    else:
        assert actual == shown, (actual, shown)


def check(entry):
    problem, lesson = entry["problem"], entry["lesson"]
    evaluator, reference, starter = {}, {}, {}
    exec(compile(HELPERS + "\n" + entry["tests"], "tests_public.py", "exec"), evaluator)
    exec(compile(entry["solution"], "solution.py", "exec"), reference)
    exec(compile(entry["starter"], "starter.py", "exec"), starter)
    run_tests = evaluator["run_tests"]
    results = run_tests(reference, "all")
    assert len(results) == lesson["test_count"], "Public case count mismatch"
    assert all(result["passed"] for result in results), results
    assert not all(result["passed"] for result in run_tests(starter, "all")), "Starter passes"
    samples = run_tests(reference, "sample")
    assert len(samples) == lesson["sample_count"] == 3
    assert [r["name"] for r in samples] == [e["name"] for e in lesson["examples"]]
    for example in lesson["examples"]:
        # The display convention allows an explanatory parenthesis after a literal.
        shown = ast.literal_eval(example["output"].split("\n(", 1)[0])
        equal(eval(example["input"], reference), shown)
    first = eval(lesson["examples"][0]["input"], reference)
    for wrong in (None, 0, [], first):
        candidate = {problem["evaluation"]["entrypoint"]: lambda *a, **kw: copy.deepcopy(wrong)}
        assert not all(r["passed"] for r in run_tests(candidate, "all")), "Canned answer passes"
    return len(results)


entries = json.load(sys.stdin)
total = 0
for entry in entries:
    try:
        total += check(entry)
    except Exception as error:
        raise AssertionError(f"{entry['problem']['id']}: {error}") from error
print(f"Native contracts passed: {len(entries)} drafts / {total} cases; examples, samples, starters and canned answers checked.")
