from cryptography.hazmat.primitives.asymmetric import dh

def negotiated_secret(p, g, peer):
    params = dh.DHParameterNumbers(p, g).parameters()
    local = params.generate_private_key()
    return local.exchange(peer)

def temporary_group(peer):
    params = dh.generate_parameters(generator=2, key_size=2048)
    local = params.generate_private_key()
    return local.exchange(peer)
