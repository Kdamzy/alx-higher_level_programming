#!/usr/bin/node

/* script that prints the addition of two numbers */
function add (a, b) {
  const result = a + b;
  return result;
}
const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (!isNaN(arg1) && !isNaN(arg2)) {
  console.log(add(arg1, arg2));
} else {
  console.log('NaN');
}
