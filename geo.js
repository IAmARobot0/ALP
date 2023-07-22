var geoip = require('geoip-lite');

var ip = "144.92.135.66";
var geo = geoip.lookup(ip);

console.log(geo);
