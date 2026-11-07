# Separate a Forecast from Its Update

The ordering of prediction and update is the central lesson. Returning the updated level as the forecast would use information that was unavailable at prediction time.

Alpha controls how quickly older information fades. At zero the initial level never changes, while at one the next forecast becomes the previous observation.
