import ssl, hashlib, hmac
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, ec, ed25519, x25519, dh, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from Crypto.Cipher import DES, DES3, ARC4, Blowfish
from Crypto.Hash import MD5

def receipt_signature(payload):
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return key.sign(payload, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=32), hashes.SHA256())

def elliptic_receipt(payload):
    signer = ec.generate_private_key(ec.SECP256R1())
    return signer.sign(payload, ec.ECDSA(hashes.SHA256()))

def modern_receipt(payload):
    signer = ed25519.Ed25519PrivateKey.generate()
    return signer.sign(payload)

def shared_route(peer):
    key = x25519.X25519PrivateKey.generate()
    return key.exchange(peer)

def elliptic_route(peer):
    local = ec.generate_private_key(ec.SECP256R1())
    return local.exchange(ec.ECDH(), peer)

def seal(payload, nonce):
    key = AESGCM.generate_key(bit_length=128)
    return AESGCM(key).encrypt(nonce, payload, None)

def legacy_ticket(payload):
    key = b'12345678'
    return DES.new(key, DES.MODE_ECB).encrypt(payload)

def checksums(payload):
    first = hashes.Hash(hashes.MD5())
    first.update(payload)
    return hashlib.md5(payload).digest(), hashlib.sha1(payload).digest(), MD5.new(payload).digest()

def mac(payload):
    return hmac.new(b'disposable', payload, hashlib.sha1).digest()

def old_ciphers(payload):
    triple = DES3.new(b'0123456789abcdefghijklmn', DES3.MODE_ECB)
    stream = ARC4.new(b'1234567890123456')
    blow = Blowfish.new(b'12345678', Blowfish.MODE_ECB)
    return triple, stream, blow

plain_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
server_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
server_context.minimum_version = ssl.TLSVersion.TLSv1
server_context.load_cert_chain('assets/parcel.pem', 'assets/parcel.key')
