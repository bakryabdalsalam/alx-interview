#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, response, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters; 
  exact0rder(actors, 0);
});
const exact0rder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, response, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exact0rder(actors, x + 1);
  });
};