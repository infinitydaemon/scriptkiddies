import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
sock.bind(server_address)

sock.listen()

while True:
    # wait for a connection
    connection, client_address = sock.accept()
    try:
        # Receive data and log it to the log file
        with open("socket_log.txt", "a") as log_file:
            while True:
                data = connection.recv(16)
                if data:
                    log_file.write(data.decode())
                else:
                    break
    finally:
        # Cleanup
        connection.close()
