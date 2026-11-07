# Read Simple Key-Value Lines

Small configuration formats need an explicit grammar even when they look simple. Splitting only the first equals sign permits values such as tokens or expressions containing equals signs.

Rejecting duplicate keys makes ambiguity visible. A parser that silently keeps the final value can hide a copied setting or a configuration mistake.
