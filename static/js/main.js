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
// function CSVToArray(filename){
//     var cols = 13;
//     var allTextLines = allText.split(/\r\n|\n/);
//     var entries = allTextLines[0].split(',');
//     var lines = [];

//     var headings = entries.splice(0,cols);
//     while (entries.length>0) {
//         var tarr = [];
//         for (var j=0; j<cols; j++) {
//             tarr.push(headings[j]+":"+entries.shift());
//         }
//         lines.push(tarr);
//     }

//     with open('../cs121/app/flower-data.csv') as f:
//         csv_f = csv.reader(f)
//         flowers = {}
//         for row in csv_f:
//             flowers[row[0]] = row
//         return flowers[prediction]

// }