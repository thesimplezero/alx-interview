#!/usr/bin/node
const request = require('request');

/**
 * Fetches character data from a given character URL.
 * @param {string} characterUrl - The URL of the character.
 * @returns {Promise<string>} A promise that resolves with the character's name.
 */
const fetchCharacter = (characterUrl) => {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const character = JSON.parse(body);
        resolve(character.name);
      } else {
        reject(error || `Failed to fetch character from ${characterUrl}`);
      }
    });
  });
};

/**
 * Fetches movie data and logs character names.
 * @param {string} movieId - The ID of the movie to fetch.
 */
const fetchMovieCharacters = (movieId) => {
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode === 404) {
      console.error('Error: Movie not found (404)');
    } else if (response.statusCode !== 200) {
      console.error('Error: Unexpected response:', response.statusCode);
    } else {
      const film = JSON.parse(body);
      if (film && film.characters && Array.isArray(film.characters)) {
        const promises = film.characters.map(characterUrl => fetchCharacter(characterUrl));
        Promise.all(promises)
          .then(characters => {
            characters.forEach(characterName => console.log(characterName));
          })
          .catch(err => {
            console.error('Error fetching characters:', err);
          });
      } else {
        console.error('Invalid film data:', film);
      }
    }
  });
};

// Usage
const movieId = process.argv[2];
if (!movieId) {
  console.error('Error: Please provide a movie ID as argument.');
} else {
  fetchMovieCharacters(movieId);
}
