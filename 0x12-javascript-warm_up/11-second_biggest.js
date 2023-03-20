#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  let second = -Infinity;
  let first = parseInt(process.argv[2]);
  process.argv.slice(2).forEach(val => {
    if (parseInt(val) > first) {
      second = first;
      first = parseInt(val);
    } else if (parseInt(val) > second && parseInt(val) < first) {
      second = parseInt(val);
    }
  });
  console.log(second);
}
