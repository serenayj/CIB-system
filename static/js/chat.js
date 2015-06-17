function saveRecord(historyrecord){

    alert("historyrecord save");
    $.ajax({
    type :"POST",
    url : "chat/saverecord/",
    dataType: "json",
    data :{
      'history' : historyrecord,
    },
    success: function(data){
        alert("data saved successfully");

        }
    });
}

$(document).ready( function() {

    var inputBox = document.getElementById("inputbox");

    inputbox.addEventListener("keydown", function(e) {
      if (!e) { var e = window.event; }

      if (e.keyCode == 13 && inputbox.value.value!='') { 
        e.preventDefault(); // sometimes useful
        var myObj = new Object();

        myObj.type = "chat";
        myObj.text = inputbox.value;
        myObj.userid = $('#curr-user-name').attr('value');//$("#curr-user-id").html();

        var passingObj = JSON.stringify(myObj);
        saveRecord(passingObj);
        share.send(passingObj);
        inputbox.value="";
      
      }
    }, false);

});