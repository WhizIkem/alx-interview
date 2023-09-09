#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

// Define the URL to fetch the movie data
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

// Function to fetch character names and print them
function fetchAndPrintCharacterNames(url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      process.exit(1);
    }

    if (response.statusCode !== 200) {
      console.error('Invalid response:', response.statusCode);
      process.exit(1);
    }

    try {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;

      if (!Array.isArray(characterUrls)) {
        console.error('Character URLs are not an array.');
        process.exit(1);
      }

      // Fetch character names
      characterUrls.forEach((characterUrl) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error('Error:', charError);
            process.exit(1);
          }

          if (charResponse.statusCode !== 200) {
            console.error('Invalid response:', charResponse.statusCode);
            process.exit(1);
          }

          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        });
      });
    } catch (parseError) {
      console.error('Error parsing movie data:', parseError);
      process.exit(1);
    }
  });
}

fetchAndPrintCharacterNames(movieUrl);