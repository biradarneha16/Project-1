# Secure Key Management

- Never hard-code keys, passwords, API tokens, or private keys.
- Use environment variables for local development and a managed secret manager in production.
- Generate AES keys with a cryptographically secure random source.
- Use a fresh unpredictable IV/nonce for every AES-GCM encryption with the same key.
- Keep RSA private keys secret; distribute only public keys.
- Use RSA-PSS with SHA-256 for digital signatures.
- Use bcrypt, Argon2id, or scrypt for password storage, with a unique salt and an appropriate work factor.
- Rotate keys on a defined schedule and after suspected exposure.
- Keep key versions so retained data can be decrypted during controlled rotation.
- Never commit generated keys or secrets to GitHub; revoke and rotate any exposed credential immediately.
