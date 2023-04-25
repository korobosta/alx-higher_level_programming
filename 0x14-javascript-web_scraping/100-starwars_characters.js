#!/usr/bin/node
if (process.argv.length === 3) {
  const request = require('request');
  request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`, function (err, res, body) {
    if (res.statusCode === 200) {
      for (const char of JSON.parse(body).characters) {
        request(char, function (err, res, body) {
          if (res.statusCode === 200) {
            console.log(JSON.parse(body).name);
          } else {
            console.log(err);
          }
        });
      }
    } else {
      console.log(err);
    }
  });
}
