#!/usr/bin/node
// Print the title of Star wars movie

const request = require('request');
const movie_id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const scripts = JSON.parse(body);
    console.log(scripts.title);
  }
});
