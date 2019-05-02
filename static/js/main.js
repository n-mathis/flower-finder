function openInfo(evt, infoType) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(infoType).style.display = "block";
    evt.currentTarget.className += " active";
  }
//   $('#myForm').on('submit', function(e){
//     $('#myModal').modal('show');
//     e.preventDefault();
//   });

//   $('#myFormSubmit').click(function(e){
//     e.preventDefault();
//     alert($('#myField').val());
//     /*
//     $.post('http://path/to/post', 
//        $('#myForm').serialize(), 
//        function(data, status, xhr){
//          // do something here with response;
//        });
//     */
// });
// $("#submit-button").submit(function(e){
//     $('#largeModal').modal('show');
//     return false;
// });
// $(document).ready(function() {
//     $('#submit-button').on('submit', function(e){
//         $('#largeModal').modal('show');
//         e.preventDefault();
//     });
//   });
// $(function() {
//     $('button').click(function() {
//         $.ajax({
//             url: '/more',
//             data: $('form').serialize(),
//             type: 'POST',
//             success: function(response) {
//                 console.log(response);
//             },
//             error: function(error) {
//                 console.log(error);
//             }
//         });
//     });
// });

// $(document).ready(function() {

//     $("#submit").click(function() {
   
//        var val = 1;
//        var entry1 = 3;
   
//        $.getJSON({
//        url: "/getData",
//        data: { entry2_id: val, entry1_id: entry1 },
//        success: function(data){
//            $("#varID").html(data.var1);
//        }
//        });
   
//     });
   
//    });

$.getJSON( '/getData', { 'thing' : some_js_value } , function( data ) {
    //do stuff with data
});