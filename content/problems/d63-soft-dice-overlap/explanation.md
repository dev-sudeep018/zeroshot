# Measure Soft Segmentation Overlap

The objective uses soft predicted mass, so it remains sensitive to confidence without a hard threshold. A perfectly matched binary mask has zero loss.

Smoothing both numerator and denominator gives zero loss for empty-empty masks. Other Dice conventions may use a squared denominator or different smoothing; they are outside this contract.
