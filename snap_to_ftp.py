import cv2
import time
import ftplib

camera = cv2.VideoCapture(0)
ftp = ftplib.FTP('ftp.example.com', 'username', 'password')
ftp.cwd('/path/to/destination/directory')

while True:
    ret, frame = camera.read()
    if not ret:
        continue

    filename = f"image_{int(time.time())}.jpg"
    cv2.imwrite(filename, frame)

    with open(filename, 'rb') as file:
        ftp.storbinary(f'STOR {filename}', file)

    time.sleep(5)

camera.release()
cv2.destroyAllWindows()
ftp.quit()
