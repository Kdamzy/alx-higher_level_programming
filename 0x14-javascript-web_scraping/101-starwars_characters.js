#!/usr/bin/node
// prints all characters of a Star Wars movie

const request = require('request');
const movieid = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieid}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const scripts = JSON.parse(body);
    const characters = scripts.characters;

    for (const character of characters) {
      request.get(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const castname = JSON.parse(body);
          console.log(castname.name);
        }
      });
    }
  }
});
