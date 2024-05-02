//  fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// displays the value of hello fro the fetch
// DIV#hello tag
$('document').ready(function () {
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
