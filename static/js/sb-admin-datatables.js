// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable(
   {
  "ajax": {
    "url": "/db/urls/@urls",

    }
  }
  );
});
