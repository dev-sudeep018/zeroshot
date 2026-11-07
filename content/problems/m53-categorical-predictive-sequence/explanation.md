# Score a Sequence while Updating Category Beliefs

Each observation changes the next predictive distribution because the concentration vector accumulates evidence. A repeated category becomes more probable than it was under the initial prior.

Although individual step probabilities depend on order, the product for a complete ordered sequence depends only on its category counts. A count-event probability would also include how many different sequences have those counts.
