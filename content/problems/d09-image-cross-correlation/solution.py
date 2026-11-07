# Adapted from Dive into Deep Learning corr2d (MIT-0).
# https://github.com/d2l-ai/d2l-en/blob/23d7a5aecceee57d1292c56e90cce307f183bb0a/chapter_convolutional-neural-networks/conv-layer.md
# Original validation and NumPy adaptation: ZeroShot contributors, Apache-2.0.
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import numpy as np


def _array(value, rank):
    a = np.asarray(value, dtype=float)
    if a.ndim != rank or not np.all(np.isfinite(a)):
        raise ValueError("Expected a finite numeric array of the specified rank")
    return a


def cross_correlate(image, kernel):
    image, kernel = _array(image, 2), _array(kernel, 2)
    if min(image.shape + kernel.shape) < 1 or any(k > n for k,n in zip(kernel.shape,image.shape)):
        raise ValueError("Kernel must fit a nonempty image")
    h, w = kernel.shape
    output = np.zeros((image.shape[0]-h+1, image.shape[1]-w+1))
    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            output[i,j] = np.sum(image[i:i+h,j:j+w] * kernel)
    return output
