"""Defensive cryptography demonstration for Project-1."""

import os
import hashlib
import hmac
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import bcrypt


def aes_gcm_demo(data: bytes):
    key = AESGCM.generate_key(bit_length=256)
    iv = os.urandom(12)
    box = AESGCM(key)
    encrypted = box.encrypt(iv, data, None)
    decrypted = box.decrypt(iv, encrypted, None)
    return decrypted == data


def rsa_signature_demo(data: bytes):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    signature = private_key.sign(data, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
    public_key.verify(signature, data, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
    return True


def hmac_demo(data: bytes):
    secret = os.urandom(32)
    tag = hmac.new(secret, data, hashlib.sha256).digest()
    return hmac.compare_digest(tag, hmac.new(secret, data, hashlib.sha256).digest())


def bcrypt_demo(value: str):
    stored = bcrypt.hashpw(value.encode(), bcrypt.gensalt(rounds=12))
    return bcrypt.checkpw(value.encode(), stored)


if __name__ == "__main__":
    sample = b"Project-1 cryptography test"
    print("AES-256-GCM:", aes_gcm_demo(sample))
    print("RSA-2048/PSS:", rsa_signature_demo(sample))
    print("HMAC-SHA-256:", hmac_demo(sample))
    print("bcrypt:", bcrypt_demo("demo-value"))
