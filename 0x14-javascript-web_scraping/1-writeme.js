#!/usr/bin/node
if (process.argv.length === 4) {
  const fs = require('fs');
  const userInput = process.argv[3];
  fs.writeFile(process.argv[2], userInput, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
}
