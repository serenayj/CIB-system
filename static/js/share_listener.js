$(document).ready( function() {

    alert("share function loaded");
  
    window.share = {};
    share.ws = $.gracefulWebSocket("ws://127.0.0.1:1035/ws");
    share.send = function (message) {
      share.ws.send(message);
    }

    share.ws.onmessage = function (event) {
      var messageFromServer = event.data;
      var list_element = document.createElement('li');
      list_element.innerHTML = messageFromServer;
      $("#itemlist ul").prepend(list_element);
    };

    var inputBox = document.getElementById("mytext");

    inputbox.addEventListener("keydown", function(e) {
      if (!e) { var e = window.event; }

      if (e.keyCode == 13) { 
        e.preventDefault(); // sometimes useful
        alert("about to send");
        share.send(inputbox.value);  
        inputbox.value="";
      }
    }, false);

    });