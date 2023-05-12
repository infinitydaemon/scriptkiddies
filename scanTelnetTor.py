import socks
import socket
from stem.control import Controller

def scan_internet_via_tor():
    target_ip = input("Enter the target IP range to scan (e.g., 192.168.0.0/24): ")

    # Split the target IP range into network address and subnet mask
    network_address, subnet_mask = target_ip.split('/')

    # Calculate the number of hosts in the subnet
    num_hosts = 2**(32 - int(subnet_mask))

    print(f"Scanning {num_hosts} hosts for port 23 (Telnet) over Tor...")

    # Set up Tor proxy connection
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()

        # Set up socket with Tor proxy
        socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
        socket.socket = socks.socksocket

        # Iterate over each host in the subnet
        for i in range(1, num_hosts):
            # Construct the IP address to scan
            ip_address = f"{network_address}.{i}"

            # Try to connect to the target IP address on port 23 (Telnet)
            try:
                socket.setdefaulttimeout(1)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((ip_address, 23))
                
                # Check if the port is open
                if result == 0:
                    print(f"Machine with port 23 open found: {ip_address}")
                    
                sock.close()

            except socket.error:
                pass

scan_internet_via_tor()
