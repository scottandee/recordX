#!/usr/bin/node
// This script contains functions to display
// dynamic content on the students page

// This function renders all filters for faculty and department
function loadFilters (data, target, name) {
  let option = $('<option>');
  const targetElem = $(target);
  option.text('Select a ' + name);
  option.attr('value', '');
  targetElem.empty();
  targetElem.append(option);

  for (let i = 0; i < data.length; i++) {
    option = $('<option>');
    option.attr('value', data[i].id);
    option.text(data[i].name);
    targetElem.append(option);
  }
}

// This function renders all filters for courses
function loadCourseFilters (data, target, name) {
  let option = $('<option>');
  const targetElem = $(target);
  option.text('Select a ' + name);
  targetElem.empty();
  targetElem.append(option);

  for (let i = 0; i < data.length; i++) {
    option = $('<option>');
    option.attr('value', data[i].id);
    option.text(data[i].code + ': ' + data[i].title);
    targetElem.append(option);
  }
}

// This fuction sends a delete request for the specified
// id and resource name
function doDelete (id, resourceName) {
  $.ajax({
    type: 'DELETE',
    url: 'https://www.scottandee.tech/api/v1/' + resourceName + '/' + id,
  });
}

function doUpdate (student) {
  // retreive and open the edit faculty modal
  const modal = $('[data-update-modal]');
  modal[0].showModal();

  // Fill the form with the existing values
  $.ajax({
    type: 'GET',
    url: 'https://www.scottandee.tech/api/v1/departments/' + student.department_id,
    success: (dept) => {
      $('.dept-name').text(dept.name);
    }
  });
  $('#put-first').val(student.first_name);
  $('#put-last').val(student.last_name);
  $('#put-email').text(student.email);
  $('#put-matric').text(student.matric_number);
  $('#put-addr').val(student.address);
  $('#put-dob').val(student.dob);
  $('#put-gender').text(student.gender);

  // load up courses in the department that is to be edited
  $.ajax({
    type: 'GET',
    url: 'https://www.scottandee.tech/api/v1/departments/' + student.department_id + '/courses',
    success: (courses) => {
      loadCourseFilters(courses, 'SELECT#put-courses', 'Course');
    }
  });

  // retreive courses selected by student and fill them into the edit form
  $.ajax({
    type: 'GET',
    url: 'https://www.scottandee.tech/api/v1//students/' + student.id + '/courses',
    success: (stuCourses) => {
      console.log(stuCourses);
      // $('#selected-courses-update').empty();
      for (let i = 0; i < stuCourses.length; i++) {
        $('#put-courses option:contains(' + stuCourses[i].course.title + ')').attr('selected', 'selected');
        $('#edit').click();
        $('li.put-course' + (stuCourses[i].course.id) + ' select option:contains(' + stuCourses[i].grade + ')').attr('selected', 'selected');
      }
    }
  });

  // retreive the edit form element
  const updateFormEl = $('#update-student-form');

  // add event listener to handle PUT action
  updateFormEl.on('submit', function (event) {
    event.preventDefault();
    const formData = new FormData(updateFormEl[0]);
    formData.delete('department_id');
    formData.delete('courses');
    const data = Object.fromEntries(formData);

    console.log(data);
    $.ajax({
      type: 'PUT',
      url: 'https://www.scottandee.tech/api/v1/students/' + student.id,
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: (data) => {
        console.log(data);
        updateFormEl[0].reset();
        modal[0].close();
      },
      error: (error) => {
        const errorMessage = error.responseJSON.error;
        alert(errorMessage);
      }
    });
  });
}

function showStudentDetails (student) {
  $.ajax({
    type: 'GET',
    url: 'https://www.scottandee.tech/api/v1/departments/' + student.department_id,
    success: (dept) => {
      $('.stu-dept-name').text(dept.name);
    }
  });
  $('.stu-first').text(student.first_name);
  $('.stu-last').text(student.last_name);
  $('.stu-email').text(student.email);
  $('.stu-matric').text(student.matric_number);
  $('.stu-addr').text(student.address);
  $('.stu-dob').text(student.dob);
  $('.stu-gender').text(student.gender);
  $.ajax({
    type: 'GET',
    url: 'https://www.scottandee.tech/api/v1//students/' + student.id + '/courses',
    success: (stuCourses) => {
      $('#selected-courses-dialog').empty();
      if (stuCourses.length === 0) {
        $('#selected-courses-dialog').html('<li><p>None</p></li>');
      }
      for (let i = 0; i < stuCourses.length; i++) {
        const li = $('<li>').addClass('enroll');
        li.html('<p class="cour-name">' + stuCourses[i].course.code + ': ' + stuCourses[i].course.title + '</p>' + '<p>' + stuCourses[i].grade + '</p>');
        $('#selected-courses-dialog').append(li);
      }
    }
  });
  $('[data-details]')[0].showModal();
}
function loadStudents (studs) {
  const students = $('section.resources');
  for (let i = 0; i < Object.keys(studs).length; i++) {
    const card = $('<div>').addClass('card');
    const img = $('<img>');
    img.attr('src', 'images/faculty.png');
    img.click(() => {
      showStudentDetails(studs[i]);
    });

    card.append(img);
    const content = $('<div>').addClass('card-content');
    const resData = $('<div>').addClass('student-data');

    content.click(() => {
      showStudentDetails(studs[i]);
    });

    resData.append($('<h4>').text('First Name:'));
    resData.append($('<p>').text(studs[i].first_name));

    resData.append($('<h4>').text('Last Name:'));
    resData.append($('<p>').text(studs[i].last_name));

    resData.append($('<h4>').text('Matric No:'));
    resData.append($('<p>').text(studs[i].matric_number));

    const resOptions = $('<div>').attr('id', 'options');
    const optionsDropdown = $('<div>').addClass('options-dropdown');
    optionsDropdown.attr('data-student-id', studs[i].id);

    const updateOption = $('<div>').addClass('update').html('<p>Update</p>');
    updateOption.click(() => {
      doUpdate(studs[i]);
    });

    const deleteOption = $('<div>').addClass('delete').html('<p>Delete</p>');
    deleteOption.click(() => {
      if (confirm('Are you sure you want to delete this?')) {
        doDelete(studs[i].id, 'students');
      }
    });

    optionsDropdown.append(updateOption, deleteOption);

    resOptions.append($('<i>').addClass('fas fa-ellipsis-v options-icon'));
    resOptions.append(optionsDropdown);

    content.append(resData);
    card.append(content, resOptions);

    students.append(card);
  }
}

// This function dynamically creates a grade dropdown
function createGradeDropDown (courseId) {
  const dropDown = $('<select>').attr({ name: courseId, id: 'grade' });
  let option = $('<option>').attr('value', 'Nil').text('Grade');
  dropDown.append(option);
  option = $('<option>').attr('value', 'A').text('A');
  dropDown.append(option);
  option = $('<option>').attr('value', 'B').text('B');
  dropDown.append(option);
  option = $('<option>').attr('value', 'C').text('C');
  dropDown.append(option);
  option = $('<option>').attr('value', 'D').text('D');
  dropDown.append(option);
  option = $('<option>').attr('value', 'E').text('E');
  return (dropDown);
}

// This section of code retreives all faculties and
// dynamically displays them on the search bar filters
$(document).ready(() => {
  $.ajax({
    type: 'GET',
    url: 'https://www.scottandee.tech/api/v1/faculties',
    success: (faculties) => {
      loadFilters(faculties, 'select#search-dropdown.fac', 'Faculty');
    }
  });
});

// This section of code listens for a change in the state
// of the faculty filter. Once a chage is observed, it loads
// up all departments of that faculty into the departments search bar filter
$(document).ready(() => {
  $('SELECT#search-dropdown.fac').on('change', () => {
    const selectedDept = $('SELECT#search-dropdown.fac option:selected');
    // console.log(selectedDept);
    const facId = selectedDept.attr('value');
    $.ajax({
      type: 'GET',
      url: 'https://www.scottandee.tech/api/v1/faculties/' + facId + '/departments',
      success: (depts) => {
        loadFilters(depts, 'select#search-dropdown.dept', 'Departments');
      }
    });
  });
});

// This section of code handles the addition/enrollment of courses.
// Similar to a to-do-list once a course is added, it'll be displayed
// in the list of added courses
$(document).ready(() => {
  const addCourseButton = $('button.add-course');
  const selected = $('#selected-courses');

  // The `added` array stores all added courses. This will help to
  // prevent multiple selection of one course
  const added = [];

  // Listen for a click on the `add` button
  addCourseButton.click((event) => {
    event.preventDefault();
    const select = $('select#courses option:selected');

    // check if the course that is selected is already in the `added` array
    if (!added.includes(select.attr('value'))) {
      // check if the course selected is not the placeholder
      if (select.attr('value') !== 'select') {
        const courseId = select.attr('value');// Get the course_id of the course to be added
        const course = $('<li>').addClass('added-course course' + courseId);// create a li with a unique class
        course.append(($('<i>').addClass('fas fa-times'))); // add remove icon
        course.append($('<p>').text(select.text())); // add remove icon
        course.append(createGradeDropDown(courseId)); // Add grade dropdown
        selected.append(course);// display on the screen

        added.push(courseId);// Add course id to `added` array

        const removeCourseIcon = $('li.course' + courseId + ' i'); // select the remove course icon

        // program response of remove icon when clicked
        removeCourseIcon.on('click', () => {
          const idx = added.indexOf(courseId);
          // remove from `added` array
          added.splice([idx], 1);

          // remove from document flow
          $('li.course' + courseId).remove();
          // console.log(added)
        });
      }
    }
  });
});
$(document).ready(() => {
  const addCourseButton = $('#edit');
  const selected = $('#selected-courses-update');
  let added = [];

  addCourseButton.click((event) => {
    event.preventDefault();
    const select = $('#put-courses option:selected');

    if (!added.includes(select.attr('value'))) {
      if (select.attr('value') !== 'select') {
        const courseId = select.attr('value');
        const course = $('<li>').addClass('added-course put-course' + courseId);
        course.append(($('<i>').addClass('fas fa-times')));
        course.append($('<p>').text(select.text()));
        course.append(createGradeDropDown(courseId));
        selected.append(course);
        added.push(courseId);

        const removeCourseIcon = $('li.put-course' + courseId + ' i');
        removeCourseIcon.on('click', () => {
          const idx = added.indexOf(courseId);
          added.splice([idx], 1);

          $('li.put-course' + courseId).remove();
        });
      }
    }
  });
  const close = $('[data-close-update-modal]');
  close.on('click', () => {
    added = [];
  });
});
// This section of code loads up departments for the `create new` form
$(document).ready(() => {
  $.ajax({
    type: 'GET',
    url: 'https://www.scottandee.tech/api/v1/departments',
    success: (depts) => {
      loadFilters(depts, 'SELECT#res-filter', 'Department');
    }
  });
});

// This section of code listens for a change in the state
// of the department filter. Once a chage is observed, it loads
// up all courses of that department into the courses that can be added
$(document).ready(() => {
  $('SELECT#res-filter').on('change', () => {
    const selectedDept = $('SELECT#res-filter option:selected');
    // console.log(selectedDept);
    const deptId = selectedDept.attr('value');
    $.ajax({
      type: 'GET',
      url: 'https://www.scottandee.tech/api/v1/departments/' + deptId + '/courses',
      success: (courses) => {
        loadCourseFilters(courses, 'SELECT#courses', 'Course');
      }
    });
  });
});

// This section of code handles the submission of the `create new` form
$(document).ready(() => {
  const studentForm = $('#student-form');

  studentForm.on('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(studentForm[0]); // Get form data
    const deptId = formData.get('department_id');
    formData.delete('department_id');
    formData.delete('courses');
    const data = Object.fromEntries(formData); // Convert into an object
    console.log(data);
    $.ajax({
      type: 'POST',
      url: 'https://www.scottandee.tech/api/v1/departments/' + deptId + '/students',
      datatype: 'json',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: (data) => {
        studentForm[0].reset();
      },
      error: (error) => {
        const errorMessage = error.responseJSON.error;
        alert(errorMessage);
      }
    });
  });
});

// This section of code loads up all of the students
// from the db when the page is loaded
$(document).ready(() => {
  $.ajax({
    type: 'POST',
    url: 'https://www.scottandee.tech/api/v1/students_search',
    datatype: 'json',
    contentType: 'application/json',
    data: JSON.stringify({}),
    success: (students) => {
      $('section.resources').empty();
      loadStudents(students);
    }
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
      url: 'https://www.scottandee.tech/api/v1/students_search',
      datatype: 'json',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: (students) => {
        $('section.resources').empty();
        console.log(students);
        loadStudents(students);
      }
    });
  });
});
