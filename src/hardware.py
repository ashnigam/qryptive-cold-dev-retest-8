from tpm2_pytss import ESAPI, TPM2B_PUBLIC, TPMT_SIG_SCHEME, TPM2_ALG, TPMT_TK_HASHCHECK, TPM2_ST, ESYS_TR

def device_receipt(digest):
    with ESAPI() as tpm:
        handle, public, creation, creation_hash, ticket = tpm.create_primary(in_public=TPM2B_PUBLIC.parse('rsa2048:rsassa-sha256'), primary_handle=ESYS_TR.OWNER)
        scheme = TPMT_SIG_SCHEME(scheme=TPM2_ALG.RSASSA)
        signature = tpm.sign(handle, digest, scheme, TPMT_TK_HASHCHECK(tag=TPM2_ST.HASHCHECK, hierarchy=ESYS_TR.NULL))
        return signature
