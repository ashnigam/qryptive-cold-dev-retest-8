package sample
import "crypto/md5"
func Digest(p []byte) [16]byte { return md5.Sum(p) }
