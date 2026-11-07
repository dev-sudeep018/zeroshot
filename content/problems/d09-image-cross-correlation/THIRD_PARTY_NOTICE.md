# Dive into Deep Learning code adaptation

Source: https://github.com/d2l-ai/d2l-en/blob/23d7a5aecceee57d1292c56e90cce307f183bb0a/chapter_convolutional-neural-networks/conv-layer.md, the PyTorch `corr2d` example.
Upstream revision: `23d7a5aecceee57d1292c56e90cce307f183bb0a`.
Upstream license: MIT No Attribution (MIT-0), as published in LICENSE-SAMPLECODE.

The reference's nested sliding-window loop is adapted to NumPy. Changes include
argument names, finite-value/shape validation, and an explicit NumPy reduction.
The lesson prose, examples, public tests, starter, and added validation are original
ZeroShot contributions. Original contributions use the repository's
Apache-2.0 code / CC-BY-SA-4.0 prose terms. The upstream permission is preserved below.

## Upstream notice

Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
