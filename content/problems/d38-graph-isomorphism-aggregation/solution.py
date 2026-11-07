# Adapted from Pyre-Code / TorchCode. Source: https://github.com/whwangovo/pyre-code/blob/7ede95b47437798c74023a0ffae8fb33bbeebc2e/torch_judge/tasks/gin_layer.py
# Changes: Ported the upstream GIN sum-and-MLP equation to NumPy with explicit edge direction, supplied weights and strict shapes. Kept the final output linear and epsilon unrestricted in sign. Original lesson prose and tests.
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


def gin_layer(adjacency, features, w1, b1, w2, b2, epsilon=0.0):
    adjacency, features, w1, b1, w2, b2 = [_array(v) for v in (adjacency,features,w1,b1,w2,b2)]
    epsilon = _scalar(epsilon)
    if features.ndim != 2 or any(n == 0 for n in features.shape) or adjacency.shape != (features.shape[0],features.shape[0]) or np.any(adjacency < 0) or np.any(np.diag(adjacency) != 0):
        raise ValueError("Invalid graph or features")
    if w1.ndim != 2 or any(n == 0 for n in w1.shape) or w1.shape[0] != features.shape[1] or b1.shape != (w1.shape[1],) or w2.ndim != 2 or w2.shape[0] != w1.shape[1] or w2.shape[1] == 0 or b2.shape != (w2.shape[1],):
        raise ValueError("Invalid MLP weights or biases")
    combined = (1+epsilon)*features+adjacency@features
    hidden = np.maximum(combined@w1+b1,0)
    return hidden@w2+b2
