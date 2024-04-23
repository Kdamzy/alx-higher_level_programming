#!/usr/bin/node
// prints the number of movies where “Wedge Antilles” appear.

const request = require('request');
let num = 0;

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const scripts = JSON.parse(body);
    scripts.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          num += 1;
        }
      });
    });
    console.log(num);
  }
});
