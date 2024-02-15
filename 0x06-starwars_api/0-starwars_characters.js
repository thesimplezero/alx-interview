#!/usr/bin/node
// Script to print all the characters of a Star Wars movie

const request = require('request');

// Function to fetch character name from character URL
const getCharacterName = async (characterUrl) => {
  try {
    const response = await fetch(characterUrl);
    const character = await response.json();
    return character.name;
  } catch (error) {
    throw new Error(`Error fetching character name: ${error}`);
  }
};

// Function to fetch characters from a movie
const getMovieCharacters = async (movieId) => {
  try {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
    const response = await fetch(url);
    const movie = await response.json();
    return movie.characters;
  } catch (error) {
    throw new Error(`Error fetching characters: ${error}`);
  }
};

// Function to print characters of a movie
const printCharacters = async (movieId) => {
  try {
    const characters = await getMovieCharacters(movieId);
    for (const characterUrl of characters) {
      const characterName = await getCharacterName(characterUrl);
      console.log(characterName);
    }
  } catch (error) {
    console.error(error.message);
  }
};

// Main function
const main = async () => {
  try {
    const movieId = process.argv[2];
    if (!movieId) {
      throw new Error('Please provide a Movie ID as a command line argument.');
    }
    await printCharacters(movieId);
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
};

main();
