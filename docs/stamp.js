const c = require('crypto');
exports.stamp = x => c.createHash('sha1').update(x).digest();
