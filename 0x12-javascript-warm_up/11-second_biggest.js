#!/usr/bin/node

/* script that searches the second biggest integer in the list */
const args = process.argv.slice(2).map(Number);
const sortnum = args.sort((a, b) => b - a);

if (sortnum.length <= 1) {
  console.log(0);
} else {
  console.log(sortnum[1]);
}
