#!/usr/bin/node

// 1. Create a new function that returns a promise
function firstFunction (char) {
  const request = require('request');
  return new Promise((resolve, reject) => {
    request(char, function (err, res, body) {
      if (res.statusCode === 200) {
        resolve(JSON.parse(body).name);
      } else {
        reject(err);
      }
    });
  });
}

// 2. Create an async function
async function secondFunction (body) {
  for (const char of JSON.parse(body).characters) {
    console.log(await firstFunction(char));
  }
}

if (process.argv.length === 3) {
  const request = require('request');
  request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`, function (err, res, body) {
    if (res.statusCode === 200) {
      secondFunction(body);
    } else {
      console.log(err);
    }
  });
}
