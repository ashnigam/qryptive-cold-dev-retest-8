from cryptography.hazmat.primitives.ciphers.aead import AESGCM
small = AESGCM.generate_key(bit_length=256)
large = AESGCM.generate_key(bit_length=256)
def encrypt_pair(nonce, payload):
    return AESGCM(small).encrypt(nonce, payload, None), AESGCM(large).encrypt(nonce, payload, None)
