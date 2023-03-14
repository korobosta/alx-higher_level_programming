#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const value of list) {
    if (value === searchElement) {
      count++;
    }
  }
  return count;
};
