import socket
import sounddevice as sd
import numpy as np

HOST = '127.0.0.1'  # replace with the server's IP address
PORT = 1337  # replace with the server's port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f'Connected to {HOST}:{PORT}')
# replace with anything to perform any other given task
while True:
    # Record audio
    duration = 1  # 1 second
    sample_rate = 44100  # CD quality
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()  # Wait for recording to finish

    # Convert audio to bytes
    audio_bytes = audio.tobytes()

    # Send audio to server
    client_socket.sendall(audio_bytes)
