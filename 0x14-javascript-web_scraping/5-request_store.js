#!/usr/bin/node
// gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');

request.get(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
