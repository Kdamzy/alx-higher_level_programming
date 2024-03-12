#!/usr/bin/node

/* Define a square that define a square and inherits from square */
const subSquare = require('./5-square');

class Square extends subSquare {
  charPrint (c) {
    if (c === null) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
