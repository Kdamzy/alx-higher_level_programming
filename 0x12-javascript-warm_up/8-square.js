#!/usr/bin/node

/* script that print a square */
const size = process.argv[2];
const square = parseInt(size);

if (!isNaN(square)) {
  for (let i = 0; i < square; i++) {
    let line = '';
    for (let j = 0; j < square; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
