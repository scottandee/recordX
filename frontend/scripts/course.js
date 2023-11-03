#!/usr/bin/node

function loadFilters (depts) {
  // retrieve both the form and search box drop-down element
  const createFilter = $('select#res-filter');
  const searchFilter = $('select#search-dropdown');

  // loop through the faculties
  for (let i = 0; i < depts.length; i++) {
    const option = $('<option>');
    option.attr('value', depts[i].id);
    option.text(depts[i].name);
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
      alert(deleted);
    }
  });
}
// This function loads up the courses that are part
// of the course parameter that is passed into the function
// onto the app
function loadCourses (courses) {
  const coursesDisplay = $('section.resources');
  for (let i = 0; i < Object.keys(courses).length; i++) {
    const card = $('<div>').addClass('card dept-card');
    const img = $('<img>');
    img.attr('src', 'images/faculty.png');
    card.append(img);

    const content = $('<div>').addClass('card-content');
    const resData = $('<div>').addClass('resource-data');

    resData.append($('<h4>').text('Title:'));
    resData.append($('<p>').text(courses[i].title));

    resData.append($('<h4>').text('Description:'));
    resData.append($('<p>').text(courses[i].description));

    resData.append($('<h4>').text('Instructor:'));
    resData.append($('<p>').text(courses[i].instructor));

    const resOptions = $('<div>').attr('id', 'options');
    const optionsDropdown = $('<div>').addClass('options-dropdown');
    optionsDropdown.attr('data-student-id', courses[i].id);

    const updateOption = $('<div>').addClass('update').html('<p>Update</p>');
    const deleteOption = $('<div>').addClass('delete').html('<p>Delete</p>');
    deleteOption.click(() => {
      if (confirm('Are you sure you want to delete this?')) {
        doDelete(courses[i].id, 'courses');
      }
    });

    optionsDropdown.append(updateOption, deleteOption);

    resOptions.append($('<i>').addClass('fas fa-ellipsis-v options-icon'));
    resOptions.append(optionsDropdown);

    content.append(resData);
    card.append(content, resOptions);

    coursesDisplay.append(card);
  }
}

$(document).ready(() => {
  $.ajax({
    type: 'GET',
    url: 'http://0.0.0.0:5000/api/v1/departments',
    success: (depts) => {
      loadFilters(depts);
    }
  });
});

// This section of code works with the create new form.
// It sends a POST request to the server based on the
// data entered by the user
$(document).ready(() => {
  const formEl = $('#course-form');

  formEl.on('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(formEl[0]);
    const deptId = formData.get('department_id');
    formData.delete('department_id');
    const data = Object.fromEntries(formData);
    console.log(data);
    $.ajax({
      type: 'POST',
      url: 'http://0.0.0.0:5000/api/v1/departments/' + deptId + '/courses',
      datatype: 'json',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: (data) => {
        formEl[0].reset();
      }
    });
  });
});

// This section of code loads up all of the depatrtments
// from the db when the page is loaded
$(document).ready(() => {
  $.ajax({
    type: 'POST',
    url: 'http://0.0.0.0:5000/api/v1/courses_search',
    datatype: 'json',
    contentType: 'application/json',
    data: JSON.stringify({}),
    success: (courses) => {
      $('section.resources').empty();
      loadCourses(courses);
    }
  });
});

// This section of code handles the search feature.
// Whatever data that is entered by the user is
// relayed to the server. The response is then
// displayed in the resources section
$(document).ready(() => {
  const searchFormEl = $('form.search-box');

  searchFormEl.on('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(searchFormEl[0]);
    const data = Object.fromEntries(formData);
    $.ajax({
      type: 'POST',
      url: 'http://0.0.0.0:5000/api/v1/courses_search',
      datatype: 'json',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: (courses) => {
        $('section.resources').empty();
        loadCourses(courses);
      }
    });
  });
});
