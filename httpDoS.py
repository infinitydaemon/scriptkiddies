import socket

target = 'TARGET_IP_ADDRESS'
port = 80
message = 'GET / HTTP/1.1\r\n'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target, port))

for i in range(1000):
    client.send(message.encode('utf-8'))

client.close()
