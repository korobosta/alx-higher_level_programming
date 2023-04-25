#!/usr/bin/node
if (process.argv.length === 3) {
  const request = require('request');
  request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, function (err, resp, body) {
    if (resp.statusCode === 200) {
      console.log(JSON.parse(body).title);
    } else {
      console.log(err);
    }
  });
}
