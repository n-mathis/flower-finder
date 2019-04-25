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
    $(".nav li").removeClass("active");//this will remove the active class from  
                                       //previously active menu item 
    $('#home').addClass('active');
    //for identify
    $('#identify').addClass('active');
    //for database 
    $('#database').addClass('active');
    //for citations 
    $('#citations').addClass('active');
});
// $(document).ready(function () {
//     // Init
//     $('.image-section').hide();
//     $('.loader').hide();
//     $('#result').hide();

//     // Upload Preview
//     function readURL(input) {
//         if (input.files && input.files[0]) {
//             var reader = new FileReader();
//             reader.onload = function (e) {
//                 $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
//                 $('#imagePreview').hide();
//                 $('#imagePreview').fadeIn(650);
//             }
//             reader.readAsDataURL(input.files[0]);
//         }
//     }
//     $("#imageUpload").change(function () {
//         $('.image-section').show();
//         $('#btn-predict').show();
//         $('#result').text('');
//         $('#result').hide();
//         readURL(this);
//     });

//     // Predict
//     $('#btn-predict').click(function () {
//         var form_data = new FormData($('#upload-file')[0]);

//         // Show loading animation
//         $(this).hide();
//         $('.loader').show();

//         // Make prediction by calling api /predict
//         $.ajax({
//             type: 'POST',
//             url: '/predict',
//             data: form_data,
//             contentType: false,
//             cache: false,
//             processData: false,
//             async: true,
//             success: function (data) {
//                 // Get and display the result
//                 $('.loader').hide();
//                 $('#result').fadeIn(600);
//                 $('#result').text(' Model Predict the Water as:  ' + data);
//                 console.log('Success!');
//             },
//         });
//     });

// });
