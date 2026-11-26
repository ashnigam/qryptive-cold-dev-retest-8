package parcel
import (
 "crypto/rand"
 "crypto/rsa"
 "crypto/ecdsa"
 "crypto/elliptic"
 "crypto/ed25519"
 "crypto/ecdh"
 "crypto/sha256"
 "crypto/md5"
 "crypto/sha1"
 "crypto/hmac"
 "crypto/aes"
 "crypto/cipher"
 "crypto/des"
 "crypto/rc4"
 "crypto/tls"
 "crypto"
)
func Receipt(data []byte) {
 r, _ := rsa.GenerateKey(rand.Reader, 2048)
 digest := sha256.Sum256(data)
 rsa.SignPKCS1v15(rand.Reader, r, crypto.SHA256, digest[:])
 e, _ := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
 ecdsa.SignASN1(rand.Reader, e, digest[:])
 _, ed, _ := ed25519.GenerateKey(rand.Reader)
 ed25519.Sign(ed, data)
 x, _ := ecdh.X25519().GenerateKey(rand.Reader)
 peer, _ := ecdh.X25519().GenerateKey(rand.Reader)
 x.ECDH(peer.PublicKey())
 p, _ := ecdh.P256().GenerateKey(rand.Reader)
 p.ECDH(p.PublicKey())
 short := make([]byte, 16)
 long := make([]byte, 32)
 aes.NewCipher(short)
 block, _ := aes.NewCipher(long)
 cipher.NewGCM(block)
 md5.Sum(data)
 sha1.Sum(data)
 hmac.New(sha1.New, short)
 des.NewCipher(short[:8])
 des.NewTripleDESCipher(make([]byte, 24))
 rc4.NewCipher(short)
 _ = tls.Config{MinVersion: tls.VersionTLS10}
 _ = tls.Config{MinVersion: tls.VersionTLS11}
}
