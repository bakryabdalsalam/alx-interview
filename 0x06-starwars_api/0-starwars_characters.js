#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('An error occurred:', error);
    return;
  }

  const filmData = JSON.parse(body);

  filmData.characters.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('An error occurred:', error);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});