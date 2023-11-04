#!/usr/bin/node

$(document).ready(() => {
  $.ajax({
    type: 'GET',
    url: 'http://0.0.0.0:5000/api/v1/stats',
    success: (stats) => {
      // const numFaculty = $('h2#faculties');
      // const numDepts = $('h2#departments');
      // const numCourses = $('h2#courses');
      // const numStudents = $('h2#students');
      console.log(stats);
      for (let i = 0; i < Object.keys(stats).length; i++) {
        $('h2#' + Object.keys(stats)[i]).text(stats[Object.keys(stats)[i]]);
      }
    }
  });
}
);
