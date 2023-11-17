$(document).ready(() => {
  $.ajax({
    type: 'GET',
    url: 'http://127.0.0.1:5000/api/v1/stats',
    success: (stats) => {
      console.log(stats);
      for (let i = 0; i < Object.keys(stats).length; i++) {
        $('h2#' + Object.keys(stats)[i]).text(stats[Object.keys(stats)[i]]);
      }
    }
  });
}
);
