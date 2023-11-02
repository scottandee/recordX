#!/usr/bin/node
// This script contains functions to display
// dynamic content on the students page

// This function renders all filters for faculty and department
function loadFilters (data, target, name) {
  let option = $('<option>');
  const targetElem = $(target);
  option.text('Select a ' + name);
  option.attr('value', '')
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

function loadStudents (studs) {
  const students = $('section.resources');
  for (let i = 0; i < Object.keys(studs).length; i++) {
    const card = $('<div>').addClass('card');
    const img = $('<img>');
    img.attr('src', 'images/faculty.png');
    card.append(img);

    const content = $('<div>').addClass('card-content');
    const resData = $('<div>').addClass('resource-data');

    resData.append($('<h4>').text('First Name:'));
    resData.append($('<p>').text(studs[i].first_name));

    resData.append($('<h4>').text('Last Name:'));
    resData.append($('<p>').text(studs[i].last_name));

    resData.append($('<h4>').text('Matric No:'));
    resData.append($('<p>').text(studs[i].matric_number));

    content.append(resData);
    card.append(content);
    card.append($('<i>').addClass('fas fa-ellipsis-v'));

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
    url: 'http://0.0.0.0:5000/api/v1/faculties',
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
      url: 'http://0.0.0.0:5000/api/v1/faculties/' + facId + '/departments',
      success: (depts) => {
        loadFilters(depts, 'select#search-dropdown.dept', 'Departments');
      }
    });
  });
});

// This section of code handles the addition/enrollment of courses.
// Simoilar to a to-do-list once a course is added, it'll be displayed
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

// This section of code loads up departments for the `create new` form
$(document).ready(() => {
  $.ajax({
    type: 'GET',
    url: 'http://0.0.0.0:5000/api/v1/departments',
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
      url: 'http://0.0.0.0:5000/api/v1/departments/' + deptId + '/courses',
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
      url: 'http://0.0.0.0:5000/api/v1/departments/' + deptId + '/students',
      datatype: 'json',
      contentType: 'application/json',
      data: JSON.stringify(data),
      success: (data) => {
        studentForm[0].reset();
      }
    });
  });
});

// This section of code loads up all of the students
// from the db when the page is loaded
$(document).ready(() => {
  $.ajax({
    type: 'POST',
    url: 'http://0.0.0.0:5000/api/v1/students_search',
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
      url: 'http://0.0.0.0:5000/api/v1/students_search',
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