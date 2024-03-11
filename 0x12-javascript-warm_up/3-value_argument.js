#!/usr/bin/node

/* script that print the first argument passed to it */
const args = process.argv[2];

if (args === undefined) {
  console.log('No argument');
} else {
  console.log(args);
}
