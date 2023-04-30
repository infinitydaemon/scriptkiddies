import os
import zipfile
import ftplib

ftp_server = 'ftp.example.com'
ftp_user = 'username'
ftp_pass = 'password'

local_file_path = '/Users/username'
remote_file_path = '/backup.zip'

zip_file = zipfile.ZipFile('backup.zip', 'w', zipfile.ZIP_DEFLATED)
for root, dirs, files in os.walk(local_file_path):
    for file in files:
        zip_file.write(os.path.join(root, file))
zip_file.close()

with ftplib.FTP(ftp_server) as ftp:
    ftp.login(user=ftp_user, passwd=ftp_pass)
    with open('backup.zip', 'rb') as f:
        ftp.storbinary('STOR ' + remote_file_path, f)
