# Adapted from Pyre-Code / TorchCode. Source: https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/torch_judge/tasks/moe_load_balance.py
# Changes: Ported the upstream top-one load-balancing statistic to NumPy with stable softmax and deterministic index-order ties. Exposed the hard fractions and mean probabilities for direct inspection. Original lesson prose and tests.
#
# MIT License
#
# This project is based on TorchCode by duoan (https://github.com/duoan/TorchCode),
# licensed under the MIT License.
#
# The `torch_judge/` package and `solutions/` notebooks are derived from the original project.
# The `web/` frontend and `grading_service/` backend are new additions.
#
# Copyright (c) 2024 duoan
# Copyright (c) 2024 kiren
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import numpy as np

def _array(value):
    try:
        raw = np.asarray(value)
        if raw.dtype.kind not in "iuf":
            raise ValueError("Use real numeric arrays")
        result = raw.astype(np.float64)
    except (TypeError, OverflowError) as exc:
        raise ValueError("Use real numeric arrays") from exc
    if not np.all(np.isfinite(result)) or np.any(np.abs(result) > 1e30):
        raise ValueError("Values must be finite with magnitude at most 1e30")
    return result

def _scalar(value):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, float, np.integer, np.floating)):
        raise ValueError("Use a real scalar")
    try:
        result = float(value)
    except OverflowError as exc:
        raise ValueError("Scalar must be finite with magnitude at most 1e30") from exc
    if not np.isfinite(result) or abs(result) > 1e30:
        raise ValueError("Scalar must be finite with magnitude at most 1e30")
    return result

def _integer(value, low, high):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)) or not low <= value <= high:
        raise ValueError("Integer parameter outside the documented bounds")
    return int(value)


def load_balance(router_logits):
    logits = _array(router_logits)
    if logits.ndim != 2 or any(n == 0 for n in logits.shape):
        raise ValueError("Use a nonempty token-by-expert matrix")
    experts = logits.shape[1]
    selected = np.argmax(logits,axis=1)
    fractions = np.bincount(selected,minlength=experts)/logits.shape[0]
    weights = np.exp(logits-logits.max(axis=1,keepdims=True))
    probabilities = (weights/weights.sum(axis=1,keepdims=True)).mean(axis=0)
    return {"fractions":fractions,"probabilities":probabilities,"loss":float(experts*np.sum(fractions*probabilities))}
