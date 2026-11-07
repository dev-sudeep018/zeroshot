# Encode Tokens with an Unknown ID

A vocabulary converts text tokens into stable integer features. Reserving a distinct unknown ID prevents an unseen token from being confused with a known token.

Unknown positions provide diagnostics without changing sequence length. Keeping alignment lets a caller inspect which original tokens caused the fallback.
