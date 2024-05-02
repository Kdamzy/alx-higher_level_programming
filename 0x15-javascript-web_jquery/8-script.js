// Queries an API and fetches all movie titles then
// iinserts them nto the UL#list_movies tag
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
