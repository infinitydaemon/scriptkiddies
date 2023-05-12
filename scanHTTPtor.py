# Scan a range of IP addresses over Tor and look for open HTTPd port.
import socket
import socks
import requests

def scan_internet_with_tor():
    target_ip = input("Enter the target IP range to scan (e.g., 192.168.0.0/24): ")

    # Split the target IP range into network address and subnet mask
    network_address, subnet_mask = target_ip.split('/')

    # Calculate the number of hosts in the subnet
    num_hosts = 2**(32 - int(subnet_mask))

    print(f"Scanning {num_hosts} hosts for port 80 open over Tor proxy...")

    # Set up Tor proxy. Define local or LAN based proxy
    socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
    socket.socket = socks.socksocket

    # Create a session with Tor proxy
    session = requests.session()

    # Iterate over each host in the subnet
    for i in range(1, num_hosts):
        # Construct the IP address to scan
        ip_address = f"{network_address}.{i}"

        # Try to make an HTTP request to the target IP address on port 80
        try:
            response = session.get(f"http://{ip_address}", timeout=2)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                print(f"Port 80 open on: {ip_address}")

        except (requests.exceptions.RequestException, socket.timeout):
            pass

    session.close()

scan_internet_with_tor()
