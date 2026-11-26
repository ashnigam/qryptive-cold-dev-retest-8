const crypto = require('crypto');
const receipt = crypto.createHash('md5').update('parcel').digest('hex');
