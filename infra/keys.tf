resource "aws_kms_key" "receipt" {
 key_usage = "SIGN_VERIFY"
 customer_master_key_spec = "RSA_2048"
}
resource "azurerm_key_vault_key" "receipt" {
 name = "parcel"
 key_type = "RSA"
 key_size = 2048
}
resource "google_kms_crypto_key" "receipt" {
 name = "parcel"
 purpose = "ASYMMETRIC_SIGN"
 version_template { algorithm = "RSA_SIGN_PKCS1_2048_SHA256" }
}
resource "vault_transit_secret_backend_key" "receipt" {
 name = "parcel"
 type = "ecdsa-p256"
}
