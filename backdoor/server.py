import socket

HOST = '0.0.0.0'  # listen on all available interfaces
PORT = 1337  # choose any available port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f'Listening on {HOST}:{PORT}')

client_socket, client_address = server.accept()
print(f'Accepted connection from {client_address[0]}:{client_address[1]}')
