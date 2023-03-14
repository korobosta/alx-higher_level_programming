#!/usr/bin/node
if (process.argv.length === 5) {
  const fs = require('fs');
  const textOne = fs.readFileSync(process.argv[2]).toString();
  const textTwo = fs.readFileSync(process.argv[3]).toString();
  fs.writeFile(process.argv[4], textOne + textTwo, function (err) {
    if (err) throw err;
  });
}
