# Calibrate and Limit Sensor Channels

Broadcasting a channel vector across rows applies the same instrument calibration to each observation. The offset belongs after multiplication by the gain, which matters when the gain is negative.

The mask distinguishes changed measurements from values that happen to equal a limit. Keeping that mask supports auditing saturated sensors without confusing valid endpoint readings with clipping.
