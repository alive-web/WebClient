var socket = new WebSocket("ws://localhost:8888");
var message_text = document.getElementById('msg_box')

function send() {
  socket.send(message_text.value);
  message_text.value =''
}

socket.onmessage = function(event) {
  var incomingMessage = event.data;
  addMessageBlock(incomingMessage)
  
}

function addMessageBlock (msg) {
	var msg_div = document.createElement("div")
	msg_div.innerText = msg
	msg_div.className = "well"
	$(msg_div).appendTo("#msg_block")
	
}