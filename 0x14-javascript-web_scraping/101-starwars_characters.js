// #!/usr/bin/node

// const request = require('request');
// const id = process.argv[2];
// const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

// request.get(url, (error, response, body) => {
 // if (error) {
  //  console.log(error);
 // } else {
  //  const content = JSON.parse(body);
  //  const characters = content.characters;
    // console.log(characters);
   // for (const character of characters) {
     // request.get(character, (error, response, body) => {
      //  if (error) {
        //  console.log(error);
      //  } else {
         // const names = JSON.parse(body);
         // console.log(names.name);
       // }
     // });
   // }
 // }
// });

#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode} ${response.statusMessage}`);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  // Function to make a request for each character and print their names
  const printCharacterNames = (characterUrl) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Error: ${response.statusCode} ${response.statusMessage}`);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  };

  // Loop through each character URL and print their names
  characters.forEach(printCharacterNames);
});
