import { createHash } from 'node:crypto';
export const hash = (p: string) => createHash('md5').update(p).digest();
