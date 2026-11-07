# Simulate a FIFO Work Queue

A FIFO queue models workers accepting tasks in arrival order. Replaying operations makes both completed and waiting work visible.

An attempted removal from an empty queue is recorded explicitly. Skipping that result would lose alignment between take operations and returned responses.
