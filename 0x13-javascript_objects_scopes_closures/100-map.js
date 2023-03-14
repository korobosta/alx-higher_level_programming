#!/usr/bin/node
const array = require('./100-data').list;
console.log(array);
let index = 0;
console.log(array.map(x => x * index++));
