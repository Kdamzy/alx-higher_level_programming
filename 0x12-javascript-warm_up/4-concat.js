#!/usr/bin/node

/* script that prints two arguments passed to it, in the following format: “ is ” */
const fristargs = process.argv[2];
const secondargs = process.argv[3];

console.log(fristargs + ' is ' + secondargs);
