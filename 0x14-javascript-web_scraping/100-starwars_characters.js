#!/usr/bin/node
// prints all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const scripts = JSON.parse(body);
    const characters = scripts.characters;

    characters.forEach((character) => {
      request.get(character, (Error, response, Body) => {
        if (Error) {
          console.log(Error);
        } else {
          const castname = JSON.parse(Body);
          console.log(castname.name);
        }
      });
    });
  }
});
