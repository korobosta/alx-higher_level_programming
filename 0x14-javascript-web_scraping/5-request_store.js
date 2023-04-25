#!/usr/bin/node
if (process.argv.length === 4) {
  const fs = require('fs');
  const request = require('request');
  request(process.argv[2], function (err, res, body) {
    if (res.statusCode === 200) {
      fs.writeFile(process.argv[3], body, 'utf8', function (err) {
        if (err) {
          console.log(err);
        }
      });
    } else {
      console.log(err);
    }
  });
}
