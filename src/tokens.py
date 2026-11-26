from jwcrypto import jwk, jwe
import jwt
import xmlsec

def sealed(payload):
    public = jwk.JWK.generate(kty='RSA', size=2048)
    token = jwe.JWE(payload, protected={'alg': 'RSA-OAEP', 'enc': 'A256GCM'})
    token.add_recipient(public)
    return token.serialize()

def signed(payload, key):
    return jwt.encode(payload, key, algorithm='RS256')

def saml_signature(root):
    return xmlsec.template.create(root, xmlsec.Transform.EXCL_C14N, xmlsec.Transform.RSA_SHA1)
