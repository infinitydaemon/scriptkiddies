// a simple responder in java that sends fixed replies and logs inputs to a file

const net = require('net');
const fs = require('fs');

const server = net.createServer(function (socket) {
  console.log('Connected: ' + socket.remoteAddress + ':' + socket.remotePort);

  socket.on('data', function (data) {
    console.log('Received: ' + data);

    fs.appendFileSync('handshake.log', `Received from ${socket.remoteAddress}:${socket.remotePort}: ${data}\n`);

    const greetings = ["Hello there!", "What's up?", "Hey, how's it going?", "Yo!", "Hiya!", "G'day mate!"];
    const randomGreeting = greetings[Math.floor(Math.random() * greetings.length)];
    socket.write(randomGreeting + "\n");
  });

  socket.on('close', function () {
    console.log('Connection closed: ' + socket.remoteAddress + ':' + socket.remotePort);
  });
});

server.listen(12345, function () {
  console.log('Listening on port 12345');
});
