$(document).ready(function() {
  load();
});

function load() {
  $.ajax({
    url: '/test/get/data',
    type: 'GET',
    data: {},
    success: function(response) {
      console.log(response);
    }
  })
}