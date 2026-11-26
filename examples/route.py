from cryptography.hazmat.primitives.asymmetric import x25519
def route():
    return x25519.X25519PrivateKey.generate()
