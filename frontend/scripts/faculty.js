#!/usr/bin/node

// This fuction sends a delete request for the specified
// id and resource name
function doDelete (id, resourceName) {
  $.ajax({
    type: 'DELETE',
    url: 'http://0.0.0.0:5000/api/v1/' + resourceName + '/' + id,
    success: () => {
      alert(deleted);
    }
  });
}
// This function loads up the faculties that are part
// of the facs parameter that is passed into the function
// onto the app
function loadFaculties (facs) {
  const faculties = $('section.resources');
  for (let i = 0; i < Object.keys(facs).length; i++) {
    const card = $('<div>').addClass('card');
    const img = $('<img>');
    img.attr('src', 'images/faculty.png');
    card.append(img);

    const content = $('<div>').addClass('card-content');
    const resData = $('<div>').addClass('resource-data');

    resData.append($('<h4>').text('Name:'));
    resData.append($('<p>').text(facs[i].name));

    resData.append($('<h4>').text('Description:'));
    resData.append($('<p>').text(facs[i].description));

    const resOptions = $('<div>').attr('id', 'options');
    const optionsDropdown = $('<div>').addClass('options-dropdown');
    optionsDropdown.attr('data-student-id', facs[i].id);

    const updateOption = $('<div>').addClass('update').html('<p>Update</p>');

    const deleteOption = $('<div>').addClass('delete').html('<p>Delete</p>');
    deleteOption.click(() => {
      if (confirm('Are you sure you want to delete this?')) {
        doDelete(facs[i].id, 'faculties');
      }
    });
    optionsDropdown.append(updateOption, deleteOption);
    resOptions.append($('<i>').addClass('fas fa-ellipsis-v options-icon'));
    resOptions.append(optionsDropdown);
    // resData.append($('<h4>').text('Dean:'));
    // resData.append($('<p>').text(depts[i].hod));

    content.append(resData);
    card.append(content, resOptions);

    faculties.append(card);
  }
}
// This section of code loads up all of the faculties
// from the db when the page is loaded
$(document).ready(() => {
  $.ajax({
    type: 'POST',
    url: 'http://0.0.0.0:5000/api/v1/faculties_search',
    datatype: 'json',
    contentType: 'application/json',
    data: JSON.stringify({}),
    success: (facs) => {
      $('section.resources').empty();
      loadFaculties(facs);
    }
  });
});

$(document).ready(() => {
  const formEl = $('#fac-form');

  formEl.on('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(formEl[0]);
    const data = Object.fromEntries(formData);
    console.log(data);
    $.ajax({
      type: 'POST',
      url: 'http://0.0.0.0:5000/api/v1/faculties',
      datatype: 'json',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: (data) => {
        console.log(data);
        formEl[0].reset();
      }
    });
  });
});

// This section of code handles the search feature.
// Whatever data that is entered by the user is
// relayed to the server. The response os then
// displayed on the screen
$(document).ready(() => {
  const searchFormEl = $('form.search-box');

  searchFormEl.on('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(searchFormEl[0]);
    const data = Object.fromEntries(formData);
    console.log(data);
    $.ajax({
      type: 'POST',
      url: 'http://0.0.0.0:5000/api/v1/faculties_search',
      datatype: 'json',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: (facs) => {
        $('section.resources').empty();
        console.log(facs);
        loadFaculties(facs);
      }
    });
  });
});
