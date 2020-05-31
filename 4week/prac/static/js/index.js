$(document).ready(function() {
  load();
});

function load() {
  $.ajax({
    url: '/test/get/data?username=sparta&password=12345',
    type: 'GET',
    data: {},
    success: function(response) {
      console.log(response);
    }
  })
}