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
  $('#myForm').on('submit', function(e){
    $('#myModal').modal('show');
    e.preventDefault();
  });

  $('#myFormSubmit').click(function(e){
    e.preventDefault();
    alert($('#myField').val());
    /*
    $.post('http://path/to/post', 
       $('#myForm').serialize(), 
       function(data, status, xhr){
         // do something here with response;
       });
    */
});
$("#submit-button").submit(function(e){
    $('#registration').modal('show');
    return false;
});
$(document).ready(function() {
    $('#submit-button').on('submit', function(e){
        $('#registration').modal('show');
        e.preventDefault();
    });
  });