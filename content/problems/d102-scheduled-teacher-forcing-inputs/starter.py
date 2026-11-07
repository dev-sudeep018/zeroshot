import numpy as np


def teacher_forcing_inputs(targets, predictions, draws, teacher_probability, start_id):
    """Build decoder input tokens, beginning with a start token and then selecting the previous gold or predicted token."""
    # Choose the previous token before shifting it into the next input position.
    # At probability zero use predictions everywhere after the start; at one use gold tokens everywhere.
    raise NotImplementedError("Implement the operation and validate its inputs")
