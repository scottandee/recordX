#!/usr/bin/node

// This function loads all faculties from db into dropdown
function loadFilters (faculties) {
  // retrieve both the form and search box drop-down element
  const createFilter = $('select#res-filter');
  const searchFilter = $('select#search-dropdown');

  // loop through the faculties
  for (let i = 0; i < faculties.length; i++) {
    const option = $('<option>');
    option.attr('value', faculties[i].id);
    option.text(faculties[i].name);
    createFilter.append(option.clone());
    searchFilter.append(option);
  }
}
// This fuction sends a delete request for the specified
// id and resource name
function doDelete (id, resourceName) {
  $.ajax({
    type: 'DELETE',
    url: 'http://0.0.0.0:5000/api/v1/' + resourceName + '/' + id,
    success: () => {
      alert('deleted');
    }
  });
}

// This function loads up the departments that are part
// of the data parameter that is passed into the function
// onto the app
function loadDepartments (depts) {
  const departments = $('section.resources');
  for (let i = 0; i < Object.keys(depts).length; i++) {
    const card = $('<div>').addClass('card dept-card');
    const img = $('<img>');
    img.attr('src', 'images/faculty.png');
    card.append(img);

    const content = $('<div>').addClass('card-content');
    const resData = $('<div>').addClass('resource-data');

    resData.append($('<h4>').text('Name:'));
    resData.append($('<p>').text(depts[i].name));

    resData.append($('<h4>').text('Description:'));
    resData.append($('<p>').text(depts[i].description));

    resData.append($('<h4>').text('HOD:'));
    resData.append($('<p>').text(depts[i].hod));

    const resOptions = $('<div>').attr('id', 'options');
    const optionsDropdown = $('<div>').addClass('options-dropdown');
    optionsDropdown.attr('data-student-id', depts[i].id);

    const updateOption = $('<div>').addClass('update').html('<p>Update</p>');

    const deleteOption = $('<div>').addClass('delete').html('<p>Delete</p>');
    deleteOption.click(() => {
      if (confirm('Are you sure you want to delete this?')) {
        doDelete(depts[i].id, 'departments');
      }
    });
    optionsDropdown.append(updateOption, deleteOption);
    resOptions.append($('<i>').addClass('fas fa-ellipsis-v options-icon'));
    resOptions.append(optionsDropdown);

    content.append(resData);
    card.append(content, resOptions);

    departments.append(card);
  }
}

// This section of code requests for all of the faculties
// from the db and add updates the dropdown menu in the search
// bar and the form. It makes use of the loadFilters function
// to acheive this
$(document).ready(() => {
  $.ajax({
    type: 'GET',
    url: 'http://0.0.0.0:5000/api/v1/faculties',
    success: (faculties) => {
      loadFilters(faculties);
    }
  });
});

// This section of code loads up all of the depatrtments
// from the db when the page is loaded
$(document).ready(() => {
  $.ajax({
    type: 'POST',
    url: 'http://0.0.0.0:5000/api/v1/departments_search',
    datatype: 'json',
    contentType: 'application/json',
    data: JSON.stringify({}),
    success: (depts) => {
      $('section.resources').empty();
      loadDepartments(depts);
    }
  });
});

// This section of code works with the create new form.
// It sends a POST request to the server based on the
// data entered by the user
$(document).ready(() => {
  const formEl = $('#dept-form');

  formEl.on('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(formEl[0]);
    const facultyId = formData.get('faculty_id');
    formData.delete('faculty_id');
    const data = Object.fromEntries(formData);
    $.ajax({
      type: 'POST',
      url: 'http://0.0.0.0:5000/api/v1/faculties/' + facultyId + '/departments',
      datatype: 'json',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: (data) => {
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
      url: 'http://0.0.0.0:5000/api/v1/departments_search',
      datatype: 'json',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: (depts) => {
        $('section.resources').empty();
        console.log(depts);
        loadDepartments(depts);
      }
    });
  });
});
