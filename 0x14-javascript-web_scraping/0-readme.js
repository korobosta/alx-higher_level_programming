#!/usr/bin/node
if (process.argv.length === 3) {
  const fs = require('fs');
  fs.readFile(process.argv[2], 'utf-8', function (err, data) {
    if (err) {
      console.log(err);
    } else {
      console.log(data);
    }
  });
}
