import requests
import time
import socks
import socket
import stem.process

tor_process = stem.process.launch_tor_with_config(
    config = {
        'SocksPort': str(9050),
        'ExitNodes': '{us}'
    },
    init_msg_handler = print
)

socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket

wordlist = open("dictionary.txt", "r")
words = wordlist.readlines()
wordlist.close()

domain = "example.com"

for word in words:
    word = word.strip()
    subdomain = word + "." + domain
    url = "http://" + subdomain
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(subdomain + " exists!")
    except:
        pass
    time.sleep(1)
    
tor_process.kill()
