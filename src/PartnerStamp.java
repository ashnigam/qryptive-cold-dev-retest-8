package parcel;
import java.security.*;
import javax.crypto.*;
import javax.crypto.spec.*;
public class PartnerStamp {
  public byte[] stamp(byte[] data) throws Exception {
    KeyPairGenerator rsa = KeyPairGenerator.getInstance("RSA");
    rsa.initialize(2048);
    KeyPair pair = rsa.generateKeyPair();
    Signature sig = Signature.getInstance("SHA256withRSA");
    sig.initSign(pair.getPrivate()); sig.update(data);
    return sig.sign();
  }
  public void curves(byte[] data) throws Exception {
    KeyPairGenerator ec = KeyPairGenerator.getInstance("EC");
    ec.initialize(256); KeyPair pair = ec.generateKeyPair();
    Signature sig = Signature.getInstance("SHA256withECDSA");
    sig.initSign(pair.getPrivate()); sig.update(data); sig.sign();
    KeyPairGenerator.getInstance("Ed25519").generateKeyPair();
    Signature.getInstance("Ed25519");
    KeyAgreement.getInstance("ECDH");
    KeyAgreement.getInstance("X25519");
    KeyAgreement.getInstance("DH");
    KeyAgreement.getInstance("DiffieHellman");
  }
  public void symmetric() throws Exception {
    KeyGenerator small = KeyGenerator.getInstance("AES");
    small.init(128); SecretKey shortKey = small.generateKey();
    KeyGenerator large = KeyGenerator.getInstance("AES");
    large.init(256); SecretKey longKey = large.generateKey();
    Cipher gcm = Cipher.getInstance("AES/GCM/NoPadding");
    gcm.init(Cipher.ENCRYPT_MODE, longKey, new GCMParameterSpec(128, new byte[12]));
    Cipher.getInstance("DES/ECB/PKCS5Padding");
    Cipher.getInstance("DESede/CBC/PKCS5Padding");
    Cipher.getInstance("RC4");
    Cipher.getInstance("Blowfish/CBC/PKCS5Padding");
    MessageDigest.getInstance("MD5");
    MessageDigest.getInstance("SHA-1");
    Mac.getInstance("HmacSHA1");
  }
}
