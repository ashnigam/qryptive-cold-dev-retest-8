import * as crypto from 'node:crypto';
import { generateKeyPair, CompactEncrypt, SignJWT } from 'jose';
export async function envelope(payload: Uint8Array) {
  const { publicKey } = await generateKeyPair('RSA-OAEP');
  return new CompactEncrypt(payload).setProtectedHeader({ alg: 'RSA-OAEP', enc: 'A256GCM' }).encrypt(publicKey);
}
export function stamps(payload: Buffer) {
  const rsa = crypto.generateKeyPairSync('rsa', { modulusLength: 2048 });
  const ec = crypto.generateKeyPairSync('ec', { namedCurve: 'prime256v1' });
  const ed = crypto.generateKeyPairSync('ed25519');
  crypto.sign('sha256', payload, rsa.privateKey);
  crypto.sign('sha256', payload, ec.privateKey);
  crypto.sign(null, payload, ed.privateKey);
  crypto.createECDH('prime256v1');
  crypto.generateKeyPairSync('x25519');
  crypto.createDiffieHellman(2048);
  crypto.createHash('md5').update(payload).digest();
  crypto.createHash('sha1').update(payload).digest();
  crypto.createHmac('sha1', 'test').update(payload).digest();
  crypto.createCipheriv('aes-128-gcm', Buffer.alloc(16), Buffer.alloc(12)); crypto.createCipheriv('aes-256-gcm', Buffer.alloc(32), Buffer.alloc(12));
  crypto.createCipheriv('des-ecb', Buffer.alloc(8), null);
  crypto.createCipheriv('des-ede3-cbc', Buffer.alloc(24), Buffer.alloc(8));
  crypto.createCipheriv('rc4', Buffer.alloc(16), null);
  crypto.createCipheriv('bf-cbc', Buffer.alloc(16), Buffer.alloc(8));
}
export async function token(privateKey: any) {
  return new SignJWT({ parcel: 'demo' }).setProtectedHeader({ alg: 'RS256' }).sign(privateKey);
}
