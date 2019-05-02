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
  
  // this function is called when a "change" event happens on the "input" element in the HTML
function loadFile(event) {
    output.innerHTML = ""; // make sure to clear the output when getting a new file
    let file = event.target.files[0]; // the "change" event itself gets passed to this function
    
    // make sure the file is a CSV
    if (file.type !== "text/csv") {
      printToOutput("This app can only take CSV files!");
      return; // stop trying to do the other stuff in this function
  }
  import CSV from 'comma-separated-values';
function readCSV(flower){}
    const csv = new CSV(data, {header: true}).parse();
    const cols = [[],[],[],[]];
    csv.forEach(row => {
    row.forEach((cell, idx) => {
        cols[idx].push(cell);
    });
    })
    return flowers[flower]
  }

