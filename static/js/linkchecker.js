$(document).ready(function() {

   $.ajax({
       url: '/db/urls',
       headers: {Authorization: "Basic " + btoa('root:root')},
       success: function (data) {
          $.each(data['items'], function (idx, value) {
              $.ajax({
                  url: value['@id'],
                  headers: {Authorization: "Basic " + btoa('root:root')},
                  success: function (data) {
                    $('#dataTable').append('<tr><td>' + data['url'] +'</td><td>' + data['status'] + '</td><td>' + data['reason'] + '</td><td>' + data['last_visited'] +'</td></tr>');
              }});
          });
       }
   })


});
