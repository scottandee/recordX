#!/usr/bin/node
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
