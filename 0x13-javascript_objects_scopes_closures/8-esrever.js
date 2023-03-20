#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  for (const value of list) {
    newList.unshift(value);
  }
  return newList;
};
