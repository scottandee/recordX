#!/usr/bin/node
// This script contains functions to display
// dynamic content onto the faculty page


// This fuction sends a delete request for the specified
// id and resource name
function doDelete (id, resourceName) {
  $.ajax({
    type: 'DELETE',
    url: 'https://recordx-0b6779f5e001.herokuapp.com/api/v1/' + resourceName + '/' + id,
    success: () => {
      location.reload();
    }
  });
}

// This function handles the update action
function doUpdate (fac) {
  // retreive and open the edit faculty modal
  const modal = $('[data-update-modal]');
  modal[0].showModal();

  // Fill the form with the existing values
  $('#put-name').val(fac.name);
  $('#put-description').val(fac.description);

  // retreive the edit form element
  const updateFormEl = $('#update-fac-form');

  // add event listener to handle PUT action
  updateFormEl.on('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(updateFormEl[0]);
    const data = Object.fromEntries(formData);
    console.log(data);
    $.ajax({
      type: 'PUT',
      url: 'https://recordx-0b6779f5e001.herokuapp.com/api/v1/faculties/' + fac.id,
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: (data) => {
        console.log(data);
        updateFormEl[0].reset();
        location.reload();
      },
      error: (error) => {
        const errorMessage = error.responseJSON.error;
        alert(errorMessage);
      }
    });
  });
}

// This function retrieves a faculty's details from the
// API and displays them in the details modal.
function showFacultyDetails (faculty) {
  $('.fac-name').text(faculty.name);
  $('.fac-description').text(faculty.description);
  $('[data-details]')[0].showModal();
}

// This function loads up the faculties that are part
// of the facs parameter that is passed into the function
// onto the app
function loadFaculties (facs) {
  // reterive the container element that will contain all faculties
  const facultySection = $('section#faculties');
  facultySection.append($('<h2>').text('Faculties'));
  facultySection.append($('<div>').addClass('resources'));
  const faculties = $('div.resources');

  // loop through all the facs
  for (let i = 0; i < Object.keys(facs).length; i++) {
    const card = $('<div>').addClass('card');
    const banner = $('<div>').addClass('card-banner-faculty');
    card.append(banner);

    const content = $('<div>').addClass('card-content');
    const resData = $('<div>').addClass('resource-data');
    content.click(() => {
      showFacultyDetails(facs[i]);
    });

    resData.append($('<h4>').text(facs[i].name));

    const resOptions = $('<div>').addClass('options');
    resOptions.attr('id', 'option-' + facs[i].id);
    const optionsDropdown = $('<div>').addClass('options-dropdown');
    optionsDropdown.attr('data-faculty-id', facs[i].id);
    resOptions.click(() => {
      optionsDropdown.addClass('show');
    });

    const updateOption = $('<div>').addClass('update').html('<p>Update</p>');
    updateOption.click(() => {
      doUpdate(facs[i]);
    });

    const deleteOption = $('<div>').addClass('delete').html('<p>Delete</p>');
    deleteOption.click(() => {
      if (confirm('Are you sure you want to delete this?')) {
        doDelete(facs[i].id, 'faculties');
      }
    });
    optionsDropdown.append(updateOption, deleteOption);
    resOptions.append($('<i>').addClass('fas fa-ellipsis-v options-icon'));
    resOptions.append(optionsDropdown);

    content.append(resData);
    card.append(content, resOptions);

    faculties.append(card);
  }
  facultySection.append(faculties);
}

// This section of code loads up all of the faculties
// from the db when the page is loaded
$(document).ready(() => {
  $.ajax({
    type: 'POST',
    url: 'https://recordx-0b6779f5e001.herokuapp.com/api/v1/faculties_search',
    datatype: 'json',
    contentType: 'application/json',
    data: JSON.stringify({}),
    success: (facs) => {
      $('section#faculties').empty();
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
      url: 'https://recordx-0b6779f5e001.herokuapp.com/api/v1/faculties',
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: (data) => {
        console.log(data);
        formEl[0].reset();
        location.reload();
      },
      error: (error) => {
        console.log(error);
        const errorMessage = error.responseJSON.error;
        alert(errorMessage);
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
      url: 'https://recordx-0b6779f5e001.herokuapp.com/api/v1/faculties_search',
      datatype: 'json',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: (facs) => {
        $('section#faculties').empty();
        console.log(facs);
        loadFaculties(facs);
      }
    });
  });
});
