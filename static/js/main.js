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
$(document).ready(function () {
    $(".nav li").removeClass("active"); //this will remove the active class from  
                                        //previously active menu item 
    $('#home').addClass('active');
    //for about
    $('#about').addClass('active');
    //for identify
    $('#identify').addClass('active');
    //for database 
    $('#database').addClass('active');
    //for citations 
    $('#citations').addClass('active');
});
