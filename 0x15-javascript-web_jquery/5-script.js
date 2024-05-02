// add a <li> element to a list when the user clicks
// DIV#add_item tag
$('div#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
  });

