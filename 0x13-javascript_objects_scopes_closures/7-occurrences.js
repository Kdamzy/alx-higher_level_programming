#!/usr/bin/node

/* Define a square that define a square and inherits from square */
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((a, v) => (v === searchElement ? a + 1 : a), 0);
};
