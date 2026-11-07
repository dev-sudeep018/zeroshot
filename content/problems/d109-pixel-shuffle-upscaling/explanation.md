# Move Subpixel Channels into Image Space

Pixel shuffle exchanges channel resolution for spatial resolution without creating new values. A preceding learned layer is responsible for predicting the subpixel channel values.

The mapping convention fixes which channel becomes which pixel offset. Merely repeating input pixels or reshaping without the required axis permutation produces a different image.
