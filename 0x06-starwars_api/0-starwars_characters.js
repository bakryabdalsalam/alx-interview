#!/usr/bin/node
const request = require('request-promise');

const printCharactersInOrder = async (characters, index = 0) => {
  if (index >= characters.length) return;

  try {
    const body = await request(characters[index]);
    console.log(JSON.parse(body).name);
    await printCharactersInOrder(characters, index + 1);
  } catch (error) {
    console.error('An error occurred:', error);
  }
};

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}`;

request(apiUrl)
  .then(body => {
    const characters = JSON.parse(body).characters;
    printCharactersInOrder(characters);
  })
  .catch(error => console.error('An error occurred:', error));