#!/usr/bin/node
if (process.argv.length === 3) {
  const request = require('request');
  request(process.argv[2], function (err, res, body) {
    if (res.statusCode === 200) {
      const users = JSON.parse(body);
      const usersDict = {};
      for (const user of users) {
        if (user.completed === true) {
          if (usersDict[user.userId] === undefined) {
            usersDict[user.userId] = 0;
          }
          usersDict[user.userId] += 1;
        }
      }
      console.log(usersDict);
    } else {
      console.log(err);
    }
  });
}
